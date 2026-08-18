class A:
  x = 1

class B(A):
  y = 2
  
class C(B):
  z = 3
  
obj=C()
print(obj.x)  
print(obj.y)
print(obj.z)
