from domain.Animal import Animal
from domain.Gender import Gender

class Cat(Animal):
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
        gender: Gender
    ):
        super().__init__(id, name, birth_year, joined_shelter_ts, adopted, description, image, special_needs, gender)