# Yandi XU
# CSC 110, Section: 001k
# Project #10: Fire
# This Project has used lists of lists and drawingp anel
# to predict the spread of fire. 

from DrawingPanel import*
import random
grid=[]
new_grid=[]
def main():
    #fire = "red"
    p = DrawingPanel(130,130,"white")
    get_grid()
    get_color(p)
    #color_list = get_color(p,grid)
    #draw_fire(p,color_list)

   # for i in range(len(color_list)):
      #  for j in range(len(color_list)):
         #   if fire in color_list[i][j]:
         #       rebuild(p,color_list)
               # draw_fire(p,color_list)

    
def get_grid():
    lines = open("one.txt").readlines()
    for i in range(len(lines)):
        grid.append([])
        line = lines[i].split()
        for j in range(len(line)):
            grid[i].append(line[j])
   # return grid

def get_color(p):
    #color_list = []
    for r in range(len(grid)):
       # color_list.append([])
        for c in range(len(grid[r])):
            if grid[r][c] == "0":
                color = "yellow"
            elif grid[r][c] == "1":
                color = "green"
            else:
                color = "red"
            p.fill_rect(r*10,c*10,10,10,color)
    #return color_list

def new_grid():
    pass
                                     
def rebuild():
    for r in range(1,len(grid)):
        for c in range(1,len(grid[r])):
            if grid[r][c] == "green":
                percent=random.randint(1,100)
                if percent < 75 and (grid[r+1][c]=="red" or grid[r-1][c]=="red" or
                                     grid[r][c+1]=="red" or grid[r][c-1]=="red" ):
                    new_grid[r][c] = "red"          
            else:
                new_grid[r][c] = "yellow"
   
                

    


main()
