lst = []

p = int(input("Enter size of phonenumber : "))
print("enter the phonenumber")

for i in range(0, p):
    ele = int(input())
 
    lst.append(ele)
    
def absent_digits(lst):
  all_nums = set([0,1,2,3,4,5,6,7,8,9])
  lst = set([int(i) for i in lst])
  lst = lst.symmetric_difference(all_nums)
  lst = sorted(lst)
  return lst
print("missing number")
print(absent_digits(lst))
