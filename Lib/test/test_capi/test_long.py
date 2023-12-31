import unittest
import sys

from test.support import import_helper

# Skip this test if the _testcapi module isn't available.
_testcapi = import_helper.import_module('_testcapi')


class LongTests(unittest.TestCase):

    def test_compact(self):
        for n in {
            # Edge cases
            *(2**n for n in range(66)),
            *(-2**n for n in range(66)),
            *(2**n - 1 for n in range(66)),
            *(-2**n + 1 for n in range(66)),
            # Essentially random
            *(37**n for n in range(14)),
            *(-37**n for n in range(14)),
        }:
            with self.subTest(n=n):
                is_compact, value = _testcapi.call_long_compact_api(n)
                if is_compact:
                    self.assertEqual(n, value)

    def test_compact_known(self):
        # Sanity-check some implementation details (we don't guarantee
        # that these are/aren't compact)
        self.assertEqual(_testcapi.call_long_compact_api(-1), (True, -1))
        self.assertEqual(_testcapi.call_long_compact_api(0), (True, 0))
        self.assertEqual(_testcapi.call_long_compact_api(256), (True, 256))
        self.assertEqual(_testcapi.call_long_compact_api(sys.maxsize),
                         (False, -1))

    def test_long_asint(self):
        PyLong_AsInt = _testcapi.PyLong_AsInt
        INT_MIN = _testcapi.INT_MIN
        INT_MAX = _testcapi.INT_MAX

        # round trip (object -> int -> object)
        for value in (INT_MIN, INT_MAX, -1, 0, 1, 123):
            with self.subTest(value=value):
                self.assertEqual(PyLong_AsInt(value), value)

        # use __index__(), not __int__()
        class MyIndex:
            def __index__(self):
                return 10
            def __int__(self):
                return 22
        self.assertEqual(PyLong_AsInt(MyIndex()), 10)

        # bound checking
        with self.assertRaises(OverflowError):
            PyLong_AsInt(INT_MIN - 1)
        with self.assertRaises(OverflowError):
            PyLong_AsInt(INT_MAX + 1)

        # invalid type
        for value in (1.0, b'2', '3'):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    PyLong_AsInt(value)


if __name__ == "__main__":
    unittest.main()
