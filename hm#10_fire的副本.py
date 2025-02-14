# Yandi XU
# CSC 110, Section: 001k
# Project #10: Fire
# This Project has used lists of lists and drawingp anel
# to predict the spread of fire. 

from DrawingPanel import*
import random
def main():
    fire = "red"
    grid = get_grid()
    p = DrawingPanel(130,130,"white")
    
    color_list = get_color(p,grid)
    draw_fire(p,color_list)

    for i in range(len(color_list)):
        for j in range(len(color_list)):
            if fire in color_list[i][j]:
                rebuild(p,color_list)
                draw_fire(p,color_list)

    
def get_grid():
    grid = []
    lines = open("one.txt").readlines()
    for i in range(len(lines)):
        grid.append([])
        line = lines[i].split()
        for j in range(len(line)):
            grid[i].append(line[j])
    return grid

def get_color(p,grid):
    color_list = []
    for r in range(len(grid)):
        color_list.append([])
        for c in range(len(grid[r])):
            if grid[r][c] == "0":
                color = "yellow"
            elif grid[r][c] == "1":
                color = "green"
            elif grid[r][c] == "2":
                color = "red"
            color_list[r].append(color)
            
    return color_list
                
              
def draw_fire(p,color_list):
    for r in range(len(color_list)):
        for c in range(len(color_list[r])):
            color = color_list[r][c]
            p.fill_rect(r*10,c*10,10,10,color)
    p.sleep(100)
    
    
def rebuild(p,color_list):
    for r in range(1,len(color_list)):
        for c in range(1,len(color_list[r])):
            if color_list[r][c] == "green":
                percent=random.randint(1,100)
                if percent < 75 and (color_list[r+1][c]=="red" or color_list[r-1][c]=="red" or
                                     color_list[r][c+1]=="red" or color_list[r][c-1]=="red" ):
                    color_list[r][c] = "red"          
            else:
                color_list[r][c] = "yellow"
                

    


main()
