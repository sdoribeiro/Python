
# define a dictionary inside a list.
people = [
    {"name":"Sandro", "house": "Gryffindor"},
    {"name":"Felipe", "house": "Ravenclaw"},
    {"name":"Rafael", "house": "Slytherin"},
    
]

def f(person):
    return person["name"]
    # return person["house"]

# using a function
people.sort(key=f)
print(people)

# usigng lambda
people.sort(key=lambda person: person["house"])
print(people)