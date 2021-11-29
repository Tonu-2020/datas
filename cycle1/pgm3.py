x = int(input("enter first side"))
y = int(input("enter second side"))
z = int(input("enter thrid side"))
if x == y == z:
    print("Equilateral Triangle")


elif x == y or y == z or z == x:
    print("Isosceles Triangle")


else:
    print("Scalene Triangle")
