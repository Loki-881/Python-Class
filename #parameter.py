#parameter
def college(name):
    print(name + "college")
    
college("NCMT")
college("LINCOLN")

#sum of 2 numbers
def add(x,y):
    sum = x+y
    print("the sum is ",sum)

add(9,11)

#k ho k ho
def person(*gamer):
    print("The best gamer is " + gamer[0])
    
person("Faker","Zeus","Tenz","Envy")

#keyword argument
def add(x,y,z):
    x=1
    y=11
    z=111
    sum = z+x+y
    print("the sum is ",sum)
    
add(1,11,111)

#** argument
def person(**gamer):
    print("The best gamer is " + gamer[])
    
person("Faker","Zeus","Tenz","Envy")

#default argument
def Country(country):
    for x in country:
        print(x)

countries = ["Japan","South Korea","China"]

Country(countries)


