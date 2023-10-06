import math

import numpy as np

from hgutilities import defaults


class Line():

    def __init__(self, lattice, start, end, **kwargs):
        self.process_kwargs(**kwargs)
        self.lattice = lattice
        self.process_edges(start, end)

    def process_kwargs(self, **kwargs):
        defaults.kwargs(self, kwargs)
        self.process_color_kwargs()

    def process_color_kwargs(self):
        if self.vertex_color is None:
            self.vertex_color = self.color
        if self.edge_color is None:
            self.edge_color = self.color

    def process_edges(self, start, end):
        self.start, self.end = start, end
        self.define_base_edges()
        self.define_geometry()

    def define_base_edges(self):
        self.origin = self.get_point_from_parent(*self.start)
        self.direction = self.get_point_from_parent(*self.end)

    def get_point_from_parent(self, x, y, z):
        point = (x * self.lattice.base_x +
                 y * self.lattice.base_y +
                 z * self.lattice.base_z)
        return point

    def define_geometry(self):
        self.vertices, self.edges = [], []
        self.add_vertices_and_edges()
        self.remove_duplicate_vertices_and_edges()

    def add_vertices_and_edges(self):
        for base_vertex in self.lattice.base_vertices:
            start_point = base_vertex
            self.add_end_points(start_point)

    def add_end_points(self, start_point):
        end_point_1 = start_point + self.direction
        end_point_2 = start_point - self.direction
        self.add_point(start_point, end_point_1)
        self.add_point(start_point, end_point_2)

    def add_point(self, start_point, end_point):
        if self.valid_point(start_point) and self.valid_point(end_point):
            self.vertices.append(tuple(start_point))
            self.vertices.append(tuple(end_point))
            self.edges.append((tuple(start_point), tuple(end_point)))

    def valid_point(self, point):
        valid_x = self.valid_point_x(point)
        valid_y = self.valid_point_y(point)
        valid_z = self.valid_point_z(point)
        valid = (valid_x and valid_y and valid_z)
        return valid

    def valid_point_x(self, point):
        plane_constant = np.dot(point, self.lattice.normal_x)
        valid_minimum = (plane_constant >= self.lattice.spatial_x_min - self.tol)
        valid_maximum = (plane_constant <= self.lattice.spatial_x_max + self.tol)
        return (valid_minimum and valid_maximum)

    def valid_point_y(self, point):
        plane_constant = np.dot(point, self.lattice.normal_y)
        valid_minimum = (plane_constant >= self.lattice.spatial_y_min - self.tol)
        valid_maximum = (plane_constant <= self.lattice.spatial_y_max + self.tol)
        return (valid_minimum and valid_maximum)

    def valid_point_z(self, point):
        plane_constant = np.dot(point, self.lattice.normal_z)
        valid_minimum = (plane_constant >= self.lattice.spatial_z_min - self.tol)
        valid_maximum = (plane_constant <= self.lattice.spatial_z_max + self.tol)
        return (valid_minimum and valid_maximum)

    def remove_duplicate_vertices_and_edges(self):
        self.vertices = list(set(self.vertices))
        self.edges = list(set(self.edges))

defaults.load(Line)
