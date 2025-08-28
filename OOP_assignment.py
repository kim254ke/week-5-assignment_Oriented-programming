#!/usr/bin/env python3

#  Assignment 1: Furniture Class with Inheritance
class Furniture:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def info(self):
        return f"{self.name} made of {self.material}"

# Chair inherits from Furniture
class Chair(Furniture):
    def __init__(self, name, material, legs):
        super().__init__(name, material)  # calling parent constructor
        self.legs = legs

    def details(self):
        return f"{self.info()} | Legs: {self.legs}"

# Table inherits from Furniture
class Table(Furniture):
    def __init__(self, name, material, shape):
        super().__init__(name, material)
        self.shape = shape

    def details(self):
        return f"{self.info()} | Shape: {self.shape}"


# Create objects of furniture
chair1 = Chair("Dining Chair", "Wood", 4)
table1 = Table("Coffee Table", "Glass", "Round")

print("=== Furniture Info ===")
print(chair1.details())
print(table1.details())


# Activity 2: Animal Voices (Polymorphism)
class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Sheep(Animal):
    def speak(self):
        print("🐑 Sheep bleats: Baa Baa!")

class Pig(Animal):
    def speak(self):
        print("🐖 Pig grunts: Oink Oink!")

class Goat(Animal):
    def speak(self):
        print("🐐 Goat bleats: Meeeh Meeeh!")

# Polymorphism 
print("\n=== Animal Voices ===")
animals = [Sheep(), Pig(), Goat()]

for animal in animals:
    animal.speak()
