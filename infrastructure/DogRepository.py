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
        if len(self.__repo) == 0:
            print("The dog repository is empty!")
        else:
            foundID = 0
            for elem in self.__repo:
                if elem.getID() == ID:
                    foundID = 1
                    self.__repo.remove(elem)
                    print("Dog removed successfully!")
            
            if foundID == 0:
                print("No dog with this ID found!")
                    
    
    def updateDog(self, ID):
        '''
            Update the information about a Dog identified by its ID.
        '''
        foundID = 0
        for elem in self.__repo:
            if elem.getID() == ID:
                foundID = 1
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
                     
        if foundID == 0:
            print("No dog with this ID found!")
                
    def showAll(self):
        if len(self.__repo) == 0:
            print("The dog repository is empty!")
        else:    
            for elem in self.__repo:
                print(elem.__str__() + "\n")
                    
    def filterByAdoptionStatus(self):
        """
            Filter the dogs in the repository of dogs by their adoption status.
        """
        print("What adoption status should the dog have? Select one:\n")
        print("1 - adopted \n")
        print("2 - not adopted \n")
        option = int(input("Your option: \n"))
        
        if option == 1:
            for elem in self.__repo:
                if elem.getAdoptionStatus() == True:
                    print(elem)
        elif option == 2:
            filteredList = list(filter(lambda x: x.getAdoptionStatus() == False, self.__repo))
            if len(filteredList) == 0:
                print("There are no unadopted dogs!")
            else:
                [print(elem) for elem in filteredList]
                    
        else:
            print("This input is invalid!")
    
    def sortByAge(self, criterion: bool):
        """
            Sort the repository by the ages of the dogs, by a certain criterion (ascending - True, descending - False)
        """
        if criterion == True:
            sortedRepo = sorted(self.__repo, key=lambda x: x.getAge())
            for elem in sortedRepo:
                print(elem)
        else:
            sortedRepo = sorted(self.__repo, key=lambda x: x.getAge(), reverse = True)
            for elem in sortedRepo:
                print(elem)
    
    def sortByTimeInShelter(self, criterion: bool):
        """
            Sort the repository by the time the dogs spent in shelter, by a certain criterion (ascending - True, descending - False)
        """
        if criterion == True:
            sortedRepo = sorted(self.__repo, key=lambda x: x.getTimeInShelter())
            for elem in sortedRepo:
                print(elem)
        else:
            sortedRepo = sorted(self.__repo, key=lambda x: x.getTimeInShelter(), reverse = True)
            for elem in sortedRepo:
                print(elem)
                
    def sortByID(self, criterion: bool):
        """
            Sort by the dog's ID in ascending order (criterion = True) or descending order (criterion = False)
        """
        if criterion == True:
            sortedRepo = sorted(self.__repo, key=lambda x: x.getID())
            for elem in sortedRepo:
                print(elem)
        else:
            sortedRepo = sorted(self.__repo, key=lambda x: x.getID(), reverse = True)
            for elem in sortedRepo:
                print(elem)
            