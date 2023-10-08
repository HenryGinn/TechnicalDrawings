from lattice import Lattice

my_lattice = Lattice(size_x=2)
"""
hidden_cubic_lines = [[(0, 0, 0), (1/2, 1/2, 0)],
                      [(1, 0, 0), (1/2, 1/2, 0)],
                      [(0, 0, 0), (0, 0, 1)],
                      [(1/2, 1/2, 0), (1/2, 1/2, 1)]]
my_lattice.add_lines(hidden_cubic_lines, color="blue", line_scaling_x=1.5)
"""
my_lattice.add_primitive()
#my_lattice.add_face_centred()
my_lattice.draw()
