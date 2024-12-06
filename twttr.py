def main():
    word = input("Type the word here")
    word = list(word)

    for i in range(len(word)):
        if isAVowel(word[i]):
            print("",end="")
            continue
        else:
            # word[i] = word[i].lower()
            print(word[i],end="",sep="")
    print()

def isAVowel(character):
    vowel = ['a','e','i','o','u','U','O','I','E','A']

    for i in range(len(vowel)):
        if character == vowel[i]:
            return True


main()
