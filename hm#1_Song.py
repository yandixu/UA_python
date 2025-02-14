#Author: Yandi Xu
# Course: CSC 110, Section 001K, Autumn 2017, 
# Programming Assignment #1, 08/28/2017
#
#This program's behavior is to use function and print statements to produce a cumulative song.

base_1 = "There was an old woman who swallowed a"

def main ():
    print(str(base_1)+" fly.")
    base_2()
    print()
    spider()
    accumu_spider()
    print()
    bird()
    accumu_bird()
    print()
    cat()
    accumu_cat()
    print()
    dog()
    accumu_dog()
    print()
    snake()
    accumu_snake()
    print()
    horse()

def base_2():
    print("I don't know why she swallowed that fly,")
    print("Perhaps she'll die.")

def spider():
    print(str(base_1)+" spider,")
    print("That wriggled and iggled and jiggled inside her.")

def accumu_spider():
    print("She swallowed the spider to catch the fly,")
    base_2()

def bird():
    print(str(base_1)+" bird,")
    print("How absurd to swallow a bird.")

def accumu_bird():
    print("She swallowed the bird to catch the spider,")
    accumu_spider()

def cat():
    print(str(base_1)+" cat,")
    print("Imagine that to swallow a cat.")

def accumu_cat():
    print("She swallowed the cat to catch the bird,")
    accumu_bird()

def dog():
    print(str(base_1)+" dog,")
    print("What a hog to swallow a dog.")

def accumu_dog ():
    print("She swallowed the dog to catch the cat,")
    accumu_cat()

def snake():
    print("There was an old woman who swallowed a snake,")
    print("So crazy to swallow a snake.")

def accumu_snake ():
    print("She swallowed the snake to catch the dog,")
    accumu_dog()

def horse ():
    print(str(base_1)+" horse,")
    print("She died of course.")
    
main ()
