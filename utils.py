from math import sin,cos,pi
#contructs a regular polygon which approximates a circle
def regular_polygon(n_sides,rad,pos):
    points = []
    
    for side in range(n_sides):
        angle = (pi * 2 * side) / n_sides
        points.append([int(pos[0] + cos(angle) * rad), int(pos[1] + sin(angle) * rad)])
    return points