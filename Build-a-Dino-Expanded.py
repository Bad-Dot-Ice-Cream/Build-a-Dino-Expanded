import random

valid_dinos = ["Dino1", "Dino2", "Dino3"]


class Dinosaur:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species  #  [Flying Dinosaur, Water Dinosaur] etc.
        self.diet = diet
        self.age = age