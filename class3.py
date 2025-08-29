user_input=[]
for i in range(1,6):
 names=input("Enter names:")
 user_input.append(names)
 ah=list(set(user_input))
print(ah)
print(f"SET is {user_input}")
user_input.reverse()
print(f"reverse is {user_input}")
