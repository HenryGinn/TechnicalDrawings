"""
Conventions
The x axis vertexs to the right
The y axis vertexs into the screen
The z axis vertexs upwards

Angles are given in degrees
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
ax.set_axis_off()


lattice_type = "Face Centred"

xy_angle = np.pi/180 * 90
xz_angle = np.pi/180 * 90
yz_angle = np.pi/180 * 80

x_length = 1
y_length = 1
z_length = 1

vertex_000 = np.array([0, 0, 0])
vertex_100 = np.array([1, 0, 0])
vertex_010 = np.array([np.cos(xy_angle), np.sin(xy_angle), 0])
vertex_001 = np.array([np.cos(xz_angle),
                      np.cos(yz_angle)*np.sin(xz_angle),
                      np.sin(yz_angle)*np.sin(xz_angle)])

vertex_100 *= x_length
vertex_010 *= y_length
vertex_001 *= z_length

vertex_011 = vertex_010 + vertex_001
vertex_101 = vertex_100 + vertex_001
vertex_110 = vertex_100 + vertex_010
vertex_111 = vertex_100 + vertex_010 + vertex_001

vertices = [vertex_000, vertex_001, vertex_010, vertex_011,
            vertex_100, vertex_101, vertex_110, vertex_111]

main_edges = [(vertex_000, vertex_001), (vertex_000, vertex_010),
              (vertex_000, vertex_100), (vertex_010, vertex_011),
              (vertex_010, vertex_110), (vertex_001, vertex_101),
              (vertex_110, vertex_111), (vertex_100, vertex_110),
              (vertex_100, vertex_101), (vertex_001, vertex_011),
              (vertex_011, vertex_111), (vertex_101, vertex_111)]

point_110 = 0.5 * vertex_110
point_101 = 0.5 * vertex_101
point_011 = 0.5 * vertex_011
point_112 = point_110 + vertex_001
point_121 = point_101 + vertex_010
point_211 = point_011 + vertex_100
point_111 = 0.5 * vertex_111

points_primitive = []
points_base_centred = [point_110, point_112]
points_body_centred = [point_111]
points_face_centred = [point_110, point_101, point_011,
                       point_112, point_121, point_211]

edges_primitive = []
edges_base_centred = [(vertex_000, vertex_110), (vertex_001, vertex_111),
                      (vertex_100, vertex_010), (vertex_101, vertex_011)]
edges_body_centred = [(vertex_000, vertex_111), (vertex_100, vertex_011),
                      (vertex_010, vertex_101), (vertex_001, vertex_110)]
edges_face_centred = [(vertex_000, vertex_110), (vertex_001, vertex_111),
                      (vertex_100, vertex_010), (vertex_101, vertex_011),
                      (vertex_000, vertex_101), (vertex_100, vertex_001),
                      (vertex_010, vertex_111), (vertex_110, vertex_011),
                      (vertex_000, vertex_011), (vertex_010, vertex_001),
                      (vertex_100, vertex_111), (vertex_110, vertex_101)]

additional_points = {"Primitive": points_primitive,
                     "Base Centred": points_base_centred,
                     "Body Centred": points_body_centred,
                     "Face Centred": points_face_centred
                     }[lattice_type]

additional_edges = {"Primitive": edges_primitive,
                    "Base Centred": edges_base_centred,
                    "Body Centred": edges_body_centred,
                    "Face Centred": edges_face_centred
                    }[lattice_type]

points = vertices + additional_points
edges = main_edges + additional_edges

for edge in edges:
    edge_xyz = list(zip(*edge))
    ax.plot(*edge_xyz, color="black")
    
for point in points:
    ax.plot(*point, "ko")

plt.show()
