a = int(input("enter the number"))
sum =0
for i in range (1,a):
    if (a%i==0):
        sum = sum + i
if (sum == a):
    print(" number is a perfect square")
else:
    print(" number is not perfect square")

    