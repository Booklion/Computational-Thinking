from uuid import uuid4

from domain.Animal import Animal
from domain.Gender import Gender

class Dog(Animal):
    def __init__(
        self,
        name: str,
        birth_year: int,
        joined_shelter_ts: int,
        adopted: bool,
        description: str,
        image: str,
        special_needs: [str],
        gender: Gender,
        size: int,
        id: str = uuid4(),
    ):
        super().__init__(name, birth_year, joined_shelter_ts, adopted, description, image, special_needs, gender, id)
        self.size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        self._size = value

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "joined_shelter_ts": self.joined_shelter_ts,
            "adopted": self.adopted,
            "description": self.description,
            "image": self.image,
            "special_needs": self.special_needs,
            "gender": self.gender,
            "size": self.size
        }
    
    def from_json(json):
        return Dog(
            json['name'],
            json['birth_year'],
            json['joined_shelter_ts'],
            json['adopted'],
            json['description'],
            json['image'],
            json['special_needs'],
            json['gender'],
            json['size']
        )