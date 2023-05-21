#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.size = size
        self.condition = "New"
        self.is_cobbled = False

    def repair(self):
        print("The shoe has been repaired.")
        self.condition = "New"
        self.is_cobbled = True




