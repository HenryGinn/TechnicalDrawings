import sys
sys.path.append("..")

from lattice import Lattice

my_lattice = Lattice(type="Monoclinic", zoom=1, pad_inches=-0.4)
my_lattice.add_primitive()

# Add side length labels
space = 0.12
my_lattice.add_text((0.45, -space, -space), "$a$")
my_lattice.add_text((1 + space, 0.45, -space), "$b$")
my_lattice.add_text((-space, -space, 0.5), "$c$")

# Add angle arcs
my_lattice.add_right_angle((0, 0, 0), (0.25, 0, 0), (0, 0, 0.25)) # alpha
my_lattice.add_angle((1, 0, 0), (0, 0.4, 0), (0, 0, 0.4)) # beta
my_lattice.add_right_angle((0, 0, 1), (0.25, 0, 0), (0, 0.25, 0)) # gamma

# Add angle labels
space = 0.3
my_lattice.add_text((1, space, space), "$\\beta$")

my_lattice.create_lattice()
my_lattice.show()
#my_lattice.save("Primitive Monoclinic")
