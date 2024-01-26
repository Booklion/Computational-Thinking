'''
Created on 13 Nov 2023

@author: Big Lion
'''
from domain.Dog import Dog
from infrastructure.SingletonMeta import SingletonMeta

class DogRepository(metaclass=SingletonMeta):
    '''
        The repository of all the dogs in the shelter.
    '''
    _repo = []

    def add(self, new_dog: Dog):
        self._repo.append(new_dog)

        return new_dog
    
    def get(self, filters = {}):
        filtered_repo = self._repo
        if not filters['gender'] is None:
            filtered_repo = [cat for cat in filtered_repo if cat.gender == int(filters['gender'])]
        if len(filters['special_needs']) > 0:
            filtered_repo = [cat for cat in filtered_repo if len(set(cat.special_needs).intersection(filters['special_needs'])) > 0]

        return filtered_repo
    
    def get_by_id(self, id: int):
        return next(dog for dog in self._repo if dog.id == id)
    
    def update(self, id: int, updated_dog):
        self.remove(id)
        updated_dog.id = id
        self.add(updated_dog)
        return updated_dog

    def remove(self, id: int):
        removed_dog = self.get_by_id(id)
        self._repo = [dog for dog in self._repo if dog.id != id]
        return removed_dog