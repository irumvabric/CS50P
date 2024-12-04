name = input("What is the Answer to the Great Question of Life, the Universe, and Everything? \n")

name = name.lower()

match name:
    case "42" |"forty-two":
       print("Yes")
    case _:
        print ("No")