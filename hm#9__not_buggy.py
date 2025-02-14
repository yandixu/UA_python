# Yandi Xu
# CSc110, sECTION: 001K
# Project 9, Part B: debuggy
# This program reads in data about the Scottish Independence
# referendum and outputs data about each shire's votes
# It then outputs the result of the referendum and
# What percentage voted for independence in each shire

def main():
    file = open("votes.txt")
    Lines = file.readlines()

    countTotal = 0
    countAllTotal = 0
    for m in range(1,len(Lines),2):
        line = Lines[m].strip()
        count = 0
        countAll = 0
        for words in line:
            if words.lower() == 'a':
                countAll += 1
            elif words.lower() == 'y':
                countAll += 1
                count += 1
            else:
                countAll += 1
        countTotal += count
        countAllTotal += countAll

        print(str(Lines[m-1].strip())+":",str(round((count/countAll)*100,1)))
    print()
    print("Overall there were ", round((countTotal/countAllTotal)*100,1),"yes votes")

main()
