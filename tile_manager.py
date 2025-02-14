# Yandi Xu
# CSC110, Section : 001K
# Project: Tiles Manager
# This graphical project allows users to clike on drawingpanel to add/delete and
# rearrange the order of randomly occured rectangular tiles. 

from DrawingPanel import*
from random import*

WIDTH = 400  #the width of drwaingpanel
HEIGHT = 400  #the height of drawingpanel
NOTILES = 50  #the number of tiles randomoccured one imte
TMIN = 25  #the min-length of tile
TMAX = 60  #the max-length of tile
COLOR = 255  #the max of RGB number used to define color

p = DrawingPanel(WIDTH,HEIGHT,"white")  # define the background size and color.
tiles = []  # list sort the parameter fo tiles.

#This function is used to add a tile when user press n.
#event: this parameter represents the mouse click that happened
# and prompted function to be called.
def add(event):
    draw_all()

#This function is used to add 50 tiles randomly when program start.
def add_all():
    for i in range(NOTILES):
        draw_all()
        
#This function is used to draw tile un the tiles list.
# Size, position and color of each tile are random.       
def draw_all():
    width = randint(TMIN,TMAX)
    height = randint(TMIN,TMAX)
    x = randint(0,WIDTH-width)
    y = randint(0,HEIGHT-height)
    color = (randint(0,COLOR),randint(0,COLOR),randint(0,COLOR))    
    tile = (x,y,width,height,color)
    draw_single(tile)
    tiles.append(tile)

#This is a helper function to draw single tile each time.
#Parameter: tile: the tuple in the list contain all parameters of single tile.
def draw_single(tile):
    p.fill_rect(tile[0],tile[1],tile[2],tile[3],tile[4])
    
#This is a helper function used to find the index of tile in list which
# satistify the mouse click.
# Parameter: x: event.x position when user click mouse.
#            y: event.y position when user click mouse.
#Return: goal_tiles: a list of the index of tuple satistify the mouse click.
def find_tiles(x,y):
    goal_tiles = []
    for i in range(len(tiles)):
        if tiles[i][0]< x and tiles[i][1] < y:
            if x < (tiles[i][0]+tiles[i][2]) and y < (tiles[i][1]+tiles[i][3]):
                goal_tiles.append(i)
    return goal_tiles
    
#This function will be called when user left-clicks.
#Topmost of the tiles touch the clicked position will be moved to the top.
#event: this parameter represents the mouse click that happened
# and prompted function to be called.
def raises(event):
    x = event.x
    y = event.y
    goal_tiles = find_tiles(x,y)
    #pop the last satisfied tuple from list and insert it to the end of list.
    if len(goal_tiles) > 0:
        tiles.append(tiles.pop(goal_tiles[-1]))
    tile = tiles[-1]
    draw_single(tile)

#This function will be called when user right-clicks.
#Topmost of the tiles touch the clicked position will be moved to the bottom.                
#event: this parameter represents the mouse click that happened
# and prompted function to be called.
def lower(event):
    x = event.x
    y = event.y
    goal_tiles = find_tiles(x,y)
    #pop the last satisfied tuple from list and insert it to the start of list.
    if len(goal_tiles) > 0:
        tiles.insert(0,tiles.pop(goal_tiles[-1]))
    tile = tiles[-1]
    draw_single(tile)

#This function will be called when user Shift-left-clicks.
#Topmost of the tiles touch the clicked position will be remove from screen.
#event: this parameter represents the mouse click that happened
# and prompted function to be called.
def delete(event):
    x = event.x
    y = event.y
    goal_tiles = find_tiles(x,y)
    #pop the last satisfied tuple from list.
    if len(goal_tiles) > 0:
        tiles.pop(goal_tiles[-1])
    p.clear()   #clear all tiles from screen
    for tile in tiles:   #redraw tiles without the removed one
        draw_single(tile)

#This function will be called when user Shift-right-clicks.
#All of the tiles touch the clicked position will be removed from screen.
#event: this parameter represents the mouse click that happened
# and prompted function to be called.
def delete_all(event):
    x = event.x
    y = event.y
    goal_tiles = find_tiles(x,y)
    #pop all satisfied tuple from list.
    if len(goal_tiles) > 0:
        tiles.pop(goal_tiles[0])
        for i in range(1,len(goal_tiles)):
                tiles.pop(goal_tiles[i]-1)
    p.clear() #clear all tiles from screen
    for tile in tiles: #redraw tiles without the removed tiles.
        draw_single(tile)
    
#This function will be called when user press s.
#All tiles that currently on the screen will be moved to a new ranodm position.
#event: this parameter represents the mouse click that happened
# and prompted function to be called.
def shuffle(event):
    p.clear()  #clear all tiles from screen
    #redraw tiles by giving them a new ranodm x,y position.
    for tile in tiles:   
        width = randint(TMIN,TMAX)
        height = randint(TMIN,TMAX)
        x = randint(0,WIDTH-width)
        y = randint(0,HEIGHT-height)
        #create a new tuple by change x,y.
        new_tuple = (x,y,tile[2],tile[3],tile[4])
        draw_single(new_tuple)
        
    
    
    
