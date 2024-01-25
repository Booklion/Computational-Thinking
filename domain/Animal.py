from domain.Gender import Gender

class Animal(object):
    """
        An element of the class Animal has the following attributes:
        - name: the name of the animal
        - birth_year: the birth year of the animal
        - joined_shelter_ts: UNIX timestamp representation of the datetime when the animal joined the shelter
        - adopted: the adoption status of the animal
    """
    def __init__(self,
            id: int,
            name: str,
            birth_year: int,
            joined_shelter_ts: int,
            adopted: bool,
            description: str,
            image: str,
            special_needs: [str],
            gender: Gender):
        """
            Constructor
        """
        self._id = id 
        self.name = name
        self.birth_year = birth_year
        self.joined_shelter_ts = joined_shelter_ts
        self.adopted = adopted
        self.description = description
        self.image = image
        self.special_needs = special_needs
        self.gender = gender

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def birth_year(self):
        return self._birth_year
    
    @birth_year.setter
    def birth_year(self, value):
        self._birth_year = value

    @property
    def joined_shelter_ts(self):
        return self._joined_shelter_ts
    
    @joined_shelter_ts.setter
    def joined_shelter_ts(self, value):
        self._joined_shelter_ts = value

    @property
    def adopted(self):
        return self._adopted
    
    @adopted.setter
    def adopted(self, value):
        self._adopted = value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value
    
    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, value):
        self._image = value

    @property
    def special_needs(self):
        return self._special_needs
    
    @special_needs.setter
    def special_needs(self, value):
        self._special_needs = value
    
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, value):
        self._gender = value
    
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
            "gender": self.gender
        }
    
    def from_json(json):
        return Animal(
            json['id'],
            json['name'],
            json['birth_year'],
            json['joined_shelter_ts'],
            json['adopted'],
            json['description'],
            json['image'],
            json['special_needs'],
            json['gender']
        )