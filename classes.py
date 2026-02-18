class person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email  = email


    def talks(self):
        print(f"{self.name} talk!!!")

person1 = person("rahmo",20,"rahmo@gmail.com")
print(type(person1))

  



