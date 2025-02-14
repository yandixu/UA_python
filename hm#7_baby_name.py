#Yandi Xu
#CSC 110, Section: 001k
#Project #7: Baby Name
#This program has used two input files, based on the parameter form these
# two files, a histogram has been drawed. 

START = 1890 #the start year.
WIDTH = 60 #the width of each decade.
HEIGHT = 30 #the height of gray recetangle.

from DrawingPanel import*
def main():
    intro()
    name = input("Name : ").lower()  #the name tha the user searched for.
    gender = input("Gender : ").lower() # the gender the user searched for.
    search_name = search("names.txt",name,gender)

    #this if/else is used to judge whether the name inputed is exist.
    if len(search_name)>0:
        print(search_name)
        meaning = search("meanings.txt",name,gender)
        print(meaning)
        p = DrawingPanel(780,560,background = "white")
        basic(p,meaning)
        graph(p,search_name)
    #if not exist, a "not found" string will be printed.
    else:
        print("'",name,"'","not found.")

#This function is used to print the intro of whole program.    
def intro():
    print("This program allows you to search through the")
    print("data from the Scoial Security Administration")
    print("to see how popular a particular name has been\nsince 1890.")
    print()

#This function has used if/else, and for loop to return the string
#Parameter: filename:the name of file that inputed.
#           name: the name user searched for.
#           gender: the gender user searched for.
#Return: if both name and gender found, the specfic line will be returned.
#else it will return a blank string.
def search(filename,name,gender):
    lines = open(filename).readlines()
    for line in lines:
        nline = line.lower().split()
        if (name == nline[0] and gender == nline[1]):
            return line.strip()
    return "" 
    print()

#This function is used to draw gray rectangle at the top and bottom, the balck
# lines with them, and add the meaning string into the top gray rectangle.
#Parameter： p：the background of drawingpanel
#            meaning： the meaing of name.
def basic(p,meaning):
    p.fill_rect(0,0,780,HEIGHT,"light gray")
    p.fill_rect(0,530,780,HEIGHT,"light gray")
    p.draw_line(0,HEIGHT,780,HEIGHT,"black")
    p.draw_line(0,560-HEIGHT,780,560-HEIGHT,"black")
    p.draw_string(meaning,0,0)

#This function ha sused if/else and for loop to draw the histogram.
#Parameter: p: the background of drawingpanel.
#           search_name: a string return from search().
def graph(p,search_name):
    bottom = search_name.split()
    rank = bottom[2:] #idendify a list of ranks in different decades.
    gender = bottom[1] #idetify the gender.

    #this if/else is used to define the color of histogram changed by gender.
    if "m" in gender:
        color = "green"
    else:
        color = "yellow"

    #in this for loop, the y-coor changed by the rank.
    for i in range(len(rank)):
        if int(rank[i]) == 0:
            y = 560-HEIGHT
        elif int(rank[i]) == 1:
            y = HEIGHT           
        else:
            y = int(rank[i])//2+HEIGHT
            
        p.fill_rect(i*WIDTH,y,30,530-y,color) #draw the histogram
        p.draw_string(START+i*10,WIDTH*i,530) #add the decaed at bottom
        p.draw_string(rank[i],i*WIDTH,y-10) #add rank# to the top of each gram.

main()        
