X = 0.04
y = 15
a = 5000

def loop(a, v):

    return a if v<=0 else a * loop(a, v-1)


def function1():
    global X
    global y
    global a

    return a * loop((1+X), v=y)
