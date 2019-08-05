from oop.Animal import Animal


class Cat(Animal):
    def run(self):
        print("Cat is running")

cat = Cat()
cat.run()

