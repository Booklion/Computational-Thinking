'''
Created on 15 Nov 2023

@author: Big Lion
'''
from domain import Dog
from domain import Cat

class Person():
    '''
        An object from the class Person has as attributes:
        - name (string): the name of the person
        - surname (string): the surname of the person
        - adoptedAnimals (list): the list of all the animals adopted by this person (added by ID)
        - isAdmin (bool): checks if the person is a regular user or an admin
    '''


    def __init__(self, ID: int, name: str, surname: str, adoptedAnimals: list, isAdmin: bool):
        '''
        Constructor
        '''
        self.__id = ID
        self.__name = name 
        self.__surname = surname 
        self.__adoptedAnimals = adoptedAnimals
        self.__isAdmin = isAdmin
        
    def getID(self):
        """
            Getter for the ID of the person.
        """
        return self.__id

    def setID(self, newID: str):
        """
            Setter for the ID of the person.
        """
        self.__id = newID

    def getName(self):
        """
            Getter for the name of the person.
        """
        return self.__name

    def setName(self, newName: str):
        """
            Setter for the name of the person.
        """
        self.__name = newName

    def getSurname(self):
        """
            Getter for the surname of the person.
        """
        return self.__surname

    def setSurname(self, newSurname: str):
        """
            Setter for the surname of the person.
        """
        self.__surname = newSurname

    def getAdoptedAnimals(self):
        """
            Getter for the list of animals the person has adopted.
        """
        return self.__adoptedAnimals
    
    def setAdoptedAnimals(self, newAdoptedAnimals: list):
        """
            Setter for the list of all the animals the person has.
        """
        self.__adoptedAnimals = newAdoptedAnimals

    def getIsAdmin(self):
        """
            Getter for the status of the person (admin or regular user).
        """
        return self.__isAdmin

    def setIsAdmin(self, newStatus: bool):
        """
            Setter for the status of the person (admin - 0 or regular user - 1).
        """
        self.__isAdmin = newStatus

    def adoptCat(self, newCat: Cat):
        self.__adoptedAnimals.append(newCat)
        
    def adoptDog(self, newDog: Dog):
        self.__adoptedAnimals.append(newDog)
    
        