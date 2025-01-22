from inputimeout import inputimeout
import random
import questions

# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = questions.questions

def generate_random_timeout(min=5, max=10):
    return random.randint(min, max)

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
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


# Goodbye message
print("Thanks very much for playing the Pub Quiz!")