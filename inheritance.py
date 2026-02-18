class animamal:
    def __init__(self,name):
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} makes some sound!!")


class dog(animal):
    def make_sound(self):
        return super().make_sound()
        

class horse(animal):
    def make_sound(self):
        return super().make_sound()
    

    d1 = dog("max")
    print(type(d1))
    print(d1.name)
    d1.make_sound()

    h1 = horse("star")
    print(type(h1))
    print(h1.name)
    h1.make_sound()



    class person:
        def __init__(self,name,age):
            super().__init__(name,age)

            self.name = name
            self.age = age

        def works(self):
            print(f"{self.name} teachers!!")

        class student(person):
            def __init__(self,name,age):
                super().__init__(name,age)
            def works(self):
                print(f"{self.name} studies")

        def works(self):
            print(f"{self.name} teachers!!")

        def display(self):
            print


        



