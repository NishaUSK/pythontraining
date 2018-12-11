a={}
m=int(input("enter the no.of values"))
for i in range(m):
    d=input("enter the key")
    n=int(input("enter the no.of values"))
    if n>1:
        b={}
        for j in range(n):
            e=input("enter the key")
            c=input("enter the value")
            b[e]=c
    else:
        b=input("enter the value")
    a[d]=b
    print(a)
    print("----------------------------")
