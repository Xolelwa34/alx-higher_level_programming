#!/usr/bin/python3
"""Defines a pascal triangle."""

def pascal_triangle(n):
    """ Pascal Triangle 1h"""
    tria = []
    if n <= 0:
        return tria
    for r in range(n):
        for c in range(r + 1):
            if c == 0:
                tria.append([1])
            elif c == r:
                tria[r].append(1)
            else:
                tria[r].append(tria[r - 1][c] + tria[r - 1][c - 1])
    return tria
