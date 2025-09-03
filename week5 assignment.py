from abc import ABC, abstractmethod

# ------------------------
# Assignment 1: Smartphone Class 🏗️
# ------------------------
class Smartphone:
    def __init__(self, brand: str, model: str, storage: int) -> None:
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number: str) -> str:
        return f"Calling {number} from {self.model} 📞"
    
    def take_photo(self) -> str:
        return f"{self.model} is taking a photo 📸"
    
    def __str__(self) -> str:
        return f"{self.brand} {self.model} with {self.storage}GB storage"


class GamingPhone(Smartphone):
    def __init__(self, brand: str, model: str, storage: int, gpu: str) -> None:
        super().__init__(brand, model, storage)
        self.gpu = gpu
    
    def play_game(self, game: str) -> str:
        return f"Playing {game} smoothly on {self.model} with {self.gpu} 🎮"
    
    def take_photo(self) -> str:  # override (polymorphism)
        return f"{self.model} takes high-resolution gaming screenshots 🖼️"


# ------------------------
# Activity 2: Polymorphism Challenge 🎭
# ------------------------
class Vehicle(ABC):
    @abstractmethod
    def move(self) -> str:
        pass


class Car(Vehicle):
    def move(self) -> str:
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self) -> str:
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self) -> str:
        return "Sailing 🚤"


# ------------------------
# Testing Section
# ------------------------
if __name__ == "__main__":
    # Assignment 1 demo
    phone1 = Smartphone("Apple", "iPhone 14", 128)
    phone2 = GamingPhone("Asus", "ROG 6", 256, "Adreno 730")

    print(phone1.call("0712345678"))
    print(phone1.take_photo())
    print(phone2.play_game("PUBG"))
    print(phone2.take_photo())
    print(phone2)  # Uses __str__

    print("\n--- Polymorphism Demo ---")
    vehicles: list[Vehicle] = [Car(), Plane(), Boat()]
    for v in vehicles:
        print(v.move())
