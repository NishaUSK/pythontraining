#multiple inheritance
class A:
    a=10
    b=20
class B:
    c=11
    d=21
class C(A,B):
    pass
oa=A()
ob=B()
oc=C()
print("membe of class A")
print(A.a,A.b)
print(oa.a,oa.b)
print("---------------")
print("membe of class b")
print(B.c,B.d)
print(ob.c,ob.d)
print("---------------")
print("membe of class C")
print(C.c,C.d,C.a,C.b)
print(oc.c,oc.d,oc.a,oc.b)
