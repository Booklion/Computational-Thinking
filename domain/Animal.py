class Animal():
    """
        An element of the class Animal has the following attributes:
        - name: the name of the animal
        - age: the age of the animal
        - timeInShelter: how much time the animal spent in the shelter (until present)
        - adopted: the adoption status of the animal
    """
    def __init__(self, ID: int, name: str, age: int, timeInShelter: int, adopted: bool):
        """
            Constructor
        """
        self.__id = ID 
        self.__name = name
        self.__age = age
        self.__timeInShelter = timeInShelter
        self.__adopted = adopted
        
    #Getters and setters
    
    def getID(self):
        """
            Getter for the ID.
        """
        return self.__id

    def setID(self, newID):
        """
            Setter for the ID.
            param newID: int, the new ID of the animal
        """
        self.__id = newID
    
    def getName(self):
        """
            Getter for the name.
        """
        return self.__name
    
    def setName(self, newName):
        """
            Setter for the name.
            param newName: string, the new name of the animal
        """
        self.__name = newName
        
    def getAge(self):
        """
            Getter for the age.
        """
        return self.__age
    
    def setAge(self, newAge):
        """
            Setter for the age.
            param newAge: integer, the new age of the animal
        """
        self.__age = newAge
        
    def getTimeInShelter(self):
        """
            Getter for the time the animal spent in shelter up until the present.
        """
        return self.__timeInShelter
    
    def setTimeInShelter(self, newTime):
        """
            Setter for the time the animal spent in shelter up until the present.
            param newTime: integer, the updated time spent in the shelter for the animal
        """
        self.__timeInShelter = newTime
    
    def getAdoptionStatus(self):
        """
            Getter for the adoption status of the animal.
        """
        return self.__adopted
    
    def setAdoptionStatus(self, newStatus):
        """
            Setter for the adoption status of the animal.
            param newStatus: bool, the new adoption status of the animal
        """
        self.__adopted = newStatus
        
    def __str__(self):
        return "ID: " + str(self.__id) + "\n" + "Name: " + self.__name + "\n" + "Age: " + str(self.__age) + "\n" + "Time in shelter: " + str(self.__timeInShelter) + " month(s)" + "\n" + "Adopted: " + str(self.__adopted)
        
        