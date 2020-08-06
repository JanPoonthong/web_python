people = [
    {"name": "Jan", "house": "Lamai"},
    {"name": "John", "house": "LA"},
    {"name": "Devon", "house": "Canada"}
]

#def f(person):
    #print(person)
    #return person["name"]


people.sort(key=lambda person: person["name"])
print(people)
