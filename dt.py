
from dataclasses import dataclass
class A:
    def __init__(self):
        self.message = "Jestem A"

@dataclass
class A:
     message: str = "A ja nie"


a = A()

# to jaki będzie message?

print(a.message)

