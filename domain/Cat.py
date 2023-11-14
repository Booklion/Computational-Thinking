'''
Created on 13 Nov 2023

@author: Big Lion
'''
from domain.Animal import Animal


class Cat(Animal):
    '''
         Class Cat is derived from class Animal and has all the attributes and methods that the parent class has
         Extra attribute:
         catFood (string): the brand of food the cat prefers 
    '''

    def __init__(self, ID: int, name: str, age: int, timeInShelter: int, adopted: bool, catFood: str, photo: str):
        '''
        Constructor
        '''
        super().__init__(ID, name, age, timeInShelter, adopted)
        self.__catFood = catFood
        self.__photo = photo

    def getCatFood(self):
        return self.__catFood

    def setCatFood(self, newCatFood):
        self.__catFood = newCatFood

    def __str__(self):
        return Animal.__str__(self) + "\n" + "Preferred Cat Food Brand: " + self.__catFood + "\n"
