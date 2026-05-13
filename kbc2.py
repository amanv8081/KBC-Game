# KBC Quiz Program with Frontend (Tkinter
import tkinter as tk
from tkinter import messagebox
import tkinter

# Questions Data
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi",
        "prize": 1000,
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "options": ["Jawaharlal Nehru", "Bhagat Singh", "Mahatma Gandhi", "Subhash Chandra Bose"],
        "answer": "Mahatma Gandhi",
        "prize": 5000,
    },
    {
        "question": "Which programming language are you learning?",
        "options": ["Java", "C++", "Python", "JavaScript"],
        "answer": "Python",
        "prize": 10000,
    },
    {
        "question": "What is 5 × 6?",
        "options": ["11", "30", "56", "25"],
        "answer": "30",
        "prize": 50000,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars",
        "prize": 100000,
    },
]


class KBCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KBC Quiz Game")
        self.root.geometry("700x500")
        self.root.configure(bg="#0b1f3a")

        self.current_question = 0
        self.money_won = 0
        self.selected_option = tk.StringVar()

        # Title
        self.title_label = tk.Label(
            root,
            text="🎉 Kaun Banega Crorepati 🎉",
            font=("Arial", 24, "bold"),
            bg="#0b1f3a",
            fg="gold",
        )
        self.title_label.pack(pady=20)

        # Prize Label
        self.prize_label = tk.Label(
            root,
            text="Prize Won: ₹0",
            font=("Arial", 16, "bold"),
            bg="#0b1f3a",
            fg="white",
        )
        self.prize_label.pack(pady=10)

        # Question Label
        self.question_label = tk.Label(
            root,
            text="",
            font=("Arial", 18, "bold"),
            bg="#0b1f3a",
            fg="white",
            wraplength=600,
            justify="center",
        )
        self.question_label.pack(pady=20)

        # Options Frame
        self.options_frame = tk.Frame(root, bg="#0b1f3a")
        self.options_frame.pack(pady=10)

        self.radio_buttons = []
        for _ in range(4):
            rb = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected_option,
                value="",
                font=("Arial", 14),
                bg="#0b1f3a",
                fg="white",
                selectcolor="#1e3a5f",
                activebackground="#0b1f3a",
                activeforeground="gold",
                anchor="w",
                width=40,
                justify="left",
            )
            rb.pack(anchor="w", pady=5)
            self.radio_buttons.append(rb)

        # Submit Button
        self.submit_button = tk.Button(
            root,
            text="Submit Answer",
            font=("Arial", 14, "bold"),
            bg="gold",
            fg="black",
            command=self.check_answer,
            padx=20,
            pady=10,
        )
        self.submit_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        q = questions[self.current_question]
        self.question_label.config(
            text=f"Q{self.current_question + 1}. {q['question']}"
        )
        self.selected_option.set("")

        for i, option in enumerate(q["options"]):
            self.radio_buttons[i].config(text=option, value=option)

        self.prize_label.config(text=f"Prize Won: ₹{self.money_won}")

    def check_answer(self):
        selected = self.selected_option.get()

        if not selected:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        q = questions[self.current_question]

        if selected == q["answer"]:
            self.money_won = q["prize"]
            messagebox.showinfo(
                "Correct!", f"✅ Correct Answer! You have won ₹{self.money_won}"
            )
            self.current_question += 1

            if self.current_question < len(questions):
                self.load_question()
            else:
                messagebox.showinfo(
                    "Congratulations!",
                    f"🏆 You won the grand prize of ₹{self.money_won}!",
                )
                self.root.destroy()
        else:
            messagebox.showerror(
                "Wrong Answer",
                f"❌ Wrong Answer!\nYou take home ₹{self.money_won}",
            )
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = KBCApp(root)
    root.mainloop()
## How to Run

# 1. Save the code in a file named `kbc_quiz.py`
# 2. Open Command Prompt or Terminal.
# 3. Run:

# ```bash
# python kbc_quiz.py
# ```

## Features

# * Graphical frontend using Python `tkinter`
# * Multiple-choice questions
# * Prize money tracking
# * Correct and wrong answer popups
# * Final winning message

## Required Module

# `tkinter` is included with standard Python installations, so no extra installation is needed.
