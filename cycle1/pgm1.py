first = int(input("enter lower range"))
last = int(input("enter the last number"))

for n in range(first,last+1):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                print(n)
                break
