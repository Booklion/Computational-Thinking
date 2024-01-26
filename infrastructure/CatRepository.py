'''
Created on 13 Nov 2023

@author: Big Lion
'''
from domain.Animal import Animal
from infrastructure.SingletonMeta import SingletonMeta
from domain.Gender import Gender

class CatRepository(metaclass=SingletonMeta):
    '''
        The repository of all the cats in the shelter.
    '''
    _repo = []

    def add(self, new_cat: Animal):
        '''
            Add a cat to the repository
            param newCat (Cat): the new cat in the shelter
        '''
        self._repo.append(new_cat)

        return new_cat
    
    def get(self, filters = {}, sort_criteria = {}):
        filtered_repo = self._repo
        if not filters['gender'] is None:
            filtered_repo = [cat for cat in filtered_repo if cat.gender == int(filters['gender'])]
        if len(filters['special_needs']) > 0:
            filtered_repo = [cat for cat in filtered_repo if len(set(cat.special_needs).intersection(filters['special_needs'])) > 0]
        if sort_criteria['birth_year'] in ['ASC', 'DESC']:
            filtered_repo.sort(key=lambda x: x.birth_year, reverse=sort_criteria['birth_year'] == 'DESC')

        return filtered_repo
    
    def get_by_id(self, id: str):
        return next(cat for cat in self._repo if cat.id == str(id))
    
    def update(self, id: str, updated_cat):
        self.remove(id)
        updated_cat.id = id
        self.add(updated_cat)
        return updated_cat

    def remove(self, id: str):
        removed_cat = self.get_by_id(id)
        self._repo = [cat for cat in self._repo if cat.id != id]
        return removed_cat