# Yandi Xu
# CS 120, Fall 18, Section: 01F
# Project#1: Word Search
# This program is used to searching words in a grid of letters,
# and prin the word out if it exists in grid.

def main():
    s,L = init()
    results = occurs_in(s,L)
    
    #print out the results list one word per row.
    for word in sorted(results):       
        print(word)
        
#This fucntion is used to get the name of input words file and grids file,
# and change these file in to lists.
#Return: s:the list words
#        L:the grid of letters
def init():
    s = []
    L = []
    wname = input()
    gname = input()

    words = open(wname).readlines()
    for word in words:
        word = word.strip().lower()
        s.append(word)

    grid = open(gname).readlines()
    for elem in grid:
        L.append(elem.strip().split())

    return s,L

#This function is used to check the existence of words in grid by L to R, R to L,
# T to B, B to T, and by diagional from TL to BR.
#Parameter: s:the list words
#           L:the grid of letters
#Return: results: a list stored rxisted words.
def occurs_in(s,L):
    #the start length of searching length is 3.
    pos = 3
    #create list to store words. 
    results = []
    
    #Searching the grid horizontally form Left to Right.
    for i in range(len(L)):
        for j in range(len(L[i])):           
            while j+pos <= len(L[i]):               
                str1 = "".join(L[i][j:j+pos])
                if str1 in s and str1 not in results:
                    results.append(str1)
                pos += 1
            pos = 3
    
                
    #Searching the grid horizontally form Right to Left.
    for i in range(len(L)):
        #reverse the grid per row to search.
        L[i].reverse()

    for i in range(len(L)):
        for j in range(len(L[i])):
            while j+pos <= len(L[i]):               
                str1 = "".join(L[i][j:j+pos])
                if str1 in s and str1 not in results:
                    results.append(str1)
                pos += 1
            pos = 3

    #Searching the grid vertically from top to bottom.
    line = [[0]]*len(L)
    j = 0
    
    for elem in L:
        elem.reverse()

    #while i and j both within the length-value.
    subline = []
    while j < len(L):
        for i in range(len(L)): 
            subline.append(L[i][j])
            line[j] = subline
        subline = []
        j += 1

    #Do the searching in new grid row by row.
    for i in range(len(line)):
        for j in range(len(line[i])):           
            while j+pos <= len(line[i]):               
                str1 = "".join(line[i][j:j+pos])
                if str1 in s and str1 not in results:
                    results.append(str1)
                pos += 1
            pos = 3
        
    #Searching the grid vertically from bottom to top.
    line = [[0]]*len(L)
    j = 0

    #create a new grid to convenience searching.
    subline = []
    while j < len(L):
        for i in range(len(L)-1,-1,-1): 
            subline.append(L[i][j])
            line[j] = subline
        subline = []
        j += 1

    #Do the searching in new grid row by row.
    for i in range(len(line)):
        for j in range(len(line[i])):           
            while j+pos <= len(line[i]):               
                str1 = "".join(line[i][j:j+pos])
                if str1 in s and str1 not in results:
                    results.append(str1)
                pos += 1
            pos = 3
            
    #Searching the grid by diagonal from top left to bottom right.
    for offset in range(-len(L),len(L),1): #set the offset
        if offset >= 0:
            i = 0
            j = offset
        else:
            i = -offset
            j = 0

        #while i and j both smaller than the length-value, do the while loop.
        subline = []
        while i < len(L) and j < len(L[i]):
            subline.append(L[i][j])
            i += 1
            j += 1
        #create a new grid to convenience searching.
        line.append(subline)
        subline = []

    #Do the searching in new grid row by row.
    for i in range(len(line)):
        for j in range(len(line[i])):           
            while j+pos <= len(line[i]):               
                str1 = "".join(line[i][j:j+pos])
                if str1 in s and str1 not in results:
                    results.append(str1)
                pos += 1
            pos = 3

    #return the results list to main function.
    return results

main()
