import sys
sys.path.append("..")

from lattice import Lattice

my_lattice = Lattice(type="Triclinic", zoom=1, pad_inches=-0.4)
my_lattice.add_primitive()
my_lattice.add_text((0.5, -0.15, -0.15), "$a$")
my_lattice.add_text((1.15, 0.5, -0.15), "$b$")
my_lattice.add_text((-0.15, -0.15, 0.5), "$c$")
my_lattice.create_lattice()

my_lattice.show()
#my_lattice.save("Lattice Example")
