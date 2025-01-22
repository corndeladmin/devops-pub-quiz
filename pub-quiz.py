from inputimeout import inputimeout
import random
import questions

# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = questions.questions

<<<<<<< HEAD
def generate_random_timeout(min=5, max=10):
    return random.randint(min, max)
=======
users_score = 0
>>>>>>> 0b57fb6 (Add score tracking)

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
<<<<<<< HEAD
    try: 
        user_answer = inputimeout("Your answer (A, B, C, D): ", generate_random_timeout()).strip().upper() # Ensuring the input is uppercase for comparison
        # Check if the answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
    except: 
        time_over = 'Your time is over!'
        print("\n I'm sorry, you're just really slow at this \n") 

=======
    user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        users_score += 1
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")
>>>>>>> 0b57fb6 (Add score tracking)

# Print score
print("You scored", users_score,"/",len(quiz_questions))

# Goodbye message
print("Thanks very much for playing the Pub Quiz!")