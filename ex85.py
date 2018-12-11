#list inside a list
a=[]
m=int(input("enter the no.of values"))
for i in range(m):
    n=int(input("enter the no.of elements"))
    if n>1:
        b=[]
        for j in range(n):
            c=int(input("enter the values"))
            b.append(c)
    else:
        b=int(input("enter the value"))
    a.append(b)
    print(a)
    print("-----------------------")
