numbers=[]
for i in range(1,6):
 num=int(input("Enter 5 nums:"))
 numbers.append(num)
print(f"List is {numbers}")

num_set = set(numbers)


if 10 in num_set:
    print("The number 10 is in the set.")
else:
    print("The number 10 is NOT in the set.")