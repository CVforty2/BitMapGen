import numpy as np
from stl import mesh, base
import pprint

class STL:
    def __init__(self, file_name):
        self.stl_mesh = mesh.Mesh.from_file(file_name)



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

        list = self.stl_mesh.data.copy()

        for i in range(len(list)):
            list[i][1][0][0:3] *= conversion_factor
            list[i][1][1][0:3] *= conversion_factor
            list[i][1][2][0:3] *= conversion_factor

        data = np.asarray(list, dtype=mesh.Mesh.dtype)
        new_mesh = mesh.Mesh(data)
        new_mesh.save(f'new_stl.stl')
