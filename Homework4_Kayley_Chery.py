##importing libraries/modules
import math
import time

###Exercise 1##########################################################
#creating a function that takes an integer greater than zero and finds a sum for all the integers starting with 1 and ending with that integer
def triangle_number(num):

    #a variable is created for the amount of numbers iterated through in the while loop
    i = 0

    #a variable is created to hold the total sum of all the numbers leading up to the number taken into the function
    total = 0

    #making sure that the integer inputed is greater than 0
    if num > 0:

        #while i is less than the number arguement
        while i < num:

            #i increases each time that number is added to the total number
            i = i + 1
            total = total + i
            
            
    else:
        print("Input an integer greater than 0")
        
    return total

#testing to see if the function works with 5 as an example parameter  
print(triangle_number(5))

###Exercise 2##########################################################
#a function that creates a rectangle consisting of any character
#uses arguements height, width & character to create the rectangle
def make_rectangle(height, width, character):

    #counts the number of rows completed which accounts for the height of the rectangle
    row = 0
    
    #while the row number is less than the indicated height
    while row < height:
        #the row number increases
        row = row + 1

        #the row with the designated width is printed
        print(character * width)
        
#testing of the function works with a height of 4 characters, a width of 5 characters using the * symbol
make_rectangle(4, 5, "*")

###Exercise 3##########################################################
#a function that creates a parallelogram consisting of any character
def make_character_parallelogram(height, width, char):
    
    #counts the number of rows needed to complete the height of the parallelogram
    how_tall = height
    space = " "

    #while the number of rows that need to be drawn are greater than zero
    while how_tall > 0:
        print(space*(how_tall - 1 ) + char*width)
        how_tall = how_tall - 1

#testing out the parallelogram
make_character_parallelogram(4, 5, "*")

###Exercise 4##########################################################

#a functiom that prints out the time in format
def print_one_line(hrs,mins,secs,tenths):

    #converts the variable for tenth of a second into a string
    tenths = str(tenths)

    #if the hours are less than 10 it adds a zero in front of the number & changes the variable into to a string
    if hrs < 10:
        hrs = '0' + str(hrs)

    #if the hours are more than 10 it changes the variable into to a string
    else:
        hrs = str(hrs)

    #if the minutes are less than 10 it adds a zero in front of the number & changes the variable into to a string
    if mins < 10:
        mins = '0' + str(mins)

    #if the minutes are more than 10 it changes the variable into to a string
    else:
        mins = str(mins)

    #if the seconds are less than 10 it adds a zero in front of the number & changes the variable into to a string
    if secs < 10:
        secs = '0' + str(secs)

    #if the seconds are more than 10 it changes the variable into to a string
    else:
        secs = str(secs)
    
    #prints out the time following the format hours:minutes:seconds:deciseconds
    print(hrs + ":" + mins + ":" + secs + "."+ tenths)

#a function that counts the time, the clock function
def run_Clock():
    
    #a variable to keep the clock going
    count = 0

    #a variable that counts the amount of hours
    hours = 0

    #a variable that counts the minutes
    minutes = 0

    #a variable that counts the seconds
    seconds = 0

    #a variable that counts the deciseconds
    deciseconds = 0

    #a while loop that continuosly counts  
    while count == 0:

        #waits one decisecond before running the loop
        time.sleep(.1)

        #if the deciseconds equal 10, the number of seconds increases by one
        if deciseconds == 10:
            seconds = seconds + 1
            
            #the number of deciseconds resets
            deciseconds = 0
            
        #if the seconds equal 60, the number of minutes increases by one
        if seconds == 60:
            minutes = minutes + 1

            #the number of seconds resets
            seconds = 0

        #if the minutes are equal 60, the number of hours increases by one
        if minutes == 60:
            hours = hours + 1

            #the number of minutes resets
            minutes = 0

        #if the hours equal 24, the number of hours reset to 0
        if hours == 24:
            hours = 0
        
        #prints out the time using the print_one_line funciton to format the time     
        print_one_line(hours,minutes,seconds,deciseconds)

        #the number of deciseconds increases by one every decisecond
        deciseconds = deciseconds + 1

#calling the run clock function to start the clock
run_Clock()



