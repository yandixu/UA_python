from DrawingPanel import*
from random import*

#Yandi Xu
#CSC110, section:001K
#TProject 3, DrawingPanel progress
#This program using drawingpanel to drw graphics and take
# parameters define the stucture of graphics.

def main():
    #draw the background of graphic
    p = DrawingPanel(500,300,background="lavender")
    #define parameters
    step = int(input("How many steps have you walked? "))
    full = step//5000
    rem = step%5000//1000
    for i in range(0,full):
        flower(p)
    remainder(p,rem)

#This function take p as parameter to draw a whole height flower
# which occured with once 5000 step.
def flower(p):
    x = randint(25,475)
    p.fill_rect(x,300-120,5,120,"forestgreen")   #draw the stalk
    p.fill_oval(x-22.5,300-170,50,50,"lightcoral")    #draw the flower petals
    p.fill_oval(x-2.5,300-150,10,10,"lightpink")    #draw the eye of flower

    #this for loop take i as parameter to draw leaves in a whole length flower.       
    for i in range(1,6):
        p.draw_line(x-10,300-(20+20*(i-1)),x,300-(10+20*(i-1)),
                    color="forestgreen",width=5)
        p.draw_line(x+5,300-(20+20*(i-1)),x+15,300-(30+20*(i-1)),
                    color="forestgreen",width=5)
        
#This function take rem and p as parameters to draw a flower
# which height and the number of leaves were both defines on
# the remindar.
def remainder(p,rem):
    x = randint(25,475)
    p.fill_rect(x,300-(20+rem*20),5,120,"forestgreen")   #draw the stalk
    p.fill_oval(x-22.5,300-(20+rem*20+50),50,50,"lightcoral")    #draw the flower petals
    p.fill_oval(x-2.5,300-(20+rem*20+30),10,10,"lightpink")    #draw the eye of flower

    #this for loop take i and rem as parameter
    # to draw leaves in a flower which height defined by rem. 
    for i in range(1,rem+1):
        p.draw_line(x-10,300-(20+20*(i-1)),x,300-(10+20*(i-1)),
                        color="forestgreen",width=5)
        p.draw_line(x+5,300-(20+20*(i-1)),x+15,300-(30+20*(i-1)),
                        color="forestgreen",width=5)
               
main()
