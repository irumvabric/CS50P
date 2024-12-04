# for i in range(4):
#     n = n  3
#     print(i)

# i = 0
# while i < 3 :
#     print("meow")
#     i += 1

# for _ in range(6):
#     print("meow")


# while True:
#     n = int(input("what's n?"))
#     if n > 0:
#         break
    

# for _ in range(n):
#     print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            return n
        
def meow(n):
    for _ in range(n):
        print("meow")  

main()