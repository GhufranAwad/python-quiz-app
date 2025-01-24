import tkinter as tk
from tkinter import messagebox
import random

# topics: Loops, Lists, and Strings
questions = [
    {"topic": "Loops", "question": "What is the output of `for i in range(3): print(i)`?",
     "options": ["0 1 2", "1 2 3", "0 1 2 3"], "answer": 0},
    {"topic": "Lists", "question": "What is the output of `my_list = [1, 2, 3]; print(my_list[1])`?",
     "options": ["1", "2", "3"], "answer": 1},
    {"topic": "Strings", "question": "What is the output of `'hello'.upper()`?",
     "options": ["hello", "HELLO", "error"], "answer": 1},
    {"topic": "Strings", "question": "What does `'world'.find('r')` return?",
     "options": ["1", "2", "3"], "answer": 1}
]

def generate_question():
    """Generates a question based on the selected topic."""
    selected_topic = topic_entry.get().strip().lower() 
# Get user input and convert to lowercase
    filtered_questions = [q for q in questions if q["topic"].lower() == selected_topic]
# If no matching questions are found, display an error message
    if not filtered_questions:  
        messagebox.showerror("Error", f"No questions available for topic: {selected_topic}")
        return

    # Randomly select a question from the filtered list
    question = random.choice(filtered_questions)
    question_label.config(text=f"Q: {question['question']}", fg="#333333")

    # Display Options
    for i, option in enumerate(question["options"]):
        option_buttons[i].config(text=option, value=i)

    # Store the correct answer for checking
    global correct_answer
    correct_answer = question["answer"]

def check_answer():
    """Checks the selected answer and provides feedback."""
    if selected_option.get() == correct_answer:
        messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
        messagebox.showerror("Incorrect", "Wrong answer. Try again!")

# Set up the main application window
app = tk.Tk()
app.title("Python Quiz App")
# Light blue background
app.config(bg="#d3abff")
# Set a fixed window size  
app.geometry("400x400")  

# Input field for the topic
tk.Label(app, text="Enter a Topic (Loops, Lists, Strings):", font=("Arial", 14), bg="#F0F8FF", fg="black").pack(pady=10)
topic_entry = tk.Entry(app, font=("Arial", 12), width=30, bg="#FFFFFF", relief="groove")
topic_entry.pack(pady=5)

# Generate button
tk.Button(app, text="Generate Question", command=generate_question, font=("Arial", 12), bg="#4682B4", fg="white").pack(pady=10)

# Question label
question_label = tk.Label(app, text="Your question will appear here!", font=("Arial", 12), fg="black", wraplength=450, justify="left")
question_label.pack(pady=10)

# Options (Radio Buttons)
selected_option = tk.IntVar()
option_buttons = [
    tk.Radiobutton(app, variable=selected_option, font=("Arial", 10), bg="#F0F8FF", anchor="w")
    for _ in range(3)
]
for btn in option_buttons:
    btn.pack(anchor="w", padx=20, pady=5)

# Submit button
tk.Button(app, text="Submit Answer", command=check_answer, font=("Arial", 12), bg="#32CD32", fg="black").pack(pady=20)

# Run the application
app.mainloop()
