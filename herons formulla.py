print("____________________________________________________________________")
print("this is a program made by saksham ")
print("instruction:-")
print("1.it is necessary that you got the class 9 imo olympiad workbook")
print("you need to read the question,solve it and write the option you think is correct ")
print("then this program will tell you wheather it is correct or not it it is incorrect it will show you the correct "
      "answer.")
print("this program will ask you to fill the option a,b,c,d")
print("the question no ex-Q1,Q2 etc is the answer of the same question as marked in the book ")

print("____________________")
print("this program will only tell you the answer's of ch 7 named TRIANGLE ")
print("____________________")

questions = ("Q1",
                       "Q2",
                       "Q3",
                       "Q4",
                       "Q5:",
                       "Q6 ",
                        "Q7",
                        "Q8",
                        "Q9 ",
                        "Q10:",
                        "Q11 ",
                        "Q12: ",
                        "Q13:",
                        "Q14 ",
                        "Q15",
                        "Q16",
                        "Q17 ",
                        "Q18:",
                        "Q19 ",
                        "Q20")

options = (("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"),
                   ("A", "B", "C", "D"))
#          1     2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20
answers = ("B", "D", "B", "C", "C", "C", "C", "A", "A", "C", "C", "B", "A", "A", "D", "A", "A", "C", "D", "D")
guesses = []
score = 0
question_num = 0

for question in questions:

    print("____________________")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("----------CORRECT!----------")

    else:
        print("----------INCORRECT!----------")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("____________________")

print("____________________")
print("       RESULTS        ")
print("____________________")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

print("this program is created by saksham singh")
