#LEGB - Local, Enclosing, Global, Built-in

x = 0

def f1():
    x = 1
    print(x)

    def f2():
        x = 2
        print(x)
    f2()

print(x)
f1()