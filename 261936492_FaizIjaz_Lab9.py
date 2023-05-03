class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return self.name
        return self.age
        
class House:
    
    def __init__(self,address,numOfrooms):
        self.address = address
        self.numOfrooms = numOfrooms
        self.persons = []
        
    def add_person(self,obj):
        self.persons.append(obj)
        
    def remove_person(self,obj):
        for i in self.persons:
            if i == obj:
                self.persons.remove(i)
            else:
                continue
            
    def display(self):
        for i in range(0,len(self.persons)):
            print("Person",i+1,"Name:",self.persons[i].display())
            
Faiz = Person("Faiz",14)
Mansion = House("103 Ghulshan ",5)
Mansion.add_person(Faiz)
Mansion.add_person(Person("Abdullah",21))
Mansion.display()
Mansion.remove_person(Faiz)
Mansion.display()