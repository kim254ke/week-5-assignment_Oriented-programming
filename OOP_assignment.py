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
    def move(self):
        print("This animal moves somehow.")

class Sheep(Animal):
    def move(self):
        print("🐑 Sheep moves while bleating: Baa Baa!")

class Pig(Animal):
    def move(self):
        print("🐖 Pig moves while grunting: Oink Oink!")

class Goat(Animal):
    def move(self):
        print("🐐 Goat moves while bleating: Meeeh Meeeh!")

# Polymorphism demo
print("\n=== Animal Movements ===")
animals = [Sheep(), Pig(), Goat()]

for animal in animals:
    animal.move()

