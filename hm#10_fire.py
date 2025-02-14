# Yandi XU
# CSC 110, Section: 001k
# Project #10: Fire
# This Project has used lists of lists and drawing panel
# to predict the spread of fire. 

LENGTH = 10 #the height and width of each rectangle.
TIME = 100  #the time silent between each two drawing panel.

from DrawingPanel import*
from random import*
def main():
    fire = "red"
    grid = get_grid() #get original lists of lists.
    p = DrawingPanel(130,130,"white")  
    
    color_list = get_color(p,grid)  #define the color of rects by original grid.
    draw_fire(p,color_list)

    for i in range(len(color_list)):
        for j in range(len(color_list)):
            #while there is red color in color list, do the rebild of grid.
            while fire in color_list[i][j]:
                rebuild(color_list)
                draw_fire(p,color_list)

#This function is used to get the original lists of lists.
#Return: grid: the lists of lists.
def get_grid():
    grid = []
    lines = open("one.txt").readlines()  #open goal file and read it.
    for i in range(len(lines)):
        grid.append([])
        line = lines[i].split()
        for j in range(len(line)):
            grid[i].append(line[j])
    return grid

#This function is used to get a color grid from original grid.
#Parameter: p: the background of drawing panel.
#           grid: the origianl grid from get_grid function.
#Return: color_list: a grid of colors.
def get_color(p,grid):
    color_list = []
    for r in range(len(grid)):
        color_list.append([])
        for c in range(len(grid[r])):
            #decide the color by the number.
            if grid[r][c] == "0":
                color = "yellow"
            elif grid[r][c] == "1":
                color = "green"
            elif grid[r][c] == "2":
                color = "red"
            color_list[r].append(color)
            
    return color_list
                
#This function used p and color_list to draw rectangles.
#Parameter: p: the background of drawing panel.
#           color_list: a grid of colors.
def draw_fire(p,color_list):
    p.clear()  #clear the previous drawingpanel to redarw. 
    for r in range(len(color_list)):
        for c in range(len(color_list[r])):
            color = color_list[r][c]
            p.fill_rect(r*LENGTH,c*LENGTH,LENGTH,LENGTH,color)
    p.sleep(TIME)  #silent between each two redraw.
    
#This function used ranodm number to rebuild the color_list
# and to show the tendency fo fire.
#Parameter: color_list: a grid of colors.   
def rebuild(color_list):
    for r in range(1,len(color_list)):
        for c in range(1,len(color_list[r])):
            if color_list[r][c] == "green":
                percent = randint(1,100) #take random number between 1 and 100.
                # if random number smaller than 75 and there's red in
                # its neighbour, the color will change to red.
                if percent <= 75 and (color_list[r+1][c]=="red" or
                                      color_list[r-1][c]=="red" or
                                      color_list[r][c+1]=="red" or
                                      color_list[r][c-1]=="red"):
                    color_list[r][c] = "red"
            else:
                color_list[r][c] = "yellow"

main()
