a=int(input("enter side1: "))
b=int(input("enter side1: "))
c=int(input("enter side1: "))
if a==b and b==c and a==c:
    print("equilateral")
elif a==b or a==c or b==c:
    print("isosceles")
else:
    print("scalene")