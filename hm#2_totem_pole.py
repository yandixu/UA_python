#Yandi Xu
#CSC 110, Section 001K
#Project 2_b,Totem Pole

#This is project is write to build a combined totem symbol
# by using expression and parameter in each function,
# and for loops in some specfic functions to print a totem pole.
 
size = 3 #Define the parameter"size" which used in whole program.

def main():
    slash_combo()
    face1()
    number(6)
    quotation("\\")
    face2()
    number(5)
    totem_1()
    totem_2(4," ","/",":","\\"," ")
    totem_2(4,"'","-",":","-","'")
    laugh()
    number(4)
    quotation("/")
    face1()
    number(3)
    cat_head()
    number(2)
    totem_1()
    letters()
    number(1)
    quotation("|")
    endingpart()
    
#This fuction take size as parameter, using for loops to
# print a combo of slash and back slash. Basic expression
# also has been used in this function
def slash_combo():
    print(" "*7,end="")
    for i in range(1,size+2):
        print("\\",end="")
    for i in range(1,size+2):
        print("/",end="")
    print()

#This function use size as parameter and expression based on size.    
def face1():
    print(" "*8,end="")
    print("|"+" "*(size-3)+".)(."+" "*(size-3)+"|")
    print(" "*8,end="")
    print("|"+" "*(size-2)+"||"+" "*(size-2)+"|")
    print(" "*8,end="")
    print("\\"+" "*(size-3)+"(__)"+" "*(size-3)+"/")

#This function take the begin number and size as pararmeters
# to print the loop of numbers with the change
# of begining number.
def number(begin):
    print(" "*8,end="")
    for i in range(0,size):
        print((begin+i)%10,end="")
    for i in range(size-1,-1,-1):
        print((begin+i)%10,end="")
    print()

#This function take a character and size as parameters to
# print a combo of quotation marks and char.
def quotation(char):
    print(" "*8,end="")
    print(">"*size,end="")
    print("<"*size)
    print(" "*8,end="")
    print(char*size*2)

#This function take size as parameter to print another part
# of totem ehihc looks like a face。
def face2():
    print(" "*8,end="")
    print("(0)"+" "*(size-3)*2+"(0)")
    print(" "*8,end="")
    print("|"+" "*(size-2)+"/\\"+" "*(size-2)+"|")
    print(" "*8,end="")
    print("("+" "*(size-2)+"()"+" "*(size-2)+")")

#This is fuction use different expression in each line by
# taking size as parameter to print the first main part of totem.
def totem_1():
    print(" "*8,end="")
    print("|"+" "*(size-3)+"-..-"+" "*(size-3)+"|")
    print(" "*8,end="")
    print("|"+" "*(size-3)+"o\\/o"+" "*(size-3)+"|")
    print(" "*3,end="")
    print(".----\\"+" "*(size-1)*2+"/----.")
    print(" "*2,end="")
    print("/ "*3+"|"+"~"*(size-1)*2+"|"+" \\"*3)

#This function has 6parameters which 2 are numbers and the other
# 4 are characters to print the rest main part of totem.
# For loops and expression also been used in here.
def totem_2(turn,char1,char2,char3,char4,char5):
    for i in range(0,turn):
        print(char1+char2,end="")
    print("|",end="")
    print(char3*(size-1)*2,end="")
    print("|",end="")
    for i in range(0,turn):
        print(char4+char5,end="")
    print()

#Print a laugh emoji by using parameter size.        
def laugh():
    print(" "*7,end="")
    print("("*size+"^^"+")"*size)

#Print a cat head by using parameter size.
def cat_head():
    print(" "*8,end="")
    print("/\\"+"-"*(size-2)*2+"/\\")
    print(" "*7,end="")
    print("("+" "*(size-2)+".  ."+" "*(size-2)+")")

#Print a 4 lines symbol which consits of letters and slash.
def letters():
    print(" "*7,end="")
    print("(\\"+" "*(size-1)*2+"/)")
    print(" "*6,end="")
    print("( |"+"v"*(size-1)*2+"| )")
    print(" "*6,end="")
    print("( |"+"v"*(size-1)*2+"| )")
    print(" "*9,end="")
    print("T"+" "*(size-2)*2+"T")
    
#This function takes size as parameter and use expression
# to print the rest 7 lines of the whole totem pole. 
def endingpart():
    print(" "*8,end="")
    print("(o)"+" "*(size-3)*2+"(o)")
    print(" "*8,end="")
    print("|"+" "*(size-2)+"/\\"+" "*(size-2)+"|")
    print(" "*8,end="")
    print("("+"="*(size-1)*2+")")
    print(" "*8,end="")
    print("|"+"_"*(size-2)+"/\\"+"_"*(size-2)+"|")
    print(" "*8,end="")
    print("("+"_"*(size-2)+"/\\"+"_"*(size-2)+")")
    print(" "*7,end="")
    print("_|"+"_"*(size-2)+","+"_"*(size-1)+"|_")
    print(" "*6,end="")
    print("("+"_"*size+"\\"+"_"*(size+1)+")")
    
main()
