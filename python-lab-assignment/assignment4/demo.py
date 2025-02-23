# x=2
# def test():
#     global x
#     x = x+1
#     print(x)
# print(x)

a =4
def f():
    a = 5
    def g():
        nonlocal a
        a=10
        print("inside g",a)
    g()
    print("inside f",a)
f()
