import numpy as np
from stl import mesh, base

class LI_STL:
    def __init__(self, file_name):
        self.mesh = mesh.Mesh.from_file(file_name)


    def test(self):
        print(self.mesh.data[0])
        print(len(self.mesh.data[0]))
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

        list_of_triangles = np.zeros(len(self.mesh.data), dtype=base.BaseMesh.dtype)
        for point in self.mesh.data:
            vertex_of_triangle = np.zeros(3, dtype=base.BaseMesh.dtype)
            for i in point:
                vertex_of_triangle = np.append(vertex_of_triangle, i)
            list_of_triangles = np.vstack([list_of_triangles, vertex_of_triangle])

        self.mesh.data = list_of_triangles
        self.mesh.update_normals()
