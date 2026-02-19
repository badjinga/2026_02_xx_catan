
class Vertex:
    def __init__(self):
        self.adjacent_hexes = []  # List of up to 3 Hexagons

    def print_test(self):
        print("banana")

class Hexagon:
    def __init__(self, resource, number, vertices):
        self.resource = resource
        self.number = number
        self.vertices = vertices  # List of 6 Vertices

class Board:
    def __init__(self, number_of_tiles=19):
        self.number_of_tiles = number_of_tiles
        self.hexagons = []
        self.vertices = []


board = Board(19)

# I want to be able to acess to the acess the the vertexes

# Whenever i draw the dice each and every tile (hexagon) that has a value 

# In my oppinion the best approach will be running all the hexagons