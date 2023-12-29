import colorgram as cg
import turtle as t
import random

# colors = cg.extract('haistimage.jpg', 25)
# rgb_colors = []
# t.speed(100)
# screen = t.Screen()
#
# for coloring in colors:
#     r = coloring.rgb.r
#     g = coloring.rgb.g
#     b = coloring.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
tim = t.Turtle()
my_shape = tim.shape('arrow')
color_list = [(196, 166, 105), (133, 167, 194), (46, 103, 147), (147, 89, 40), (9, 21, 54), (189, 156, 33), (225, 208, 112), (62, 22, 9), (68, 120, 77), (58, 12, 23), (185, 140, 166), (136, 181, 149), (136, 28, 12), (132, 76, 105), (14, 43, 26), (18, 53, 137), (121, 26, 41), (170, 101, 137), (92, 152, 97), (175, 189, 217), (86, 121, 184)]
tim.speed('fastest')
t.colormode(255)


# for i in range(20):
#     tim.pensize(2)
#     tim.pendown()
#     tim.circle(5)
#     tim.penup()
#     tim.forward(10)
#     tim.color(random.choice(color_list))
#     tim.forward(25)


tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()


# square dot painting
def dot_painting():
    count = 0
    for _ in range(10):
        for step in range(10):
            tim.dot(20, random.choice(color_list))
            if step == 9:
                count += 1
                if count % 2 != 0:
                    turn_left()
                else:
                    turn_right()


def turn_right():
    tim.dot(20, random.choice(color_list))
    tim.right(90)
    tim.forward(35)
    tim.right(90)


def turn_left():
    tim.dot(20, random.choice(color_list))
    tim.left(90)
    tim.forward(35)
    tim.left(90)
n_of_dot = 100
# method two dot painting
for dot_count in range(1, n_of_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



#dot_painting()


screen = t.Screen()
screen.exitonclick()
