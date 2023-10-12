import os

from hgutilities import defaults
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from line import Line

class Lattice():

    def __init__(self, **kwargs):
        self.process_kwargs(kwargs)
        self.set_geometry()
        self.set_spatial_limits()
        self.create_figure()

    def process_kwargs(self, kwargs):
        defaults.kwargs(self, kwargs)
        self.lines = []
        self.current_level = 0
        self.set_type()

    def set_type(self):
        self.set_type_function_dict()
        if self.type is not None:
            self.type_function_dict[self.type]()

    def set_type_function_dict(self):
        self.type_function_dict = (
            {"Cubic": self.set_type_cubic,
             "Orthohombic": self.set_type_orthohombic,
             "Hexagonal": self.set_type_hexagonal,
             "Tetragonal": self.set_type_tetragonal,
             "Triclinic": self.set_type_triclinic,
             "Monoclinic": self.set_type_monoclinic,
             "Rhombohedral": self.set_type_rhombohedral})

    def set_type_cubic(self):
        self.angle_xy, self.angle_yz, self.angle_zx = 90, 90, 90
        self.length_x, self.length_y, self.length_z = 1, 1, 1

    def set_type_orthohombic(self):
        self.angle_xy, self.angle_yz, self.angle_zx = 90, 90, 90
        self.length_x, self.length_y, self.length_z = 1, 1.25, 1.5

    def set_type_hexagonal(self):
        self.angle_xy, self.angle_yz, self.angle_zx = 60, 90, 90
        self.length_x, self.length_y, self.length_z = 1, 1, 1.5

    def set_type_tetragonal(self):
        self.angle_xy, self.angle_yz, self.angle_zx = 90, 90, 90
        self.length_x, self.length_y, self.length_z = 1, 1, 1.5

    def set_type_triclinic(self):
        self.angle_xy, self.angle_yz, self.angle_zx = 70, 75, 80
        self.length_x, self.length_y, self.length_z = 1, 1.25, 1.5

    def set_type_monoclinic(self):
        self.angle_xy, self.angle_yz, self.angle_zx = 90, 80, 90
        self.length_x, self.length_y, self.length_z = 1, 1.25, 1.5

    def set_type_rhombohedral(self):
        self.angle_xy, self.angle_yz, self.angle_zx = 80, 80, 80
        self.length_x, self.length_y, self.length_z = 1, 1, 1

    def set_geometry(self):
        self.set_limits()
        self.set_base_vectors()
        self.set_base_vertices()

    def set_limits(self):
        origin_x = self.set_limits_x()
        origin_y = self.set_limits_y()
        origin_z = self.set_limits_z()
        self.origin = np.array([origin_x, origin_y, origin_z])

    def set_limits_x(self):
        if self.size_x % 2 == 0:
            return self.set_limits_x_even()
        else:
            return self.set_limits_x_odd()

    def set_limits_x_even(self):
        self.x_limit_min = -int(self.size_x / 2)
        self.x_limit_max = int(self.size_x / 2)
        origin_x = 0
        return origin_x

    def set_limits_x_odd(self):
        self.x_limit_min = -int((self.size_x - 1) / 2)
        self.x_limit_max = int((self.size_x + 1) / 2)
        origin_x = -0.5
        return origin_x

    def set_limits_y(self):
        if self.size_y % 2 == 0:
            return self.set_limits_y_even()
        else:
            return self.set_limits_y_odd()

    def set_limits_y_even(self):
        self.y_limit_min = -int(self.size_y / 2)
        self.y_limit_max = int(self.size_y / 2)
        origin_y = 0
        return origin_y

    def set_limits_y_odd(self):
        self.y_limit_min = -int((self.size_y - 1) / 2)
        self.y_limit_max = int((self.size_y + 1) / 2)
        origin_y = -0.5
        return origin_y

    def set_limits_z(self):
        if self.size_z % 2 == 0:
            return self.set_limits_z_even()
        else:
            return self.set_limits_z_odd()

    def set_limits_z_even(self):
        self.z_limit_min = -int(self.size_z / 2)
        self.z_limit_max = int(self.size_z / 2)
        origin_z = 0
        return origin_z

    def set_limits_z_odd(self):
        self.z_limit_min = -int((self.size_z - 1) / 2)
        self.z_limit_max = int((self.size_z + 1) / 2)
        origin_z = -0.5
        return origin_z

    def set_base_vectors(self):
        self.base_x = np.array([1, 0, 0])
        self.base_y = np.array([np.cos(np.pi/180*self.angle_xy),
                                np.sin(np.pi/180*self.angle_xy), 0])
        self.set_base_z()
        self.adjust_basis_vectors()

    def set_base_z(self):
        self.base_z = np.array([np.cos(np.pi/180*self.angle_zx),
                                np.cos(np.pi/180*self.angle_yz)*np.sin(np.pi/180*self.angle_zx),
                                np.sin(np.pi/180*self.angle_yz)*np.sin(np.pi/180*self.angle_zx)])

    def adjust_basis_vectors(self):
        self.base_x = np.round(self.base_x * self.length_x, 5)
        self.base_y = np.round(self.base_y * self.length_y, 5)
        self.base_z = np.round(self.base_z * self.length_z, 5)

    def set_base_vertices(self):
        self.base_vertices = [self.get_position(x, y, z)
                              for x in range(self.x_limit_min - 1, self.x_limit_max + 2)
                              for y in range(self.y_limit_min - 1, self.y_limit_max + 2)
                              for z in range(self.z_limit_min - 1, self.z_limit_max + 2)]

    def get_position(self, x, y, z):
        vertex = (self.origin +
                  x * self.base_x +
                  y * self.base_y +
                  z * self.base_z)
        return vertex
    
    def get_position_orthonormal_basis(self, x, y, z):
        x /= self.length_x
        y /= self.length_y
        z /= self.length_z
        return self.get_position(x, y, z)

    def set_spatial_limits(self):
        self.set_spatial_limits_x()
        self.set_spatial_limits_y()
        self.set_spatial_limits_z()

    def set_spatial_limits_x(self):
        self.normal_x = np.cross(self.base_y, self.base_z)
        self.spatial_x_min = self.get_spatial_limit(
            self.x_limit_min, self.base_x, self.normal_x)
        self.spatial_x_max = self.get_spatial_limit(
            self.x_limit_max, self.base_x, self.normal_x)

    def set_spatial_limits_y(self):
        self.normal_y = np.cross(self.base_z, self.base_x)
        self.spatial_y_min = self.get_spatial_limit(
            self.y_limit_min, self.base_y, self.normal_y)
        self.spatial_y_max = self.get_spatial_limit(
            self.y_limit_max, self.base_y, self.normal_y)

    def set_spatial_limits_z(self):
        self.normal_z = np.cross(self.base_x, self.base_y)
        self.spatial_z_min = self.get_spatial_limit(
            self.z_limit_min, self.base_z, self.normal_z)
        self.spatial_z_max = self.get_spatial_limit(
            self.z_limit_max, self.base_z, self.normal_z)

    def get_spatial_limit(self, constant, basis, normal):
        extreme_point = self.origin + constant*basis
        plane_constant = np.dot(extreme_point, normal)
        return plane_constant

    def create_figure(self):
        self.fig = plt.figure(figsize=plt.figaspect(1))
        self.ax = Axes3D(self.fig, auto_add_to_figure=False)
        self.fig.add_axes(self.ax)
        self.ax.set_axis_off()
        self.ax.view_init(elev=self.elev, azim=self.azim, roll=self.roll)

    def add_primitive(self, **kwargs):
        starts_and_ends = [[(0, 0, 0), (1, 0, 0)],
                           [(0, 0, 0), (0, 1, 0)],
                           [(0, 0, 0), (0, 0, 1)]]
        self.add_lines(starts_and_ends, **kwargs)

    def add_base_centred(self, **kwargs):
        starts_and_ends = [[(0, 0, 0), (1/2, 1/2, 0)],
                           [(1, 0, 0), (1/2, 1/2, 0)]]
        self.add_lines(starts_and_ends, **kwargs)

    def add_body_centred(self, **kwargs):
        starts_and_ends = [[(0, 0, 0), (1/2, 1/2, 1/2)],
                           [(0, 0, 0), (1/2, 1/2, 1/2)],
                           [(0, 1, 0), (1/2, 1/2, 1/2)],
                           [(1, 1, 0), (1/2, 1/2, 1/2)]]
        self.add_lines(starts_and_ends, **kwargs)

    def add_face_centred(self, **kwargs):
        starts_and_ends = [[(0, 0, 0), (1/2, 1/2, 0)],
                           [(1, 0, 0), (1/2, 1/2, 0)],
                           [(0, 0, 0), (0, 1/2, 1/2)],
                           [(0, 1, 0), (0, 1/2, 1/2)],
                           [(0, 0, 0), (1/2, 0, 1/2)],
                           [(0, 0, 1), (1/2, 0, 1/2)]]
        self.add_lines(starts_and_ends, **kwargs)

    def add_lines(self, starts_and_ends, **kwargs):
        for start_and_end in starts_and_ends:
            start, end = start_and_end
            self.lines.append(
                Line(self, start, end, level=self.current_level, **kwargs))
        self.current_level += 1

    def create_lattice(self):
        self.order_geometry()
        self.draw_geometry()
        self.fix_scaling_and_zoom()

    def order_geometry(self):
        self.order_edges()
        self.order_vertices()

    def order_edges(self):
        self.edges = {}
        for line in self.lines:
            for edge in line.edges:
                self.process_edge(edge, line)

    def process_edge(self, edge, line):
        if ((edge not in self.edges)
            or (self.edges[edge].level > line.level)):
            self.edges.update({edge: line})

    def order_vertices(self):
        self.vertices = {}
        for line in self.lines:
            for vertex in line.vertices:
                self.process_vertex(vertex, line)

    def process_vertex(self, vertex, line):
        if ((vertex not in self.vertices)
            or (self.vertices[vertex].level > line.level)):
            self.vertices.update({vertex: line})

    def draw_geometry(self):
        self.draw_edges()
        self.draw_vertices()

    def draw_edges(self):
        for edge, line in self.edges.items():
            if line.suppress_edges is False:
                self.draw_edge(edge, line)

    def draw_edge(self, edge, line):
        self.ax.plot(*zip(*edge), color=line.edge_color,
                     linewidth=line.linewidth,
                     linestyle=line.linestyle)

    def draw_vertices(self):
        for vertex, line in self.vertices.items():
            self.ax.plot(*vertex, color=line.vertex_color,
                         markersize=line.vertex_size,
                         marker=line.vertex_style)

    def fix_scaling_and_zoom(self):
        scaling = np.array([getattr(self.ax, f"get_{dim}lim")() for dim in 'xyz'])
        self.ax.auto_scale_xyz(*[[np.min(scaling), np.max(scaling)]]*3)
        self.ax.set_aspect('equal')
        self.ax.set_box_aspect((1, 1, 1), zoom=self.zoom)

    def add_text(self, coordinates, text):
        position = self.get_position(*coordinates)
        self.ax.text(*position, text, size=self.fontsize)

    def add_angle(self, point, direction_1, direction_2):
        position, vector_1, vector_2 = self.get_angle_data(
            point, direction_1, direction_2)
        arc_points = self.get_arc_points(position, vector_1, vector_2)
        self.plot_arc(arc_points)

    def get_angle_data(self, point, direction_1, direction_2):
        position = self.get_position(*point)
        vector_1 = self.get_position_orthonormal_basis(*direction_1) - self.origin
        vector_2 = self.get_position_orthonormal_basis(*direction_2) - self.origin
        return position, vector_1, vector_2

    def get_arc_points(self, position, vector_1, vector_2):
        theta = np.linspace(0, np.pi/2, 20)
        points = ((np.outer(vector_1, np.cos(theta)) + np.outer(vector_2, np.sin(theta))) /
                  np.sqrt(1 + np.sin(2*theta)*np.dot(vector_1, vector_2))
                  + np.outer(position, np.ones(20)))
        return points

    def add_right_angle(self, point, direction_1, direction_2):
        position, vector_1, vector_2 = self.get_angle_data(
            point, direction_1, direction_2)
        arc_points = self.get_right_arc_points(position, vector_1, vector_2)
        self.plot_arc(arc_points)

    def get_right_arc_points(self, position, vector_1, vector_2):
        arc_points = np.array([position + vector_1,
                               position + vector_1 + vector_2,
                               position + vector_2])
        return np.transpose(arc_points)

    def plot_arc(self, arc_points):
        self.ax.plot(*arc_points, color=self.angle_color)

    def show(self):
        plt.show()

    def save(self, file_name):
        file_name = os.path.join("Figures", f"{file_name}.{self.format}")
        plt.savefig(file_name, format=self.format, bbox_inches='tight',
                    pad_inches=self.pad_inches)
        
defaults.load(Lattice)
