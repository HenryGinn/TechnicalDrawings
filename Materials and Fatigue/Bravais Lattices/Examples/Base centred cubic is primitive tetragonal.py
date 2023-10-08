import sys
sys.path.append("..")

from lattice import Lattice

my_lattice = Lattice(size_x=2)
base_centred = [[(0, 0, 0), (1/2, 1/2, 0)],
                [(1, 0, 0), (1/2, 1/2, 0)],
                [(0, 0, 0), (0, 0, 1)],
                [(1/2, 1/2, 0), (1/2, 1/2, 1)]]
my_lattice.add_lines(base_centred, color="blue",
                     line_scaling_x=1.5)
my_lattice.add_primitive()
my_lattice.add_base_centred()
my_lattice.draw()
