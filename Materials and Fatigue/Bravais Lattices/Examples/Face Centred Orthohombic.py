import sys
sys.path.append("..")

from lattice import Lattice

my_lattice = Lattice(type="Orthohombic", zoom=1, pad_inches=-0.4,
                     elev=24, azim=-76)
my_lattice.add_primitive()
my_lattice.add_face_centred(edge_color="gray")

my_lattice.create_lattice()
#my_lattice.show()
my_lattice.save("Face Centred Orthohombic")
