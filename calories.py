nutritions = [
    {"name" : "apple" ,"calories": 130},
    {"name" : "Avocado" ,"calories": 50},
    {"name" : "banana" ,"calories": 110},
    {"name" : "Sweet Cherries" ,"calories": 100},
    {"name" : "Kiwifruit" ,"calories": 90},
    {"name" : "pear" ,"calories": 100},
]

name = input("Item:")

for nutrition in nutritions:
    if name == nutrition["name"]:
        print("Calories : ",nutrition["calories"])
