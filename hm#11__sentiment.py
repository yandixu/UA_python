# Yandi Xu
# CSC110. Section: 001K
#Project#11: Sentiment Analysis
#This projecthas used dictionaries to a sentiment analysis for an input file.

def main():
    word_time = {}  #creat an empty dictionary to sort the occurence of words.
    word_count = {}  #creat an empty dictionary to sort the count of words.
    time = 0  #the occurence of word.(accumulate)
    count = 0  #the count of word.(accumulate)
    
    file = open(input("Learning data file name? ")) #get the name of input file.
    lines = file.readlines() #read the file as a list.
    print("\nWhat would you like to do?\n1: Get the score of a word")
    print("2: Get the average score fo words in a file")
    print("3: Find the highest / lowest scoring words in a life")
    print("4: Score the words in a life into positive.txt and negative.txt")
    print("5: Exit the program")
    #get the user's option to treate file.
    option = input("Enter a number 1 - 5: ")

    # This while loop is used to do different option bwtween 0-4.
    while option != "5":
        if option == "1":
            start(lines,time,count,word_time,word_count)
        elif option == "2":
            average_score(lines,time,count,word_time,word_count)
        elif option == "3":
            high_low_score(lines,time,count,word_time,word_count)
        elif option == "4":
            out_to_file(lines,word_time,word_count)
        print("\nWhat would you like to do?\n1: Get the score of a word")
        print("2: Get the average score fo words in a file")
        print("3: Find the highest / lowest scoring words in a life")
        print("4: Score the words in a life into positive.txt and negative.txt")
        print("5: Exit the program")
        option = input("Enter a number 1 - 5: ")

# This function will be called when option is 1, to get score of specifc word.
# Parameters: lines: a list syary by the rating score
#             time: the occurence of words.
#             count: the rating score of word.
#             word_time: a dictionary of the occurence of words.
#             word_count: a dictionary of the rating score of words.
def start(lines,time,count,word_time,word_count):   
    word = input("Which word? ").lower()
    if ord("a") <= ord(word[0]) <= ord("z"):
        for line in lines:
            line = line.lower().split()
            if word in line:
                time += 1
                count += int(line[0])
        word_time[str(word)] = time
        word_count[str(word)] = count
    score = round(word_count[str(word)]/word_time[str(word)],2)
    print("Score =",score)
    if score >= 2:
        print(word,"is positive.")
    else:
        print(word,"is negative")
        
# This function will be called when option is 2, to calculate the average score of
# another input file based on the current input file.
# Parameters: lines: a list syary by the rating score
#             time: the occurence of words.
#             count: the rating score of word.
#             word_time: a dictionary of the occurence of words.
#             word_count: a dictionary of the rating score of words.    
def average_score(lines,time,count,word_time,word_count):
    score = 0
    #get the name of another input file and read it.
    wordss = open(input("file name? ")).read()
    words = wordss.split()
    for word in words:
        for line in lines:
            line = line.split()
            if word in line:               
                time += 1
                count += int(line[0])
        word_time[str(word)] = time
        word_count[str(word)] = count
        score += word_count[str(word)]/word_time[str(word)]
    print("Score =",round(score/len(words),2))
    if score >= 2:
        print(str(wordss),"\nis positive.")
    else:
        print(str(wordss),"\nis negative")
        
    comment = input("Am I right (yes/no)? ")
    #this if/else is used to let the user check whether the result is correct.
    # when the result is not correct, the string will be rewrite and stored
    # to the end of lines list.
    if comment[0].lower() != "y":
        new_comment = input("What score should this sentence have \
                            (0 - 4 where 4 is the most positive)?")
        new_str = new_comment+" "+wordss
        lines.append(new_str)

# This function will be called when option is 3, to compare the min and max
# score of the another input file based on the current input file.
# Parameters: lines: a list syary by the rating score
#             time: the occurence of words.
#             count: the rating score of word.
#             word_time: a dictionary of the occurence of words.
#             word_count: a dictionary of the rating score of words.    
def high_low_score(lines,time,count,word_time,word_count):
    maxm = 0
    minm = 5
    score = 0
    wordss = open(input("file name? ")).read()
    words = wordss.lower().split()
    for word in words:
        for line in lines:
            line = line.split()
            if word in line:               
                time += 1
                count += int(line[0])
        word_time[str(word)] = time
        word_count[str(word)] = count
        score = word_count[str(word)]/word_time[str(word)]
        maxm = max(maxm,score)
        # do the comparsion.
        if maxm == score:
            name_1 = str(word)
        if score <= minm:
            minm = score
            name_2 = str(word)
    print("Maximum score is",maxm,"for",name_1)
    print("Minimum score is",minm,"for",name_2)

# This function will be called when option is 4, to output words in lines list
# to the positive.txt / negative.txt based on their score.
# Parameters: lines: a list syary by the rating score
#             word_time: a dictionary of the occurence of words.
#             word_count: a dictionary of the rating score of words.     
def out_to_file(lines,word_time,word_count):
    p = open("positive.txt","w")
    n = open("negative.txt","w")
    for line in lines:
        line = line.lower().split()
        for word in line:
            if ord("a") <= ord(word[0]) <= ord("z"):
                pass
            
    '''I didn't finish this project since I'm still so
         confused by the usage fo dictionary.'''

    
main()
