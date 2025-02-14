#Yandi Xu
#CSC110, Sectio :001K
#Project5: Gradanator
#This Projest has used if／else， for loops，input and return values
# to build a gradenator.

def main():
    tittle()
    over_all()

#this function is used to print the intro part for the whole program.
def tittle():
    print("This program reads exam/homework scores")
    print("and reports your overall course grade.")
    print()

#This function has used input and if/else to calculate the weighted exam score.
#Parameter(input):
# weight:how much the exam weight on final grade.
# score:how much the student earn without weighted.
# shift & amount: whether the score will be shifted and how much the shift is.
#Return: the final weighted exam score with shift.
def exam():
    constant = 100 #the constant value: 100.
    weight = int(input("Weight (0-100)? "))
    score = int(input("Score earned? "))
    shift = int(input("Were scores shifted (1=yes, 2=no)? "))
    if shift == 1:
        amount = int(input("Shift amount? "))
        score += amount
    if score > constant: #make sure the shifted score is ≤100.
        score = constant
    else:
        score = score
    print("Total points =",score,"/",constant)
    weighted = score/constant*weight #calculate the final weighted score
    print("Weighted score =",round(weighted,1),"/",weight)
    print()
    
    return weighted

#This function has used input,for loops and if/else to calculate the
# weighted and accumulated homework score.
#Return: the final weighted homwwork score.
def homework():
    constant = 37  #constant value: the max score for section total.
    #Parameters: 
    assign_score = 0  #the accumulated assignment scores student earned
    assign_max = 0  #the accumulated assignment max socres
    sec_points = 0  #the points determined by # of section attend.
    sub_total = 0
    weight = int(input("Weight (0-100)? "))
    nums = int(input("Number of assignments? "))
    for num in range(1,nums+1): #accumulate the total assignments score and max.
        score = int(input("Assignment "+str(num)+" score? "))
        single_max = int(input("Assignment "+str(num)+" max? "))
        assign_score += score
        assign_max += single_max
    attend = int(input("How many sections did you attend? "))
    sec_points = attend*3
    if sec_points > constant: #make sure the section points is ≤37
        sec_points = constant
    else:
        sce_points = sec_points
    sub_total = sec_points + assign_score
    #check the subtotal socre is ≤the (max of assignments + 37).
    if sub_total > assign_max+constant: 
        sub_total= assign_max+constant
    else:
        sub_total = sub_total
    print("Section points =",sec_points,"/",constant)
    print("Total points =",sub_total,"/",assign_max+constant)
    weighted = sub_total/(constant+assign_max)*weight #calculate the weighted score
    print("Weighted score =",round(weighted,1),"/",weight)
    print()
    
    return weighted

#This function has used input and if to get the weighted scores of
# quizzes and daily homework.
#Parameters:
# weight: how much the score weight on final grade.
# total_earn: how munch the student earn.
# total_possible: how mucht the total points is possible to be.
#Return: the final weighted score.
def quiz_hm():
    weight = int(input("Weight (0-100)? "))
    total_earn = int(input("Total points earned? "))
    total_poss = int(input("Total points possible? "))
    #make sure the grade of quizzes or daily homework is ≤ the possible total。
    if total_earn > total_poss:   
        total_earn = total_poss
    weighted = total_earn / total_poss * weight
    print("Total points =",total_earn,"/",total_poss)
    print("Weighted score =",round(weighted,1),"/",weight)
    print()
    
    return weighted

#This function is used to call the functions above to get values
# then calculate the final grade and level.
def over_all():
    total = 0
    level = ""
    message = ""
    print("Midterm 1:")
    mid1 = exam()
    print("Midterm 2:")
    mid2 = exam()
    print("Final:")
    final = exam()
    print("Homework:")
    hm = homework()
    print("Quizzes:")
    quiz = quiz_hm()
    print("Daily homework:")
    d_hm = quiz_hm()
    total = mid1 + mid2+ final + hm + quiz + d_hm
    #use if/else to check the level of student's grade.
    if total>=90:
        level = "A"
        message = "Well Done here!"
    elif total >=80:
        level = "B"
        message = "Still Pretty Good!"
    elif total >=70:
        level = "C"
        message = "Try more hard for next B."
    elif total >=60:
        level = "D"
        message = "Safe pass."
    else:
        level = "F"
        message = "Failed :(("
    print("Overall percentage =",round(total,1))
    print("Your grade will be at least:",level)
    print(message)


main()
    

