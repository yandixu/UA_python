# Yandi XU
# CS 120, Fall 18, Section: 01F
# Project#1: Word Grid
# This program is used to create a grid include randomly
# generated lower-case letters and print the grid out per row. 

#import random to get number.
import random

def main():
    N,S = init()
    G = make_grid(N)
    
    #print out the grid.
    print_grid(G)

#This function is used to get input number of N and S.
#Return: N: number used to make N*N grid.
#        S: used to initialize the random number generator.
def init():
    N = int(input())
    S = input()
    
    #intialize the random number generator.
    random.seed(S)

    return N,S
#This function us used to make a N*N grid and add lower-case letters into it.
#Parameter: N: number used to make N*N grid.
#Return: grid: an N*N gird filled with lower-case letters
def make_grid(N):
    grid = []
    for i in range(N):
        grid.append([])
        for j in range(N):
            grid[i].append(chr(random.randint(ord("a"),ord("z"))))

    return grid

#This function is used to print out the grid by rows.
#Parameter: G: the grid.
def print_grid(G):
    for elem in G:
        print(",".join(elem))

main()
