#Yandi Xu,
#CSC110, Section: 001K
#Project 4: Cafe Wall
#This program is to use for loop and DrawingPanel to draw a "cafewall".

from DrawingPanel import*

def main():
    p = DrawingPanel(650,400,background="gray")
    single_row(p,0,0,20,4)
    single_row(p,50,70,30,5)
    grid(p,10,150,25,4,0,8)   #the lower left grid
    grid(p,250,200,25,3,10,6)   #the lower middle grid
    grid(p,425,180,20,5,10,10)   #the lower right grid
    grid(p,400,20,35,2,35,4)   #the upper right grid
       
def single_row(p,x,y,size,pairs):
    for i in range(0,pairs):
        p.fill_rect(x+2*i*size,y,size,size,"black")
        p.draw_line(x+2*i*size,y,x+(2*i+1)*size,y+size,"blue")
        p.draw_line(x+(2*i+1)*size,y,x+2*i*size,y+size,"blue")
        p.fill_rect(x+(2*i+1)*size,y,size,size,"white")
        p.fill_rect(x+2*i*size,y,2*size,2,"gray") # add the mortar

def grid(p,x,y,size,pairs,offset,row):
    for i in range(0,row):
        single_row(p,x+offset*(i%2),y+(i-1)*size,size,pairs)

main()

