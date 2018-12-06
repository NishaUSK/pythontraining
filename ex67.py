class demo:
    a=45
    b=55
obj=demo()
print("accessing w.r.t cname")
print(demo.a,demo.b)
print("modification w.r.t classname")
demo.a=90
print("accessing w.r.t cname")
print(demo.a,demo.b)
print("accessing w.r.t objname")
print(obj.a,obj.b)
