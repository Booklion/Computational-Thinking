'''
Created on 11 Dec 2023

@author: Big Lion
'''
from domain import Person
from domain import Cat
from domain import Dog

class Person(Person):
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
                print("What information would you like to update? Select: \n")
                print("1 - name \n")
                print("2 - surname \n")
                print("3 - status \n")
                print("0 - exit \n")
                
                option = int(input("Your option: "))
                while option != 0:
                    if option == 1:
                        newName = str(input("Enter new name: "))
                        elem.setName(newName)
                        option = int(input("Your option: "))
                        
                    elif option == 2:
                        newSurname = int(input("Enter the new surname: "))
                        elem.setSurnme(newSurname)
                        option = int(input("Your option: ")) 
                    
                    elif option == 3:
                        newStatus = bool(input("Enter the new status: "))
                        elem.setIsAdmin(newStatus)
                        option = int(input("Your option: "))
                        
                    else:
                        print("The option is invalid!")
                        break
                if option == 0:
                    print("Thank you for your update!") 
                     
        if foundID == 0:
            print("No Person with this ID found!")
                
    def showAll(self):
        if len(self.__repo) == 0:
            print("The Person repository is empty!")
        else:    
            for elem in self.__repo:
                print(elem.__str__() + "\n")
            