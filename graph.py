#!/bin/env python
# -*- coding:utf-8
"""
@author:xingz
@file:graph.py
@time:2022/11/24
"""
from typing import TypeVar, Generic, List

from pygraph.edge import Edge

V = TypeVar('V')  # type of the vertices in the graph


class Graph(Generic[V]):
    def __init__(self, vertices=None):
        if vertices is None:
            vertices = []
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in self._vertices]

    @property
    def vertex_count(self):
        return len(self._vertices)

    @property
    def edge_count(self):
        return sum(map(len, self._edges))

    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self, edge: Edge):
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u: int, v: int):
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first: V, second: V):
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    def vertex_at(self, index: int):
        return self._vertices[index]

    def index_of(self, vertex: V):
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index: int):
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self, vertex: V):
        return self.neighbors_for_index(self.index_of(vertex))

