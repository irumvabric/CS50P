# def main():
#     print_column(3)

# def print_column(height):
#     print("# \n" * height,end="")  

# def print_column(height):
#     print("# \n" * height,end="")  


# ---------------------------------
# def main():
#     print_row(3)

# def print_row(width):
#     print("??" * width)  

# ---------------------------------

def main():
    print_square(3)

def print_square(size):

    #For each row in square 
    for i in range(size):

        #For each brick in row
        for j in range(size):

            #Print brick
            print("#",end="")
        print()

main()