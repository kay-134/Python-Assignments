#importing the turtle module and the random module
import turtle
import random


#the two lists of coordinates
coord_list_1 = [[-200,200],[-200,90],[-50,-20]]
coord_list_2 = [[50,200],[50,170],[300,90],[50,30],[50,0],[50,-13],[50,-73]]

#a function to create the bipartite_graph
def bipartite_graph(list_1, list_2):

    #for each point in the forst list
    for point in list_1:

        #for each point in the second list
        for other_point in list_2:

            #each point in the first list is drawn to a point in the second list
            turtle.penup()

            #goes to a point from the first list
            turtle.setposition(point[0],point[1])

            #draws from the forst point to the second point
            turtle.pendown()
            turtle.setposition(other_point[0],other_point[1])

#running the list with the the sample coordinate lists inputted
bipartite_graph(coord_list_1, coord_list_2)
