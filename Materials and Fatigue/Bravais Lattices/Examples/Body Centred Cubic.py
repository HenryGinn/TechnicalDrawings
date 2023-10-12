import sys
sys.path.append("..")

from lattice import Lattice

my_lattice = Lattice(type="Cubic", zoom=1, pad_inches=-0.4,
                     elev=24, azim=-76)
my_lattice.add_primitive()
my_lattice.add_body_centred(edge_color="gray")

my_lattice.create_lattice()
#my_lattice.show()
my_lattice.save("Body Centred Cubic")
