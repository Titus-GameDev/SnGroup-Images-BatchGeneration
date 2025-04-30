# Copyright Titus Thompson, 2025. All Rights Reserved.

import math
from manim import *
import sys

# Make sure arg 1 is filled in with value N.
# Make sure args 2 and 3 are filled out with values in range [1,n]
# and arg 4 is filled out with a value in range [1,2].
p1 = int(sys.argv[1])   # N
p2 = int(sys.argv[2])   # Arrow start point
p3 = int(sys.argv[3])   # Arrow end point
p4 = int(sys.argv[4])   # Arrow direction

class CreateParameterizedSnGroup(Scene):
    def construct(self):
        dot_locations = dict()
        dots = []
        radius = 3.0
        for i in range(0,p1):
            point = [radius * math.sin((i*math.tau/p1)), radius * math.cos((i*math.tau/p1)), 0]
            dot = Dot(point, 0.3, 0.0, 1.0, ManimColor('#FFFFFF'))
            dots.append(dot)
            dot_locations[dot] = point
            if (p2 == p3 == p4 == 0):
                self.add(dot)
        
        for dot1 in dots:
            i = dots.index(dot1)
            for dot2 in dots:
                j = dots.index(dot2)
                if dot1 != dot2 and p2 == i + 1 and p3 == j + 1:
                    
                    if (p4 == 1):
                        line_gradient= Line(dot1, dot2, stroke_width=10.0, buff= 0.2, path_arc=0.35).add_tip(tip_shape=StealthTip, tip_length=1.0, tip_width= 1.0)
                        #line_gradient=Arrow(dot1, dot2, stroke_width= 10.0, buff= 0.2, path_arc = 0.35)
                        sheen_direction = (RIGHT-LEFT)/5.0

                        line_gradient.set_color([ORANGE,BLUE])
                        line_gradient.set_sheen_direction(sheen_direction)

                        self.add(line_gradient)
                        line_gradient.tip.color = ORANGE
                    
                    if (p4 == 2):
                        line_gradient2= Line(dot2, dot1, stroke_width=10.0, buff= 0.2, path_arc=0.35).add_tip(tip_shape=StealthTip, tip_length=1.0, tip_width= 1.0)
                        #line_gradient2=Arrow(dot2, dot1, stroke_width= 10.0, buff= 0.2, path_arc = 0.35)
                        sheen_direction2 = (LEFT-RIGHT)/5.0

                        line_gradient2.set_color([ORANGE,BLUE])
                        line_gradient2.set_sheen_direction(sheen_direction2)

                        self.add(line_gradient2)
                        line_gradient2.tip.color = ORANGE

with tempconfig({"quality": "high_quality", "preview": False}):
    scene = CreateParameterizedSnGroup()
    scene.render()