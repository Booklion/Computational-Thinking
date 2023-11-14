from domain.Animal import Animal
from domain.Cat import Cat
from domain.Dog import Dog
from infrastructure.CatRepository import CatRepository
from infrastructure.DogRepository import DogRepository

if __name__=='__main__':
    cat1 = Cat(1, "Blue", 3, 12, True, "Aro")
    cat2 = Cat(2, "Dori", 2, 12, True, "Aro")
    dog1 = Dog(3, "Max", 14, 2, False, "Maidanez", "Anything and everything")
    dog2 = Dog(4, "Rex", 5, 7, True, "Poodle", "idk dog foods")
    
    # Test CatRepository:
    print("TESTING: CAT REPOSITORY\n")
    print("Test: add and show list of cats: \n")
    catRepo = CatRepository()
    catRepo.addCat(cat1)
    catRepo.showAll()
    
    print("Test: remove cat and show empty list: \n")
    catRepo.removeCat(1)
    catRepo.showAll()
    
    print("Test: update cat: \n")
    catRepo.addCat(cat2)
    catRepo.addCat(cat1)
    catRepo.showAll()
    
    #catRepo.updateCat(2)
    #catRepo.showAll()
    
    print("Test: filter cats by adoption status")
    #catRepo.filterByAdoptionStatus()
    
    print("Test: sort cats by age - ascending")
    catRepo.sortByAge(True)
    
    print("Test: sort cats by age - descending")
    catRepo.sortByAge(False)
    
    print("Test: sort cats by time in shelter - ascending")
    catRepo.sortByTimeInShelter(True)
    
    print("Test: sort cats by time in shelter - descending")
    catRepo.sortByTimeInShelter(False)
    
    print("Test: sort cats by ID - ascending")
    catRepo.sortByID(True)
    
    print("Test: sort cats by ID - descending")
    catRepo.sortByID(False)
    
    # Test DogRepository:
    print("TESTING: DOG REPOSITORY\n")
    print("Test: add and show list of dogs: \n")
    dogRepo = DogRepository()
    dogRepo.addDog(dog1)
    dogRepo.showAll()
    
    print("Test: remove dog and show empty list: \n")
    dogRepo.removeDog(3)
    dogRepo.showAll()
        
    print("Test: update dog: \n")
    dogRepo.addDog(dog2)
    dogRepo.addDog(dog1)
    dogRepo.showAll()
    
    #dogRepo.updateDog(3)
    #dogRepo.showAll()
    
    
    #print("Test: filter dogs by adoption status")
    #dogRepo.filterByAdoptionStatus()
    
    """
    print("Test: sort dogs by age - ascending")
    dogRepo.sortByAge(True)
    
    print("Test: sort dogs by age - descending")
    dogRepo.sortByAge(False)
    
    print("Test: sort dogs by time in shelter - ascending")
    dogRepo.sortByTimeInShelter(True)
    
    print("Test: sort dogs by time in shelter - descending")
    dogRepo.sortByTimeInShelter(False)
    
    print("Test: sort dogs by ID - ascending")
    dogRepo.sortByID(True)
    
    print("Test: sort dogs by ID - descending")
    dogRepo.sortByID(False)
    """
    
    
    
    
    
    
    
    