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

    def add_edge(self, edge:Edge):

        pass