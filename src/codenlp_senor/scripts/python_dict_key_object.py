from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str

    def __repr__(self):
        return f"<Person({self.first_name},{self.last_name})"

    def __hash__(self):
        return hash((self.first_name, self.last_name))

    def __eq__(self, p):
        if isinstance(p, Person):
            return self.first_name == p.first_name \
                and self.last_name == p.last_name
        return NotImplemented


if __name__ == '__main__':
    p1 = Person("John", "Smith")
    p2 = Person("John", "Smith")
    p3 = Person("Paul", "Smith")

    people = {p1: p1.first_name, p2: p2.first_name, p3: p3.first_name}
    print(people)

    # {<Person(John,Smith): 'John', <Person(Paul,Smith): 'Paul'}
