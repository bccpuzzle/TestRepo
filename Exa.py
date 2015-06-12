from enum import Enum


class Type(Enum):
    Flood = 0
    Cyclon = 1

class Exa(object):
    def __init__(self, ex1, ex2):
        self.ex1 = ex1
        self.ex2 = ex2

