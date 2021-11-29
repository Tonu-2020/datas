from math import sqrt

print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b ** 2 - 4 * a * c

if r > 0:

    x1 = (((-b) + sqrt(r)) / (2 * a))
    x2 = (((-b) - sqrt(r)) / (2 * a))
    print("first root ",round(x1,2))
    print("second root ", round(x2, 2))
elif r == 0:

    x = (-b) / 2 * a
    print("There is one root: ", x)
else:

    print("No roots, discriminant < 0.")
    exit()
