#importing the turtle module and the random module
import turtle
import random

#a function setting up the turtle scene
def setup():
    turtle.setup(900,500,0,0)

#a function that draws the head of the stick figure
def head():
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

#a function that draws the body of the stick figure
def body():
    turtle.right(90)
    turtle.forward(100)

#a function that draws the arms of the stick figure
def arms():
    turtle.right(180)
    turtle.forward(60)
    turtle.right(60)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(60)
    turtle.right(60)
    turtle.forward(60)
    turtle.right(180)
    turtle.forward(60)

#a function that draws the legs of the stick figure
def legs():
    turtle.right(60)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(60)
    turtle.right(180)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(60)
    turtle.penup()
    
#a function that resets the pen to a place where it can start to draw the next stick figure
def reset():
    turtle.penup()
    turtle.left(60)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()

#a function that draws one stick figure
def make_stick_figure():
    head()
    body()
    arms()
    legs()
    reset()
    



# a function that randomizes the number of stick figures drawn in a rainbow pattern
def randomize():
    #calls the setup function
    setup()

    #creating a list of 5 random colors
    random_color_list = ["red", "orange", "green", "blue", "purple"]

    #creating a random number between 1 and 5 to indicate how many stick figures are created
    num_of_figures = random.randint(1, 5)

    #counts up everytime the while loop runs to control how many stick figures are drwan
    i = 0

    #while i is less than the number of figures that will be drawn
    while i < num_of_figures:
        #the color of the pen is choosen in sequence so the stick figures are drawn in a rainbow
        turtle.pencolor(random_color_list[i])

        #the fill color of the head also matches the color of the stick figure
        turtle.color(random_color_list[i], random_color_list[i])

        #draws a stick figure
        make_stick_figure()

        #the pen is lifted and moved to the spot of the new stick figure
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()

        #i increases by 1 everytime the while loop runs
        i = i + 1
        
#the randomized function is called   
randomize()
