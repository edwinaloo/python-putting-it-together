#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.size = size
        self.condition = "New"
        self.is_cobbled = False

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
        self.is_cobbled = True

stan_smith = Shoe("Addidas", 9)
stan_smith.cobble()

