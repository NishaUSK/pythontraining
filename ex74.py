#multilevel inheritance
class A:
    a=10
    b=20
class B(A):
    pass #empty class
class C(B):
    pass
oa=A()
ob=B()
oc=C()
print("data of class A & it's object")
print(A.a,A.b)
print(oa.a,oa.b)
print("data of class B & it's object")
print(B.a,B.b)
print(ob.a,ob.b)
print("data of class C & it's object")
print(C.a,C.b)
print(oc.a,oc.b)
print("------------------------")
print("modification w.r.t class A")
A.a=24
print("data of class A & it's object")
print(A.a,A.b)
print(oa.a,oa.b)
print("data of class B & it's object")
print(B.a,B.b)
print(ob.a,ob.b)
print("data of class C & it's object")
print(C.a,C.b)
print(oc.a,oc.b)
print("------------------------")
print("modification w.r.t class B")
B.a=45
print("data of class A & it's object")
print(A.a,A.b)
print(oa.a,oa.b)
print("data of class B & it's object")
print(B.a,B.b)
print(ob.a,ob.b)
print("data of class C & it's object")
print(C.a,C.b)
print(oc.a,oc.b)
print("------------------------")
print("modification w.r.t class C")
C.a=33
print("data of class A & it's object")
print(A.a,A.b)
print(oa.a,oa.b)
print("data of class B & it's object")
print(B.a,B.b)
print(ob.a,ob.b)
print("data of class C & it's object")
print(C.a,C.b)
print(oc.a,oc.b)
print("------------------------")
