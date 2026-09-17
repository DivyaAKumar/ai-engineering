from typing import TypedDict

class Person(TypedDict):
    name: str
    age : int

new_person: Person = {
    'name': 'Divya',
    'age': 21 #wont throw an error even if age : '21'
}
print(new_person)