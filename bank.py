greeting = input("Greeting :")

greeting = greeting.lower()

if(greeting.startswith("h") or greeting.__contains__("hello")):
    if(greeting.__contains__("hello")):
        print("$0")
    else:
        print("$20")
else:
    print("$100")
    