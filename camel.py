name = input("Type the name here")
name = list(name)

for i in range(len(name)):
    if name[i].islower():
        print(name[i],end="") 
        continue
    else:
        name[i] = name[i].lower()
        print("_",name[i],end="",sep="") 
print() 
