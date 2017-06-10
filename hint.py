from typing import Text, NamedTuple


class Employee(NamedTuple):
    id: int
    name: Text


class Manager:
    def __init__(self, emp: Employee) -> None:
        self._emp = emp

    def greeting(self) -> Text:
        return self._emp.name


employee: Employee = Employee(name='Guido', id=5)
m: Manager = Manager(employee)

print(m.greeting())
