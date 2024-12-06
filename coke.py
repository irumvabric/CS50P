amount = 50
change_owe = 0

while amount > 0:
    print("Amount Due:",amount)
    Coin = int(input("Insert Coin: "))
    amount = amount - Coin

    if amount < 0:
        change_owe = - amount
        break
    elif amount > 0:
        continue


print("Change Owed:",change_owe)  



