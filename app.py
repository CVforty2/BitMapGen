import numpy as np
from stl import mesh
from model.li_stl import LI_STL






if __name__ == "__main__":
    file_name = "8.stl"
    stl = LI_STL(file_name)

    print('z', stl.max_z)
    print('x', stl.min_x, stl.max_x)
    print('y', stl.min_y, stl.max_y)
    print('verts', len(stl.verts))
