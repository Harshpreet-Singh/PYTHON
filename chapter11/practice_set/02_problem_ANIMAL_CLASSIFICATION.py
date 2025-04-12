class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):

    @staticmethod  # because of this we don't need to use self
    def bark():
        print("\033[1;93m 🐾  ~*~*~  BOW  BOW!  ~*~*~  🐾")


d = Dog()

d.bark()


