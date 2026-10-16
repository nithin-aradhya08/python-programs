a=int(input("enter first angle:"))
b=int(input("enter second angle:"))
c=int(input("enter third angle:"))

if a==b and b==c and c==a:
    print("equialateral tringle")
elif a==b or b==c or c==a:
    print("isosceles tringle")
else:
    print("scalene tringle2")