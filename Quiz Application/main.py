#QUIZE GAME

questions = ("Who developed the Python language?",
             "Which of these of python Frame-Work",
             "What is the maximum possible length of an identifier?",
             "which year was the Python language developed?",
             "In which language is Python written?",
             "Which one of the following is the correct extension of the Python file?",
             "What do we use to define a block of code in Python language?",
             "Which character is used in Python to make a single line comment?",
             "Which of the following statements is correct regarding the object-oriented programming concept in Python?",
             "What is the method inside the class in python language?")

options =  (("A. Zim Den","B. Guido van Rossum", "C. Niene Stom","D. Wick van Rossum"),
            ("A. SpringBoot","B. Djnago","C. Flask","D. B and C Both"),
            ("A. 16","B. 32","C. 64","D. None of these above"),
            ("A. 1995","B. 1972","C. 1981","D. 1989"),
            ("A. ENGLISH" ,"B. PHP" ,"C. C","D. All of the above"),
            ("A. .py","B. .python","C. .p","D. None of these"),
            ("A. Key","B. Brackets","C. Indentation","D. None of these"),
            ("A. !","B. #","C. //","D. /"),
            ("A. Objects are real-world entities while classes are not real","B. Classes are real-world entities while objects are not real","C. Both objects and classes are real-world entities","D. All of the above"),
            ("A. Object","B. Function","C. Attribute","D. Argument"))

answers = ("B", "D", "D", "D", "C", "A", "C", "B", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1

print("------------------------")
print("        RESULT          ")
print("------------------------")

print("answers: ",end=" ")
for answer in answers:
    print(answer,end=" ")
print()


print("gussess: ",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")