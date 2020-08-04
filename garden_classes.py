class Tree:
    def __init__(self, shade = 2):
        self.shade = shade

class Gnome:
    def __init__ (self, rain = 0.05):
        self.rain = rain

class Woodchuck:
    def __init__(self, tree_felling = 0.05):
        self.tree_felling = tree_felling
class Garden:
    def __init__(self, name, water_level=0, trees=[], gnomes=[], woodchucks=[]):
        self.name = name
        self.water_level = water_level
        self.trees = trees
        self.gnomes = gnomes
        self.woodchucks = woodchucks

    def add_trees(self, plus_tree):
        self.trees.append(plus_tree)
    def add_gnomes(self,plus_gnome):
        self.gnomes.append(plus_gnome)
    def add_woodchuck(self, plus_woodchuck):
        self.woodchucks.append(plus_woodchuck)
    def water_level_chng (self, water_change):
        self.water_level += water_change

    def __str__ (self):
        return f"There are {len(self.trees)} trees in the garden, {len(self.gnomes)} gnomes in the garden, and {len(self.woodchucks)} woodchucks in the {self.name} garden."
    
