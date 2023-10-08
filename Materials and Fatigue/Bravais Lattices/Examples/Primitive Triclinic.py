import sys
sys.path.append("..")

from lattice import Lattice

my_lattice = Lattice(type="Triclinic", zoom=1, pad_inches=-0.4)
my_lattice.add_primitive()

# Add side length labels
space = 0.12
my_lattice.add_text((0.45, -space, -space), "$a$")
my_lattice.add_text((1 + space, 0.45, -space), "$b$")
my_lattice.add_text((-space, -space, 0.5), "$c$")

# Add angle arcs
my_lattice.add_angle((0, 0, 0), (0.4, 0, 0), (0, 0, 0.4))
my_lattice.add_angle((0, 0, 1), (0.4, 0, 0), (0, 0.4, 0))
my_lattice.add_angle((1, 0, 0), (0, 0.4, 0), (0, 0, 0.4))

# Add angle labels
space = 0.25
my_lattice.add_text((space, 0, space), "$\\alpha$")
my_lattice.add_text((1, space, space), "$\\beta$")
my_lattice.add_text((space, space, 1), "$\\gamma$")

my_lattice.create_lattice()
my_lattice.show()
#my_lattice.save("Lattice Example")
