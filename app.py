import numpy as np
from stl import mesh
from model.li_stl import LI_STL
import sys


if __name__ == "__main__":
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        conversion = sys.argv[2]

        stl = LI_STL(file_name)

        # print(type(stl.stl_mesh.data))
        # print()
        # print(stl.stl_mesh.data)
        # print()
        #
        # print(len(stl.stl_mesh.data['vectors']))
        # print(type(stl.stl_mesh.data['vectors']))
        # print()
        # print(stl.stl_mesh.data['vectors'][0])
        # print()
        # print(stl.stl_mesh.data['vectors'][0][0])
        # print()
        # print(stl.stl_mesh.data['vectors'][0][0][0])

        stl.convert_verts(conversion)
