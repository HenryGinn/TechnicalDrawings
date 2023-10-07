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

my_lattice = Lattice(size_x=2)
hidden_cubic_lines = [[(0, 0, 0), (1/2, 1/2, 0)],
                      [(1, 0, 0), (1/2, 1/2, 0)],
                      [(0, 0, 0), (0, 0, 1)],
                      [(1/2, 1/2, 0), (1/2, 1/2, 1)]]
my_lattice.add_lines(hidden_cubic_lines, color="blue", line_scaling_x=1.5)
my_lattice.add_primitive()
my_lattice.add_base_centred()
my_lattice.draw()
