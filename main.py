# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 35)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


# 10 by 10
# 20 in size spaced apart by 50 paces

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)

color_list = [(43, 2, 176), (79, 253, 174), (226, 149, 109),
              (230, 225, 253), (160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247),
              (252, 253, 53), (184, 184, 251), (211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0),
              (252, 36, 35), (50, 240, 56), (216, 114, 171), (16, 127, 144), (85, 248, 252), (188, 39, 109),
              (23, 5, 107), (8, 209, 215), (99, 8, 50), (231, 163, 205), (204, 119, 35), (112, 6, 4),
              (239, 165, 161), (8, 114, 21)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_of_dots = 100a

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
