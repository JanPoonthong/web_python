people = [
    {"name": "Jan", "house": "Lamai"},
    {"name": "John", "house": "LA"},
    {"name": "Devon", "house": "Canada"}
]


# def f(person):
#     return person["house"]


people.sort(key=lambda person: person["name"])
print(people)
