'''
Created on 13 Nov 2023

@author: Big Lion
'''
from domain.Dog import Dog

class DogRepository(Dog):
    '''
        The repository of all the dogs in the shelter.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__repo = []
    
        
    # Operation for Dogs:
    
    def addDog(self, newDog: Dog):
        '''
            Add a Dog to the repository
            param newDog (Dog): the new dog in the shelter
        '''
        self.__repo.append(newDog)
        
    def removeDog(self, ID):
        '''
            Remove a Dog from the repository by ID
        '''
        for elem in self.__repo:
            if elem.getID() == ID:
                self.__repo.remove(elem)
        print("Dog removed successfully!")
        if len(self.__repo) == 0:
            print("The dog repository is empty!")
    
    def updateDog(self, ID):
        '''
            Update the information about a Dog identified by its ID.
        '''
        for elem in self.__repo:
            if elem.getID() == ID:
                print("What information would you like to update? Select: \n")
                print("1 - name \n")
                print("2 - age \n")
                print("3 - time in shelter")
                print("4 - race")
                print("5 - preferred food \n")
                print("6 - adoption status \n")
                print("0 - exit \n")
                
                option = int(input("Your option: "))
                while option != 0:
                    if option == 1:
                        newName = str(input("Enter name: "))
                        elem.setName(newName)
                        option = int(input("Your option: "))
                        
                    elif option == 2:
                        newAge = int(input("Enter the new age: "))
                        elem.setAge(newAge)
                        option = int(input("Your option: "))
                        
                    elif option == 3:
                        newTimeInShelter = int(input("Enter the new time in shelter (in months): "))
                        elem.setTimeInShelter(newTimeInShelter)
                        option = int(input("Your option: "))
                        
                    elif option == 4:
                        newRace = str(input("Enter the new race: "))
                        elem.setRace(newRace)
                        option = int(input("Your option: "))
                        
                    elif option == 5:
                        newDogFood = str(input("Enter the new preferred Dog food: "))
                        elem.setDogFood(newDogFood)
                        option = int(input("Your option: "))
                    
                    elif option == 6:
                        newStatus = bool(input("Enter the new status: "))
                        elem.setAdoptionStatus(newStatus)
                        option = int(input("Your option: "))
                        
                    else:
                        print("The option is invalid!")
                        break
                if option == 0:
                    print("Thank you for your update!")  
        
    def showAll(self):
        if len(self.__repo) == 0:
            print("The dog repository is empty!")
        else:    
            for elem in self.__repo:
                print(elem.__str__() + "\n")
                    
    def filterByAdoptionStatus(self):
        # TO-DO
        pass
    
    def sortByAge(self, criteria: bool):
        # TO-DO
        pass
    
    def sortByTimeInShelter(self, criteria: bool):
        # TO-DO
        pass
            