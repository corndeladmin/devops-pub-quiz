# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What number was the Apollo mission that successfully put a man on the moon for the first time in human history?",
        "options": ["A) Apollo 11", "B) Apollo 12", "C) Apollo 13"],
        "answer": "A"
    },
    {
        "question": "Who sang the title song for the latest Bond film, No Time to Die?",
        "options": ["A) Adele", "B) Sam Smith", "C) Billie Eilish"],
        "answer": "C"
    },
    {
        "question": "Where was the first example of paper money used??",
        "options": ["A) China", "B) Turkey", "C) Greece"],
        "answer": "A"
    },
    {
        "question": "Who is generally considered the inventor of the motor car?",
        "options": ["A) Henry Ford", "B) Karl Benz", "C) Henry M. Leland"],
        "answer": "B"
    },
    {
        "question": "What is the longest-running Broadway show ever?",
        "options": ["A) Les Miserable", "B) The Lion King", "C) The Phantom of the Opera"],
        "answer": "C"
    },
    # Learners can add more questions here following the same structure
]

# Initialize score and streak tracking
score = 0
total_questions = len(quiz_questions)
current_streak = 0
best_streak = 0

# Loop through each question
for question_num, question in enumerate(quiz_questions, 1):
    print(f"\nQuestion {question_num}/{total_questions}")
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    user_answer = input("Your answer (A, B, C): ").strip().upper() # Ensuring the input is uppercase for comparison
    
    # Check if the answer is correct and update score
    if user_answer == question["answer"]:
        print("CORRECT!")
        score += 1
        current_streak += 1
        best_streak = max(current_streak, best_streak)
        print(f"Correct! 🎯 Current streak: {current_streak}!")
    else:
        print(f"WRONG! Clearly the correct answer was {question['answer']}.")
        current_streak = 0

# Display final score
print("\n=== Final Score ===")
print(f"You got {score} out of {total_questions} questions correct!")
percentage = (score / total_questions) * 100
print(f"That's {percentage:.1f}%!")

# Add a performance message
if percentage == 100:
    print("Perfect score! 🏆")
elif percentage >= 70:
    print("Great job! 🌟")
elif percentage >= 50:
    print("Good effort! 👍")
else:
    print("Keep practicing! 📚")

# Display final score with additional stats
print("\n=== Final Score ===")
print(f"You got {score} out of {total_questions} questions correct!")
percentage = (score / total_questions) * 100
print(f"That's {percentage:.1f}%!")
print(f"Best streak: {best_streak} questions in a row! 🔥")

# Add a performance message
if percentage == 100:
    print("Perfect score! 🏆")
elif percentage >= 70:
    print("Great job! 🌟")
elif percentage >= 50:
    print("Good effort! 👍")
else:
    print("Keep practicing! 📚")

# Goodbye message
print("\nThanks for playing our Pub Quiz!")
