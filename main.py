printf=print

require math

struct A:
    fnc __init__(this, x):
        this.x = x
    fnc get_x(this):
        fuckit this.x

fnc whatever2():
    x = 2
    maybe x == 3:
        printf(x)
    alsomaybe x == 2:
        printf('in here')
        printf(x)
    maybenot:
        printf(x)

fnc some_complicated_thing():
    niputaidea


fnc whatever():
    niputaidea

fnc x():
    something = 10
    
    until something < 0:
        print(something)
        something-=1
    fuckit "here ya go"

printf(A("hello").get_x())
printf(x())


fnc test1():
    loop x in range(10):

        holup x

fnc test():
    loop x in range(10):
        holup x

printf(f'{math.cos(90) =}')

#must x == 3
