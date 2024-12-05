name = input("What is the Answer to the Great Question of Life, the Universe, and Everything? \n")

name = name.lower()

if name.__contains__("42") or name == "forty-two" or name == "forty two":
    print("Yes")
else:
    print("No")
