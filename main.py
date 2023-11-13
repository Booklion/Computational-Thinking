from domain.Animal import Animal
from domain.Cat import Cat
from domain.Dog import Dog
from infrastructure.CatRepository import CatRepository

if __name__=='__main__':
    cat1 = Cat(1, "Blue", 3, 12, True, "Aro")
    cat2 = Cat(2, "Dori", 3, 12, True, "Aro")
    dog1 = Dog(3, "Max", 14, 2, False, "Maidanez", "Anything and everything")
    dog2 = Dog(4, "Rex", 5, 7, True, "Poodle", "idk dog foods")
    
    # Test CatRepository:
    # Test 1: adding elements to the repo
    print("Test: add and show list of cats: \n")
    catRepo = CatRepository()
    catRepo.addCat(cat1)
    catRepo.showAll()
    
    print("Test: remove cat and show empty list: \n")
    catRepo.removeCat(1)
    catRepo.showAll()
    
    print("Test: update cat: \n")
    catRepo.addCat(cat2)
    catRepo.showAll()
    
    catRepo.updateCat(2)
    catRepo.showAll()
    
    
    
    
    
    
    
    
    
    