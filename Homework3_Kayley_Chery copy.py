import math

######## Part 1##############################################
###Exercise 1###
def number_identifier(num):
    #an if statement that prints "even" if the number module 2 equals 0 (when the number is even)
    if num % 2 == 0:
        print("even")

    #prints "odd" if the number module 2 equals 1 (happens when the number is odd)
    else:
        print("odd")

    #an if statement that prints "divisible" if the number module 2 equals 0 (when the number is even)
    if num % 3 == 0:
        print("divisible by 3")

    #an if statement that prints "zero" if the number arguement passed in the function equals zero
    if num == 0:
        print("zero")

#testing the function
number_identifier(3)

###Exercise 2###
def divisible_by_three(newNum):
    #a boolean variable that holds the status of the number whether it meets the two conditions or not
    meetsCondition = False

    #if the number is divisible by 2 and not divisible by 3, the value of the variable meetsCondition becomes true and is printed
    if newNum % 2 == 0 & newNum % 3 !=0:
        meetsCondition = True
        
        print(meetsCondition)

    #if the number is not divisible by 2 and is divisible by 3, the value of the variable meetsCondition becomes true and is printed
    if newNum % 2 == 1 & newNum % 3 == 0:
        meetsCondition = True
        
        print(meetsCondition)

    #if the number does not meet either condition, the value of the variable meetsCondition stays False and is printed
    else:
        print(meetsCondition)
        
##testing the function
divisible_by_three(4)

###Exercise 3###
#creating a function to print out the truth column results
def generate_truth_row(p,q):
    
    #initializing the p and q column
    if p == True:
        other_p = str(True) + "       "
        
    else:
        other_p = str(False) + "      "

    if q == True:
        other_q = str(True) + "       "
        
    else:
        other_q = str(False) + "      "

    #creating variables for each column
    p_equals_q = str(False) + "      "
    p_not_equals_q = str(False) + "      "
    p_and_q = str(False) + "      "
    p_or_q  = str(False) + "      "
    not_p   = str(True) + "      "
    
    #creating the p == q column
    if p == q:
        p_equals_q = str(True) + "       "

    #creating the p!=q column
    else:
        p_not_equals_q = str(True) + "       "

    #creating the p and q column
    if p and q:
        p_and_q = str(True) + "       "

    #creating the p or q column
    if p == True or q == True:
        p_or_q  = str(True) + "       "

    #creating the not p column    
    if p == True:
        not_p = str(False) + "       "

        
    print(other_p + other_q + p_equals_q + p_not_equals_q + p_and_q + p_or_q + not_p)
   


def generate_truth_table():
    print("p          q          p==q       p!=q       p and q    p or q     not p")
    generate_truth_row(False,False)
    generate_truth_row(False,True)
    generate_truth_row(True,False)
    generate_truth_row(True,True)

generate_truth_table()
    
    
######## Part 2##############################################
#a function that evaluates the answers for questions during decision tree
#making sure that a user only uses y or n for answers
def answer(string):
    the_answer = input(string)
    if the_answer == "y":
        return (True)

    elif the_answer == "n":
        return (False)

    else:
        print("Re-run the program only using 'y' or 'n' for yes and no answers in order to run through the decision tree!")

#a function that gives the user a list of the 11 main undergrad colleges at NYU and asks them a series of questions to determine which college they were thinking about when asnwering the questions
def find_the_undergrad_college():

    #the starting message
    start = "Did you know that NYU has 11 major undergrad colleges within NYU? \n I didn't know, either way here are the main 11 undergrad schools: "
    
    #variables for all the colleges
    cas = "College of Arts and Science"
    dentistry = "College of Dentistry"
    courant = "Courant Institute of Mathematical Sciences"
    gallatin = "Gallatin School of Individualized Study"
    sps = "School of Professional Studies"
    silver = "Silver School of Social Work"
    steinhardt = "Steinhardt School of Culture, Education, and Human Development"
    stern = "Stern School of Buisness"
    tandon = "Tandon School of Engineering"
    tisch = "Tisch School of the Arts"
    nursing = "Rory Meyers College of Nursing"

    #a list of colleges that a user can choose from to choose a college to use for the guessing game
    list_of_colleges = " -" + cas + " \n" + " -" + dentistry + " \n" + " -" + courant + " \n" + " -" + gallatin + " \n" + " -" + sps + " \n" + " -" + silver + " \n" + " -" + steinhardt + " \n" + " -" + stern + " \n" + " -" + tandon + " \n" + " -" + tisch + " \n" + " -" + nursing

    #the message that will intro the questionnarie
    part_2 = "Now mentally choose one college and answer the following questions using 'y' or 'n' as they pertain to the college you choose! Let's get started!"

    #starting question
    start_with_t = "Does the name start with a T?"

    #additional questions asked
    in_brooklyn = "Are their classes primarily in Brooklyn?"
    school_in_medicine = "Is the college primarily known for their medicine/health specific classes?"
    healthy_teeth = "Does this college focus on the training of students to identify healthy teeth?"
    start_with_s = "Does the name start with S?"
    create_major = "Is this college known for allwoing students to create their own major?"
    music_related = "Does this school have extensive music related majors?"
    comp_sci_and_math = "Is this school known for it's undergrad comp sci/mathematics program?"
    buisness_related = "Does this school focus on buisness realted majors?"
    social_work = "Is this school known for their classes in social work?"

    #revealing answer
    revealing_the_college = "You were thinking of: " 
    
    print(start)
    print(list_of_colleges)
    print(part_2)

    #if the school name starts with a t
    if answer(start_with_t):

        #if the school is also in Brooklyn
        if answer(in_brooklyn):

            #revealing the answer -> Tandon
            print(revealing_the_college + tandon)

        #if the school is not in Brooklyn but starts with T
        else:
            print(revealing_the_college + tisch)
            
    #if the name does not start with a t
    else:
        
        #if a school is know for their medical practice
        if answer(school_in_medicine):

            #if a school focuses on the training of students to identify healthy teeth
            if answer(healthy_teeth):
                print(revealing_the_college + denstistry)

            #if the school does not primarily focus on training students to identify healthy teeth but is a medical school
            else:
                print(revealing_the_college + nursing)

        #if a school is not known for their medical practice
        else:

            #if a school starts with an s
            if answer(start_with_s):

        

                #if a school has music related majors
                if answer(music_related):
                    print(revealing_the_college + steinhardt)

                #if a school doesn't primarily have music related majors
                else:

                    #if the school does focus on buisness related majors
                    if answer(buisness_related):
                        print(revealing_the_college + stern)

                    #if a school does not focus on buisness related majors
                    else:

                        #if this school is known for their classes in social work
                        if answer(social_work):
                            print(revealing_the_college + silver)

                        #if the school is not known for their classes in social work
                        else:
                            print(revealing_the_college + sps)

            #if a school does not start with an s
            else:

                #if you can make your own major in this school
                if answer(create_major):
                    print(revealing_the_college + gallatin)

                else:

                    #if a school is known for their comp sci/math program
                    if answer(comp_sci_and_math):
                        print(revealing_the_college + courant) 

                    #if a school is not known for their comp sci/math program
                    else:
                        print(revealing_the_college + cas) 
                
            
        
    
    
    
find_the_undergrad_college()   
