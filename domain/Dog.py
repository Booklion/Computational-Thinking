from domain.Animal import Animal
from domain.Gender import Gender

class Dog(Animal):
    def __init__(
        self,
        id: int,
        name: str,
        birth_year: int,
        joined_shelter_ts: int,
        adopted: bool,
        description: str,
        image: str,
        special_needs: [str],
        gender: Gender,
        size: int
    ):
        super().__init__(id, name, birth_year, joined_shelter_ts, adopted, description, image, special_needs, gender)
        self.size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        self._size = value