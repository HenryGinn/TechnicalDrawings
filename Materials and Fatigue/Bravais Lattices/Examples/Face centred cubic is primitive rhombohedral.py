import sys
sys.path.append("..")

from lattice import Lattice

my_lattice = Lattice()
rhombohedral = [[(1/2, 1/2, 0), (1/2, 1, 1/2)],
                [(0, 0, 0), (0, 1/2, 1/2)],
                [(1/2, 1/2, 0), (1, 1/2, 1/2)],
                [(0, 0, 0), (1/2, 0, 1/2)],
                [(1/2, 1/2, 0), (0, 0, 0)],
                [(1/2, 0, 1/2), (1, 1/2, 1/2)]]
my_lattice.add_lines(rhombohedral, color="blue",
                     normal_x_coefficients=(1, -1, 1),
                     normal_y_coefficients=(1, 1, -1),
                     normal_z_coefficients=(-1, 1, 1))
my_lattice.add_primitive()
my_lattice.add_base_centred()
my_lattice.draw()
