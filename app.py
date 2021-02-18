import numpy as np
from stl import mesh
from model.stl_c import STL
import sys


if __name__ == "__main__":
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        conversion = sys.argv[2]
        
        stl = STL(file_name)

        stl.convert_verts(conversion)
