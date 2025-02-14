#Yandi Xu
#CSC 110, Section: 001K
#Project #12: Recommendation System
#This program is usde to .....

#Constant: th name of output file. 
FILENAME = "ratings.txt"

def main():
    tittle()
    #open the inout file and read it by lines.
    lines = open(FILENAME).readlines()
    books,dic = treatfile(lines)
    
    task = input("next task?" )
    while task != "quit":
        if task == "recommend":
            recommend(books,dic)
        elif task == "average":
            sorting = average(books,dic)
            #print the average ratings of books. 
            for i in range(len(sorting)):
                print(sorting[i][1].strip(),sorting[i][0])
        task = input("\nnext task? ")

#This function print the description of the whole program.
def tittle():
    print("Welcome to the CSC110 Book Recommender. Type the word in the")
    print("left column to do the action on the right。")
    print("recommend : recommend books for a particular user")
    print("averages  : output the average ratings of all books in the system")
    print("quit      : exit the program")

#This function take lines as parameter to get a list of books' name, and
# a dictionary contain the users' name and their rating matching wiht the books.
#Parameter: lines: a list of input file.
#Return: books: a list of books' name
#        dic: dictionary contain users' name (keys) and rating (values) pairs.
def treatfile(lines):
    #this for loop used to casting the names of books into a list.
    books = set()
    for i in range(1,len(lines),3):
        if lines[i] not in books:
            books.add(lines[i].strip())
    books = list(books)
    
    #create a blank dictionary to store the keys.
    dic = {}
    for i in range(0,len(lines),3):
        if lines[i] not in dic:
            dic[lines[i].strip()] = [0]*len(books)

    #add the maooing values to soecfic keys. 
    for elem in dic:
        for i in range(len(books)):
            for j in range(1,len(lines)-1,3):
                if lines[j].strip() == books[i] and lines[j-1].strip() == elem:
                    dic[elem][i] = lines[j+1].strip()

    return books,dic

#This function will be called when the task is recommend. It will find the
#similar books, and will recommend them to the user.
#Parameter: books: a list of books' name
#           dic: dictionary contain users'name (keys) and rating (values) pairs.
def recommend(books,dic):
    recom = []
    highest_three = {}
    final_recom = []
    user = input("user? ")

    #identify whether the "user" input exist in dictionary.
    if user in dic:
        goal = dic[user]  #a list of the user's rating fo books.
        for elem in dic:
            similar = 0
            for i in range(len(goal)):
                similar += int(goal[i])*int(dic[elem][i])
            sub_tuple = (similar,elem)
            recom.append(sub_tuple)

        #the following steps are used to sorting, reverse the recom list.
        #poping the similar results of user himself and
        #take the highest three as a new list of tuples.
        recom.sort()
        recom.reverse()
        recom.pop(0)
        new_recom = recom[:3]

        #based on the highest three, taking the pairs of them out
        #from the dictionary as a new sub dictionary.
        for item in new_recom:
            highest_three[item[1]] = dic[item[1]]

        #this for loop creates a tuple contain the average rating of book and
        #the name of book. Then ass the tuples into a final recommendation list.
        for i in range(len(books)):
            total = 0
            count = 0
            for elem in highest_three:
                total += int(highest_three[elem][i])
                if int(highest_three[elem][i]) != 0:
                    count += 1

            #this if is used to avoid the division by 0 ERROR.
            if count != 0:
                aver = total/count
                sub_tuple = (aver,books[i])
                final_recom.append(sub_tuple)

        final_recom.sort()
        final_recom.reverse() #sort and reverse the final recommendation list.

        for item in final_recom:
            if item[0] > 0:
                print(item[1],item[0])  #print the recommended books and rating.
                
    #if the user do not exist in dictionary, it will do the average function.
    else:
        sorting = average(books,dic)
        for i in range(len(sorting)):
                print(sorting[i][1].strip(),sorting[i][0])

#This function will be called when the task is average.
#Parameter: books: a list of books' name
#           dic: dictionary contain users'name (keys) and rating (values) pairs.
#Return: sorting: the sorted list of average rates of books from the highest.
def average(books,dic):
    sorting = []
    for i in range(len(books)):
        total = 0
        count = 0
        for elem in dic:
            if int(dic[elem][i]) != 0:               
                total += int(dic[elem][i])
                count += 1
        aver = total/count
        sub_tuple = (aver,books[i])
        sorting.append(sub_tuple)

    sorting.sort()
    sorting.reverse()

    return sorting
    
main()
