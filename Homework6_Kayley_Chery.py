##importing libraries/modules
import math

###Exercise 1##########################################################
#Write a function that takes a string as an argument parameter and returns a new string consisting of numbers divided by spaces
def secret_Code(code):

    #sets the input from the user as a string to use in the function
    new_string = code

    #creates an empty string that can hold the outputted string that has all the numbers that represent the inputed string when using the ord function
    output = ""

    #a for loop that cycles through every letter of the inputted string
    for char in new_string:

        #for every letter that is converted into a number, it is added to the output string
        output = output + str(ord(char))+ " "
   
    #the output string with all the letters converted to numbers is printed out
    print(output)

#testing the word "cat" to see if the function works
secret_Code("cat")


###Exercise 2##########################################################
#A program that take a single word as input, modifying it as appropriate, and adding ing to the end of the word
def adding_Ing(word):

    #converts all the letters in the inputted string to lowercase
    lower_word = word.lower()

    #a variable that holds the quanitative last index of a string ex. if a string is 4 letters, the last index is 3 
    length = len(word) - 1

    #an empty string that holds the value of the word when "ing" is added to it
    new_word = " "
    
    #an if statement that checks if the word inputted ends with "it" like "sit" it adds an extra "t" to the word before adding "ing"
    if word[length] == "t" and word[length-1] == "i" :
        new_word = word + word[length] + "ing"

    #if a word ends in "te" like "write" it removes the e and adds "ing" 
    elif word[length] == "e" and word[length-1] == "t" :
        new_word = word[0:length] + "ing"
        
    #if the word ends in "ie" like "die" it removes the "ie" and adds "ying"
    elif word[length] == "e" and word[length-1] == "i" :
        new_word = word[0:length - 1] + "ying"

    #if the word ends in "ic" like "panic" it adds "king"
    elif word[length] == "c" and word[length-1] == "i" :
        new_word = word + "king"

    #if the word ends in "et" like "forget" it adds "ting"
    elif word[length] == "t" and word[length-1] == "e" :
        new_word = word + "ting"

    #if the word doesn't meet any of the earlier conditions, "ing" is just added to the end of the word
    else:
        new_word = word + "ing"

    #the new word is printed out
    print(new_word)

#testing a couple of words
adding_Ing("sit")
adding_Ing("seat")
adding_Ing("write")
adding_Ing("sleep")
adding_Ing("fly")
adding_Ing("flee")
adding_Ing("stomp")
adding_Ing("be")

###Exercise 3##########################################################
def wordToInt(phrase):

    input_phrase = phrase
    
    ##Part 1: Making a list of numbers
    def make_list_of_nums(input_phrase):
        
        ##1. adding a function that returns an integer for the word of a number inputted
        def word_to_number(word):
            if word == 'one':
                return(1)
            elif word == 'two':
                return(2)
            elif word == 'three':
                return(3)
            elif word == 'four':
                return(4)
            elif word == 'five':
                return(5)
            elif word == 'six':
                return(6)
            elif word == 'seven':
                return(7)
            elif word == 'eight':
                return(8)
            elif word == 'nine':
                return(9)
            elif word == 'ten':
                return(10)
            elif word == 'eleven':
                return(11)
            elif word == 'twelve':
                return(12)
            elif word == 'thirteen':
                return(13)
            elif word == 'fourteen':
                return(14)
            elif word == 'fifteen':
                return(15)
            elif word == 'sixteen':
                return(16)
            elif word == 'seventeen':
                return(17)
            elif word == 'eighteen':
                return(18)
            elif word == 'nineteen':
                return(19)
            elif word == 'twenty':
                return(20)
            elif word == 'thirty':
                return(30)
            elif word == 'forty':
                return(40)
            elif word == 'fifty':
                return(50)
            elif word == 'sixty':
                return(60)
            elif word == 'seventy':
                return(70)
            elif word == 'eighty':
                return(80)
            elif word == 'ninety':
                return(90)
            elif word == 'hundred':
                return(100)
            elif word == 'thousand':
                return(1000)
            elif word == 'million':
                return(1000000)
            elif word == 'billion':
                return(1000000000)

        
        ##2.Splitting the input by spaces (using the "split" method), creating a list of words
        new_phrase = input_phrase.split( )

        ##3.Use the word_to_number function in number_program_input.py to create a list of integers from the list of words
        
        #3.1 Initializing an empty list to hold the number form of all the seperate words
        list_of_numbers = []

        #3.2 For each word in the list, convert it to an integer and add that integer to the list_of_number 
        for word in new_phrase:

            #3.3 Making sure that for every word inputted in the function to get the number form of the word, the word itself is lowercase
            new_int = word_to_number(word.lower())
            list_of_numbers.append(new_int)

        #can use this line to test the list of numbers
        #print(list_of_numbers)
        
        #returns the list of numbers
        return(list_of_numbers)
    
        
    
    #creates a global variable that can be used for the next fuction that holds the numbered list
    numbered_list = make_list_of_nums(input_phrase)
    
    ##Part 2: Combine numbers less than 1000
    def combine_numbers_less_than_1000(numbered_list):

        #creates a vaibale to take the numbered listed inputted in the function to use for other parts of the problem
        list_to_be_sorted = numbered_list

        #a variable to hold the combined list
        combined_list = []

        #a variable to hold the previous item value in the list
        hold = 0

        #a variable to count the index of the list
        i = 0
        
        #for every number in the list to be sorted
        for number in list_to_be_sorted:
            
            #if the number is less than 1000 
            if number > 999:

                #if hold is greater than 0
                if hold > 0:

                    #add the hold value to the combined list
                    combined_list.append(hold)

                #also add the current number to the combined list
                combined_list.append(number)

                #set hold to zero
                hold = 0
            
            #if hold equals zero
            elif hold == 0:

                #the value of hold becomes the number
                hold = number

            #if the current number is greater than the hold value
            elif number > hold:

                #the value becomes the product of hold and the current number
                hold = hold * number

            #otherwise the value of hold and the current number are appended to the the combined list
            else:
                combined_list.append(hold)
                combined_list.append(number)

                #the value of hold is set to zero
                hold = 0
                
        #if hold is greater than zero at the end of the for loop
        if hold > 0:

            #the value of hold is appended to the combined list
            combined_list.append(hold)

        #can use this line to test the combined list of numbers  
        #print(combined_list)

        #return the value of the combined list
        return(combined_list)
    
    #a global variable is set within the function that holds the value of the combined list   
    complied_list = combine_numbers_less_than_1000(numbered_list)
    
    ##Part 3: Combine numbers less than 1000
    def add_numbers_less_than_100(complied_list):

        #creates a list to hold the unadded list to be modified within the function
        unadded_list = complied_list

        #creates a list that holds the numbers with numbers less than 1000 between numbers that are greater than 1000 to be added to each other
        added_list = []
        
        #a variable to hold the previous item value in the list
        new_hold = 0

        #a variable to count the index of the list
        i = 0

        #for each number in the list of unadded numbers
        for number in unadded_list:
            
            #if the number is greater than 999 
            if number > 999:

                #if hold = 0
                if new_hold > 0:

                    #the hold number is appended to the new list
                    added_list.append(new_hold)

                #the current number is added to the new list of added numbers
                added_list.append(number)

                #the hold value is set to 0
                new_hold = 0
            
            #if the hold number equals 0
            elif new_hold == 0:

                #the hold number is set to the value of the current number
                new_hold = number

            #if the current number is less than the value of the hold number
            elif number < new_hold:

                #the hold is set to the sum of the hold + the current number
                new_hold = new_hold + number

            #otherwise the hold value and the current number values are added to the new list 
            else:
                added_list.append(new_hold)
                added_list.append(number)

                #the hold value is set to 0
                new_hold = 0

        if new_hold > 0:
            added_list.append(new_hold)

    #can be used to test the combined list of numbers  
    #print(added_list)

        #returns the value of the list with some number that were added together
        return(added_list)
    
    #testing the fucntion
    add_numbers_list = add_numbers_less_than_100(complied_list)

    ##Part 4: Combine numbers greater than 999 with numbers 999 or less
    def add_numbers_greater_than_999(add_numbers_list):
        
        #creates a list to hold the unmultiplied list to be modified within the function
        unmultiplied_list = add_numbers_list

        # 
        multiplied_list = []
        
        #a variable to hold the previous item value in the list
        hold_to_multiply = 0

        #a variable to hold the sum of all the numbers
        sum_of_numbers = 0

        #a variable to count the index of the list
        x = 0

        #a variable to count the index of the list
        i = 0

        #for 
        for number in unmultiplied_list:

            if number < 1000:

                hold_to_multiply = number

                #if the for loop is at the last index of the list
                if i == len(unmultiplied_list) - 1:

                    #add the last number in the list to the combined list
                    multiplied_list.append(number)

            else:
                 multiplied_list.append(hold_to_multiply*number)
                 hold_to_multiply = 0
                 
            i = i + 1

        sum_of_numbers = sum(multiplied_list)
        #can be used to test the combined list of numbers
        #print(multiplied_list)
        print(sum_of_numbers)

        return(multiplied_list)
                
    add_numbers_greater_than_999(add_numbers_list) 

print("Five hundred million two hundred three thousand seventeen")    
wordToInt("Five hundred million two hundred three thousand seventeen")

print("One billion seventy three")
wordToInt("One billion seventy three")

print("One hundred ninety two thousand seven hundred thirty one")  
wordToInt("One hundred ninety two thousand seven hundred thirty one")
