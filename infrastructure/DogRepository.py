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
    
    def get(self, filters = {}, sort_criteria = {}):
        filtered_repo = self._repo
        if not filters['gender'] is None:
            filtered_repo = [dog for dog in filtered_repo if dog.gender == int(filters['gender'])]
        if len(filters['special_needs']) > 0:
            filtered_repo = [dog for dog in filtered_repo if len(set(dog.special_needs).intersection(filters['special_needs'])) > 0]
        if not filters['min_size'] is None:
            filtered_repo = [dog for dog in filtered_repo if dog.size >= int(filters['min_size'])]
        if not filters['max_size'] is None:
            filtered_repo = [dog for dog in filtered_repo if dog.size <= int(filters['max_size'])]
        if sort_criteria['birth_year'] in ['ASC', 'DESC']:
            filtered_repo.sort(key=lambda x: x.birth_year, reverse=sort_criteria['birth_year'] == 'DESC')

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