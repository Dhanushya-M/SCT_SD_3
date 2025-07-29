# 🧠🔢 Task 03 – Web-based Sudoku Solver using Flask

This project is a web-based **Sudoku Solver** developed in **Python** using the **Flask framework**, created as part of **Task 03** of my internship at **SkillCraft Technology**.  
The app accepts a 9x9 puzzle input from the user via a web form, solves it using **backtracking**, and displays the solution on the same page.

---

## 📘 Task Description

> "Create a program that solves Sudoku puzzles automatically. The program should take an input grid representing an unsolved Sudoku puzzle and use an algorithm to fill in the missing numbers."

In this implementation, the user fills the puzzle directly in the browser. Upon submission, the back-end logic processes the input, solves it, and displays the result — or returns a message if the puzzle is unsolvable.

---

## 🧩 How It Works

- Users enter a 9x9 Sudoku grid (use `0` or leave blank for empty cells).
- The grid is sent to the Flask back-end via a POST request.
- A recursive **backtracking algorithm** solves the puzzle.
- The completed grid is rendered as output using an HTML template.

---

## 🌟 Features

- 🔢 Web form-based 9x9 Sudoku input
- ✅ Real-time solving using Python’s backtracking algorithm
- 💡 Error detection for invalid or unsolvable puzzles
- 🧹 Clean and responsive UI (HTML + Jinja templates)
- 🔄 Automatic reset and resubmission options

---

## 📁 File Structure

sudoku-solver-web/

├── app.py # Main Flask application

├── templates/

│ └── index.html # HTML template for input/output

├── static/ # (Optional) CSS or JS files

├── .gitignore # Git ignored files

├── LICENSE # MIT License

└── README.md # Project documentation


---

## 🛠️ Technologies Used

- 🐍 Python 3
- 🌐 Flask (Web framework)
- 🖥️ HTML & Jinja2 (Templating)
- ✅ CSS (optional for styling)

---

## 🚀 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sudoku-solver-web.git
   cd sudoku-solver-web
   Install Flask

2.**Install flask**

pip install flask

3.**Run the app**
  
python app.py

4.**Open in browser**

Navigate to http://127.0.0.1:5000

## 🧠 Learning Outcomes

- Implemented a backtracking algorithm in Python

- Gained experience building a web app with Flask

- Learned HTML form handling with Flask templating

- Practiced debugging user input and recursive logic

- Strengthened skills in full-stack mini project development

## 🧪 Sample Test Grid

Input:

5 3 0 | 0 7 0 | 0 0 0

6 0 0 | 1 9 5 | 0 0 0

0 9 8 | 0 0 0 | 0 6 0

------+-------+------

8 0 0 | 0 6 0 | 0 0 3

4 0 0 | 8 0 3 | 0 0 1

7 0 0 | 0 2 0 | 0 0 6

------+-------+------
0 6 0 | 0 0 0 | 2 8 0

0 0 0 | 4 1 9 | 0 0 5

0 0 0 | 0 8 0 | 0 7 9


Output:
Full solved grid will be displayed after clicking “Solve”.


## 📝 License

This project is licensed under the MIT License.
You are free to use, modify, and share it with attribution.
See LICENSE for full details.

--


## 📬 Contact

👩‍💻 Name: Dhanushya M

📧 Email: dhanushyamahendran2004@gmail.com

💼 LinkedIn: linkedin.com/in/dhanushya-m



## 🔖 Created as part of SkillCraft Technology Internship – Task 03

🧠 "Bringing logic and interactivity together through code."



---


