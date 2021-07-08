X = 0.04
y = 15
a = 5000

def help(v, m):

    i=1

    while i < m:

        v*=help(v, m)
        i+=1

    return v


def function1():
    global X
    global y
    global a

    return a * help((1+X), y)

