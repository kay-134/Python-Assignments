import math

######## exercise 1##############################################
#A function that prints a specific day depending on the variables defined
def todays_date():
    #defining varables
    day_of_week = "Tuesday"
    month = "January"
    day_of_month = "30th"
    year = "2024"
    print(day_of_week + ", "+ month + " " + day_of_month + ", " + year)

todays_date()

######## exercise 2##############################################
#function to print the entire sentence including the since
def new_sentence():
    print("""The newscaster said, "And Now for Something Completely Different!"\n \nOne quote: ', Two quotes “, Red Quotes, Blue Quotes""")
    
new_sentence()

######## exercise 3##############################################
#In the first print statement the 5 & 4 are strings so when you add them together you are adding the characters not adding the numerical quantity
def add_strings():
    print('5' + '4')
    
add_strings()

#In the second print statement the 5 & 4 are integers so when you add them, you are adding their numerical quantity thus printing out 9
def add_ints():
    print(5 + 4)
    
add_ints()

######## exercise 4##############################################
def convert_str_to_int():
    output = int('5') + int('4')
    print(output)
    
convert_str_to_int()

######## exercise 5##############################################
###A
def pemdas_A():
    outputA = ((5*5)/5)-5
    print(outputA)
    
pemdas_A()

###B
def pemdas_B():
    outputB = 5-((5**5)*5)
    print(outputB)

pemdas_B()

###C
def pemdas_C():
    outputC = (60-((40*1.5)+(5**2)))-25
    print(outputC)
    
pemdas_C()

######## exercise 6##############################################
##paying 543 cents using only quarters, nickels and pennies
def paying_543cents():
    #defining how many quarters will be needed using integer division to round down
    quarters = 543//25

    #defining how many nickels will be needed using the modulus to see how many cents are left to pay
    #additionally using integer division to see how many nickels would be needed the pay the remaining cents
    nickels = (543%25)//5

    #in addition to '(543%25)' which defines how many nickels will be needed '%5' is added to see the remaining cents left to pay after nickels are used
    pennies = (543%25)%5

    #prints out how many quarters, nickels & pennies needed to pay 543 cents
    print(quarters,'quarters',nickels,'nickels',pennies,'pennies')
    
paying_543cents()


######## exercise 7 & 8 ##############################################
#function with 3 parameters of numbers a user would input
def function_1(numA, numB, numC):
    #output converts all the inputs to floats just in case some of the paramerters are different types
    output = float(numA) + float(numB) + float(numC)
    
    #returns the average over the 3 numbers
    return(output)

#a print statement testing the function with different types of parameters
print(function_1(1, 6.2, "3"))

#function that prints out the user input once on one line then prints it 3 times on the same line
def function_2(user_input):
    print("You entered:")
    print(user_input)
    output = (user_input + " ") * 3
    return(output)

print(function_2("Hello There!"))

######## exercise 9 ##############################################
#function with 6 parameters that takes calculates two averages with function_1 & returns the sum of the two averages
def function_3(number1, number2, number3, number4, number5, number6):
    #a variable containing the average of the first 3 numbers
    first_half = function_1(number1, number2, number3)
    
    #a variable containing the average of the first 3 numbers
    second_half = function_1(number4, number5, number6)
    
    #a variable contianing the sum of the teo averages
    sum_of_averages = first_half + second_half

    return(sum_of_averages)

#prints statement testing if the new function_3 using function_1 from the eariler exercise works
print("With the number 2,4,6,8,10 & 12, the sum of the average of the first three numbers and last three is: ")
print(function_3(2,4,6,8,10,12))

######## exercise 10 ##############################################
#a function that computes a persons biorhythms using the amount of days (t) they have been alive
def bio_rhythm():
    #prompts the user to enter how old they are in days (t)
    print("Input how many days you have been alive:")
    t = int(input())

    #each variable uses the amount of days (t) and the conversion equation and also rounds each float to the nearest 2 decimal places
    physical = round(math.sin((2 * math.pi * t)/23), 2)
    emotional = round(math.sin((2 * math.pi * t)/28), 2)
    intellectual = round(math.sin((2 * math.pi * t)/33), 2)

    #prints out the users results depending on how many days (t) they are
    print("Your biorythm today is:")
    print("Physical: " + str(physical) + " Emotional: " + str(emotional) + " Intellectual: " + str(intellectual))

#calls the function
bio_rhythm()


    
    

