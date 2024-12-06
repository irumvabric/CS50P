def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# “All vanity plates must start with at least two letters.” ok
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) ok and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate;
# AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”


def is_valid(s):
    # Split all the string in a list
    s = list(s)

    # Check if the length string is formed of 6 char
    if 2<= len(s) <= 6:
        # Check if the 1st char and the 2 nd char are not num
        if s[0].isnumeric() and s[1].isnumeric():
            return False
        else:
            for i in range(len(s)):
                if containsPonctuation(s[i]):
                    return False
                # Figure out how to get this not numeric
                # elif s[len(s) - 1].isnumeric():
                else:
                    return True
    else:
        return False

def isANumber(num):
    number = [1,2,3,4,5,6,7,8,9]

    for i in range(len(number)):
        if num == number[i]:
            return True

def containsPonctuation(char):
    ponctuation = ['.','?',':',',','!',]

    for i in range(len(ponctuation)):
        if char == ponctuation[i]:
            return True

main()
