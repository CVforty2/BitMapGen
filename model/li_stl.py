import numpy as np
from stl import mesh
from math import ceil
from .vertex import Vertex

class LI_STL:
    def __init__(self, file_name):
        self.verts = []
        self.max_z = 0
        self.max_y = 0
        self.min_y = 0
        self.max_x = 0
        self.min_x = 0

        _ = self.read_file(file_name)
        self.make_verts(_)
        self.remove_duplicates()


    def read_file(self, file_name):
        np_mesh = mesh.Mesh.from_file(file_name)
        return np_mesh


    def make_verts(self, mesh):
        for point in mesh.points:
            #                  X,         Y,        Z
            vert_1 = Vertex(point[0], point[1], point[2])
            vert_2 = Vertex(point[3], point[4], point[5])
            vert_3 = Vertex(point[6], point[7], point[8])

            self.max_x = max(self.max_x, point[0], point[3], point[6])
            self.max_y = max(self.max_y, point[1], point[4], point[7])
            self.max_z = max(self.max_z, point[2], point[5], point[8])

            self.min_x = min(self.min_x, point[0], point[3], point[6])
            self.min_y = min(self.min_y, point[1], point[4], point[7])

            self.verts.extend((vert_1, vert_2, vert_3))


    def linear_interpolate(self):
        for v in self.verts:
            # converts z into a grayscale color
            v.z = math.ceil(((v.z / self.max_z) * 255))

    def remove_duplicates(self):
        self.verts = list(set(self.verts))
