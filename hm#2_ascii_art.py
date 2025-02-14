#Yandi Xu,
#CSC 110,Fall 2017,Section: 01K
#ASCii_art

#This program's behavior is to using for loops to create a ASCii-art image.
def main():
    body ()
    line ()
    rebody ()

#function1 output a head and first half of body of a fish
def body ():
 for line in range(1,5):
    for space in range(1,-line+6):
        print(" ",end="")
    for slash in range(1,line+1):
        print("/\\",end="")
    for space in range(1,-line+6):
        print(" ",end="")
    print()
    
#funcion2 output a middle line of a fish
def line ():
 for plus in range(1,4):
    print("|+~",end="")
 print("|")

#function3 output a tail and the rest half bodyof a fish
def rebody ():
 for line in range(4,0,-1):
    for space in range(1,-line+6):
        print(" ",end="")
    for slash in range(1,line+1):
        print("/\\",end="")
    for space in range(1,-line+6):
        print(" ",end="")
    print()


main ()
