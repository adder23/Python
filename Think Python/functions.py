import math

degrees = 45
radians = degrees / 180 * math.pi

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

#zadacha 1
def right_justify(s):
    space = (" "*70)
    cat = space + s
    print(cat)
    print(len(cat))

#right_justify("asd")

#zadacha 2
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')


def print_twice(bruce):
    print(bruce)
    print(bruce)


#do_twice(print_twice , "asd")
def do_four(f):
    do_twice(f)
    do_twice(f)

#do_four(print,"123")

#zadacha 3
def print_top():
    print("+", "- "*4, end="")

def print_top_end():
    print ("+")

def print_mid():
    print ("|", " "*8, end="")

def print_mid_end():
    mid_end = print ("|")

def print_row():
    do_four(print_top)
    print_top_end()
    do_four(print_mid)
    print_mid_end()
    do_four(print_mid)
    print_mid_end()
    do_four(print_mid)
    print_mid_end()
    do_four(print_mid)
    print_mid_end()

def kvadrat():
    do_four(print_row)
    do_four(print_top)
    print_top_end()
kvadrat()


