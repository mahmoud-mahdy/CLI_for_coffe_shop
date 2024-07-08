# AWS_Pipeline
# CLI_coffe_shop

### Project Background:
The project was done during my boot camp course in generations UK and Ireland.
The CLI Coffee Shop Management System is a Python-based application designed to manage the daily operations of a coffee shop. It offers a user-friendly command-line interface for efficient management of products, couriers, and orders.

### Client requirements:
three menus for products, couriers and orders
a client can add, inspect, edit and remove each of the products list, couriers list and orders list.
data persistence data saved in files or in a database (MySQL).
to use files to save dates please go to branch "week-5" and to use MYSQL database use the main branch and compose up the docker container

### How to run the app
method one: can be run using Python on the command line or any other IDE
method two: can be run using the stand-alone file (..\dist\main\main)
please note that the MYSQL database has to be working you can use the docker file to compose up the database container

### Testing
pytest is used to run unit tests as proof of concept however projects have been tested fully through manual testing.

# Machine learning predictive model

### Project:
Machine learning predictive models

### Tasks: 
develop a machine learning model to predict the likelihood of a patient having a stroke. The dataset used consisted of 5110 patients with 12 attributes, including age, gender, hypertension, heart disease, and smoking status, among others.

### Overview:
Knime software - graphical user interface (GUI) has been used to develop the models therefore **no code is provided in the repository.** 

⦁	preprocessing of the data such as removing the ID attribute, ignoring the missing,.etc.

⦁	analysing the dataset and identifying the attributes that affect the likelihood of having a stroke.

⦁	several classification algorithms, including random forest, gradient-boosted trees, and probabilistic neural networks, were implemented, and their performance was compared 
  to determine the best algorithm 

![2](https://github.com/mahmoud-mahdy/My_Portfolio/assets/121267693/aa03d623-f6dd-4d63-91c7-0145ccb9e31d)

![3](https://github.com/mahmoud-mahdy/My_Portfolio/assets/121267693/c8811cb5-033e-48b2-84d8-1e20e06cb816)

### Results:
reached a prediction accuracy of 77.8% using the random forest algorithm and the results demonstrated the effectiveness of the random forest algorithm in handling the classification problem.

# sodoku_solver

The "Sudoku Solver" is a Python script developed as a personal project to enhance my programming skills in Python during my free time. This project focuses on efficiently solving Sudoku puzzles using a backtracking algorithm.

### How to Use:

⦁ Input Puzzle: Define the 'board' variable with the Sudoku puzzle, inserting '0' for empty cells.
  
⦁ Run Solver: Execute the script, triggering the backtracking algorithm to solve the Sudoku puzzle.

⦁ View Solution: The completed Sudoku solution is displayed through the 'print_board' function

### how the backtracking algorithm works:

⦁ Finding an Empty Cell: The algorithm locates an empty cell on the Sudoku board. If none exists, the puzzle is considered solved; otherwise, an empty cell is chosen.

⦁ Attempting Possible Solutions: It systematically tries numbers from 1 to 9 in the selected cell, verifying each against Sudoku rules. If a valid number is found, the 
  process continues to the next empty cell; otherwise, it backtracks.
  
⦁ Recursion and Backtracking: The algorithm recurs and explores different number combinations. When it hits a dead-end, it backtracks to the previous cell, trying alternative 
  numbers until a solution is reached.

⦁ By repeating these steps, the algorithm systematically fills in all empty cells, ultimately solving the Sudoku puzzle.

# Mini-Games

have multiple small games for learning and developing my skills most advanced one is the blackjack game
