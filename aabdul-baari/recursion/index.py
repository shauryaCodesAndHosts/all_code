def func1(n):
    if n>0:
        print(n)
        func1(n-1)

def func2(n):
    if n> 0:
        func2(n-1)
        print(n)

vv=0
def func3(n):
    if n > 0:
        global vv
        vv = vv+1
        return func3(n-1) + vv
        # 3 + 3 + 3 = 9 
    return 0

def recFunc(n):
    if n>0:
        print(n)
        recFunc(n-1)
        recFunc(n-1)

n = 3
print(recFunc(3))