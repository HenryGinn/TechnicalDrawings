"""
Lattice contains information about the whole structure.
It manages the basis vectors, the origin, the size of the
lattice, and which edges are present.

Each Edge object records information about a single direction
through the lattice. Each edge is given in terms of the
coordinates of a starting vertex and the coordinates of an
ending vertex. The coordinates are given in terms of the basis
vectors, and all vertices will be generated.
"""


from lattice import Lattice

my_lattice = Lattice(type="Hexagonal", size_x=3)
my_lattice.add_base_centred(color="blue")
#my_lattice.add_body_centred(color="blue")
#my_lattice.add_face_centred(color="blue")
my_lattice.draw()
