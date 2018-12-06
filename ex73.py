#inheritance
class A:
    a=10
    b=20
class B(A):
    pass
print("data of class A")
print(A.a,A.b)
print("data of class B")
print(B.a,B.b)
print("madification w.r.t A")
A.a=30
print("---------------------")
print("data of class A")
print(A.a,A.b)
print("data of class B")
print(B.a,B.b)
print("---------------------")
print("madification w.r.t B")
B.a=55
print("data of class A")
print(A.a,A.b)
print("data of class B")
print(B.a,B.b)
