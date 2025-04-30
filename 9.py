
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")


car1 = Car("Toyota", "Corolla")
car1.show_details()
