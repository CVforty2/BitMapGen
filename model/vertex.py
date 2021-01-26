class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __eq__(self, v):
        return self.x == v.x and self.y == v.y and self.z == v.z

    def __hash__(self):
        return hash(('x', self.x,
                     'y', self.y,
                     'z', self.z))
