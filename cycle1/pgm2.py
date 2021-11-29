n = int(input("enter the number"))
f1 = 0
f2 = 1
if (n < 1):
   print(f1)
for x in range(1,n):
    print(f2)
    f3 = f1 + f2
    f1 = f2
    f2 = f3
