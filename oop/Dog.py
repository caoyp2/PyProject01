from oop.Animal import Animal


class Dog(Animal):
    def run(self):
        print("Dog is running")



dog = Dog()
dog.run()

dog1 = Dog()
dog1.run_twice(dog1)

