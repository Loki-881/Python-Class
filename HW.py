names= ("Goku","Sukuna","Sunraku","Loki","Naruto")
for name in names:
    if len(name)<5:
        print(name)
        
#Print the first ten even numbers using a while loop.

count=0
num=2
while count<10:
    print(num)
    num+=2
    count+=1


#Ask the user to enter numbers continuously until they type 0. Then print the sum

total=0

while True:
    num= int(input("Enter a number(0 to stop):"))
    if num==0:
        break
    total=total+num
print("The sum of total number is:",total)



#********
for i in range(1,4):
    for j in range(1,i+1):
        print("*",end=" ")
    print()        