def TOH(n,A,B,C):
    if n> 0:
        TOH(n-1,A,C,B)
        print("move from %d to %d using %d" % (A,C,B))
        TOH(n-1,B,A,C)

TOH(100,1,2,3)