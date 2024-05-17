from turtle import Turtle, Screen, colormode
import colorgram, random


tim = Turtle()
screen = Screen()

colormode(255)

tim.speed(0)
tim.hideturtle()


# extract colors from image and make list of them
colors = colorgram.extract("18 - Turtle and Graphic interfaces//Exercises//download.jpg", 100)
rgb_colors = []

for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.b, color.rgb.g ))    

print(len(rgb_colors))
print(len(colors))


def startgame(row, columns):

    number_of_dots = row*columns

    tim.penup()
    tim.setheading(225)
    tim.forward(400)
    tim.setheading(0)


    for i in range(1, number_of_dots):
        ind = random.randint(0, len(rgb_colors)-1)
        tim.dot(20, rgb_colors[ind])
        tim.forward(50)

        # tim.penup()    
        # tim.pendown()



        if i % columns == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(50*columns)
            tim.setheading(0)



startgame(10, 5)



SPACE = 50
RADIUS = 20






screen.exitonclick()

