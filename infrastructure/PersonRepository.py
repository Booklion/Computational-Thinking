'''
Created on 11 Dec 2023

@author: Big Lion
'''
from domain import Person

class PersonRepository(Person):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__repo = []
        
    def addPerson(self, newPerson: Person):
        '''
            Add a Person to the repository
            param newPerson (Person): the new Person in the shelter
        '''
        self.__repo.append(newPerson)
        
    def removePerson(self, ID):
        '''
            Remove a Person from the repository by ID
        '''
        if len(self.__repo) == 0:
            print("The Person repository is empty!")
        else:
            foundID = 0
            for elem in self.__repo:
                if elem.getID() == ID:
                    foundID = 1
                    self.__repo.remove(elem)
                    print("Person removed successfully!")
            
            if foundID == 0:
                print("No Person with this ID found!")
                    
    
    def updatePerson(self, ID):
        '''
            Update the information about a Person identified by their ID.
        '''
        foundID = 0
        for elem in self.__repo:
            if elem.getID() == ID:
                foundID = 1
                elem.setName(newName)
                elem.setSurnme(newSurname)
                elem.setIsAdmin(newStatus)
                     
        if foundID == 0:
            print("No Person with this ID found!")
                
    def showAll(self):
        if len(self.__repo) == 0:
            print("The Person repository is empty!")
        else:    
            for elem in self.__repo:
                print(elem.__str__() + "\n")
            