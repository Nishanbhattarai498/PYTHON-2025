
#-------------------------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print("")
        print(key)
        for i in options[question_number - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1
    
    show_score(correct_guesses, guesses)


#-------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")   
        return 1
    else:
        print("Incorrect!")
        return 0
        
#-------------------------------------------
def show_score(correct_guesses, guesses):
    print("")
    print("Results:")
    print("")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print("")
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print("")
    score= (correct_guesses / len(questions)) * 100
    print("")
    print("Your score is: " + str(int(score)) + "%")
    print("")

#-------------------------------------------
def play_again():
    response = input("Do you want to play again? (yes or no): ").lower()
    if response == "yes":
        return True
    else:
        return False
#-------------------------------------------


questions = {
    "who created python?":"A",
    "what year was python created?":"B",
    "python is tributed to which comedy group?":"C",
    "is python owned by google?":"A",
}

options = [
     ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
     ["A. 2000", "B. 1991", "C. 1989", "D. 1995"],
     ["A. Simpsons", "B. The Beatles", "C. Monty Python", "D. Friends"],
    ["A. True", "B. False"]
] #list of lists

new_game()
while play_again():
    new_game()
print("Thanks for playing!")
#-------------------------------------------
# This code is a simple quiz game that asks the user multiple-choice questions and checks their answers. The game continues until the user chooses to stop playing. The score is calculated based on the number of correct answers.