import numpy as np
from stl import mesh

class LI_STL:
    def __init__(self, file_name):
        self.mesh = mesh.Mesh.from_file(file_name)


    def test(self):
        for i in self.mesh.points:
            for j in i:
                print(j)

    def convert_verts(self, conversion):
        conversion_factor = 1.0

        if conversion == "in2cm":
            conversion_factor = 2.54
        elif conversion == "in2mm":
            conversion_factor = 25.4
        elif conversion == "cm2in":
            conversion_factor = 0.393701
        elif conversion == "cm2mm":
            conversion_factor = 10
        else:
            return

        list_of_triangles = []
        for point in self.mesh.points:
            vertex_of_triangle = []
            for i in point:
                vertex_of_triangle.append(i * conversion_factor)
            list_of_triangles.append(vertex_of_triangle)

        self.mesh.points = list_of_triangles
