def main():
    expression = input("What time is it: ")

    # time,o = expression.split(" ")

    time = convert(expression)


    if 7<= time <=8:
        print("breakfast time")
    elif 12<= time <13 or 1<= time <2:
        print("lunch time")
    elif 18<= time <20:
        print("dinner time")

    

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    minutes = float(minutes/60)
    convertedTime = hours + minutes
    return convertedTime

if __name__ == "__main__":
    main()


# Todo i you have time to think about it

# def main():
#     expression = input("What time is it: ")

#     time,o = expression.split(" ")

#     time = convert(time)

#     if 7<= time <=8:
#         if o == "a.m.":
#             print("breakfast time")
#         elif o == "":
#             print("breakfast time")
#     elif 12<= time < 1:
#         if o == "p.m.":
#             print("lunch time")
#         elif o == "":
#             print("lunch time")
#     elif 1<= time < 2:
#         if o == "p.m.":
#             print("lunch time")
#         elif o == "":
#             print("lunch time")
#     elif 7<= time <=8:
#         if o == "a.m.":
#             print("breakfast time")
#         elif o == "":
#             print("breakfast time")

    

# def convert(time):
#     hours, minutes = time.split(":")
#     minutes = (minutes/60)
#     convertedTime = float(f"{hours}.{minutes}")
#     return convertedTime

# def convertEngl(time):
#     hours, minutes = time.split(":")
#     minutes = (minutes/60)
#     convertedTime = float(f"{hours}.{minutes}")
#     return convertedTime


# if __name__ == "__main__":
#     main()