people = [
    {"name": "Jan", "house": "Lamai"},
    {"name": "John", "house": "LA"},
    {"name": "Devon", "house": "Canada"}
]

def f(person):
    return person["name"]
    print(f)


people.sort(key=f)
print(people)
