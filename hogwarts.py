# students = ["Hermione", "Harry", "Ron","Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor","Slytherin"]

# students = {
#     "Hermione" : "Gryffindor",
#     "Harry" : "Gryffindor",
#     "Ron" : "Gryffindor",
#     "Draco" : "Slytherin",
# }

students = [
    {
    "name" : "Hermione",
    "house" : "Gryffindor",
    "patronus" : "Gryffindor",
    "Draco" : "Slytherin",
    },
    {
    "name" : "Hermione",
    "house" : "Gryffindor",
    "patronus" : "Gryffindor",
    "Draco" : "Slytherin",
    },
    {
    "name" : "Hermione",
    "house" : "Gryffindor",
    "patronus" : "Gryffindor",
    "Draco" : "Slytherin",
    },
    {
    "name" : "Hermione",
    "house" : "Gryffindor",
    "patronus" : "Gryffindor",
    "Draco" : "Slytherin",
    }
]



# for studebnt in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

for student in students:
    print(student["name"],student["house"],student["patronus"],sep=", ")
