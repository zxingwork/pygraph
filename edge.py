#!/bin/env python
# -*- coding:utf-8
"""
@author:xingz
@file:edge.py.py
@time:2022/11/24
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Edge:
    u: int
    v: int

    def reversed(self) -> Edge:
        return Edge(self.v, self.u)

    def __str__(self):
        return f"{self.u}->{self.v}"
