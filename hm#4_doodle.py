#Yandi Xu
#CSC110, Section:001K
#Project 4: Doodle
#This project has using drawingoanel to draw
# a fish. 

from DrawingPanel import*

def main():
    p = DrawingPanel(300,300,background = "papayawhip")
    p.draw_line(150,50,100,150,color="pink",width = 3)
    p.draw_line(150,50,200,150,color="pink",width = 3)
    p.draw_line(150,250,100,150,color="plum",width = 3)
    p.draw_line(150,250,200,150,color="plum",width = 3)
    p.fill_rect(125,250,50,30,"violet")
    p.fill_oval(140,70,20,20,"lightcoral")

main()
