##importing the turtle module and the random module
import turtle
import random

###Exercise 1##########################################################

#initialize the global variables big_total and maximum_share to zero
global big_total
big_total = 0
    
global maximum_share
maximum_share = 0

#a function that returns the whole and remainder of a division equation
def div_w_remainder(dividend,divisor):

    whole = dividend//divisor
    remainder = dividend%divisor

    #returned the values of the whole and remainder
    return(whole,remainder)
    
#take two arguments number_of_things and number_of_people to pass to div_w_remainder
def share_items(number_of_things,number_of_people):


    #calls the function div_w_remainder and uses the amounts returned from this program to update two global variables
    #w stands for whole and r stands for remainder and is assignmed based on the share_items parameters
    w, r = div_w_remainder(number_of_things,number_of_people)

    #making a global variable that increases big_total by number_of_things
    global big_total
    big_total = big_total + number_of_things

    #making a global variable that increases maximum_share by the whole (the first item returned by div_w_remainder)
    global maximum_share
    maximum_share = maximum_share + w
    
    

    #increases maximum_share by 1, if remainder (the second item returned by div_w_remainder) is greater than 0
    if r > 0:
        maximum_share = maximum_share + 1

#calls share_items at least 3 times and shows that it works
def question_1():

    #calls share_items with arguments of 10 things and 4 people
    share_items(10,4)

    #calls share_items with arguments of 20 things and 3 people
    share_items(20,3)

    #calls share_items with arguments of 14 things and 7 people
    share_items(14,7)

    #A print statement to show the functions work with the global variables big_total and maximum_share valued at 44 and 12
    print("big_total: "+ str(big_total) + " & maximum_share: " + str(maximum_share))

#calls the function question_1()
question_1()

###Exercise 2##########################################################
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


