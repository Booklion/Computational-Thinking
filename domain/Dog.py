'''
Created on 13 Nov 2023

@author: Big Lion
'''
from domain.Animal import Animal
class Dog(Animal):
    '''
        Class Dog is derived from base class Animal and inherits all the attributes and methods of parent class
        Extra attributes:
        race (str): the race of the dog
        dogFood (str): the preferred food of the dog
    '''

    def __init__(self, ID: int, name: str, age: int, timeInShelter: int, adopted: bool, race: str, dogFood: str):
        '''
        Constructor
        '''
        super().__init__(ID, name, age, timeInShelter, adopted)
        self.__race = race
        self.__dogFood = dogFood

    def getRace(self):
        return self.__race

    def setRace(self, newRace):
        self.__race = newRace

    def getDogFood(self):
        return self.__dogFood

    def setDogFood(self, newDogFood):
        self.__dogFood = newDogFood
        
    def __str__(self):
        return Animal.__str__(self) + "\n" + "Race: " + self.__race + "\n" + "Preferred Dog Food Brand: " + self.__dogFood + "\n"



    

        
        