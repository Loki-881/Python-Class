# list is a collection of items , written in square bracket []
# items are ordered changable and allow duplicate value
#index starts from 0 and (-1 refers to the last item)
#can contain any data type
#can be used in loop
#cant be used as data type


#Tuple is ordered and unchangable .alows duplicate ()

#set is unordered unchangable and unindexed no duplicamates {}
#dictioanry is ordered and changable no duplicates



fruits=["apple","mango","strawberry","peach","orange","kiwi","lemon"]
"""
print(fruits[2:5])

print(fruits[:4])
print(fruits[2:1])
print(fruits[-4:-1])

"""
#List operations

fruits.remove("mango")
print(fruits)

fruits.append("apple")
print(fruits)

fruits.insert(2,"peach")
print(fruits)

print(fruits[5])

print(len(fruits))

fruits.sort()
print(fruits)

newlists=["grapes","guava","blackberry"]
fruits.extend(newlists)
print(fruits)

copylists=fruits.copy()
print(fruits)