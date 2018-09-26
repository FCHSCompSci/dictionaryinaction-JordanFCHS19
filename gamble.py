import sys

adopt_dog = {
    'name':"name",
    'age':"age",
    'dogs_owned':"dogs_owned",
    'children':"children",
    }

def adoption(name,age,dogs_owned,children):
    buyer = {
        'name':name,
        'age':age,
        'dogs_owned':dogs_owned,
        'children':children,
        
        }
    
    return buyer

    for buyer, price in buyer.items():
        print("%s: %s" % (buyer,price))

def dog(name,age,sex,breed):
    doggo = {
        'name':name,
        'age':age,
        'sex':sex,
        'breed':breed,
        }
    return doggo

       
'''
buyer_one = adoption("Bob", 28, 3, False, "House")
buyer_two = adoption("Joe", 17, 0, True, "Mansion down by the river")
'''
adopt = input("Would you like to adopt a pupper? yes or no - ")
if adopt == 'yes':
    print("Great!")
else:
    print("oof")
    sys.exit()
    
name = input("What is your name?")
age = input("What is your age?")

dogs_owned = input("How many dogs do you own?")
children = input("How many children do you own?")
    
print("Here are the dogs that are currently avaliable for adoption.")

dogs = {
"Buster": dog("Buster",5,"M","Choc Lab"),
"Skylar": dog("Skylar",2,"F","Beagle"),
'CoCo': dog("CoCo",9,"F","Lab"),
'Bella': dog("Bella",1,"F","Boxador"),
'Scout': dog("Scout",5,"M","Pitbull"),
}

print("\n")
for i in dogs:
    print(i, dogs[i])
print("\n")

sucess = input("See any dogs you'd like to adopt? yes or no - ")
if sucess == 'yes':
    print("Thats great! Please")
    o = input("which dog ")
    if o in dogs:
        print(dogs[o])
    confirmation = input("This dog comes at a cost of $100 for rehoming fees, are you sure you'd like to purchase? yes or no- ")
    if confirmation == 'yes':
        print("Perfect! Congrats on your new companion!")
        print("Have a nice day and thanks for adopting!")
    else:
        print("We're very sorry we couldn't help you today.")
        sys.exit()
        
    
else:
    request = input("Would you like to fill out a request form? yes or no - ")
    if request == 'yes':
        dog_age = input("Would you like a puppy,young,adult,or senior dog?")
        dog_sex = input("Would you like a male or female dog")
        dog_breed = input("What breed of dog would you like?")
        print(f"   ---  Request form:  DOG AGE- {dog_age}, DOG SEX- {dog_sex}, DOG BREED- {dog_breed}.   ---")
        print("We'll let you know if we find any dogs in need of a home that meet that description.")
        
    else:
        print("Sorry we couldn't help you today, good luck on finding the right dog for you!")
        sys.exit()
