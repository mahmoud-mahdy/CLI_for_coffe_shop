# AWS_Pipeline

### Project Background

This full End-to-End ETL pipeline was developed for the Cafehub chain. The objective was to create a comprehensive data pipeline system designed to streamline and manage orders across multiple branches of coffee shops. when uploading the data to the s3 bucket the pipeline from there starts as explained in the diagram the data gets processed, cleaned, normalised and sent to the Redshift warehouse additionally powerful visualization through Grafana to monitor and analyze orders is added to the system to show the data from all the branches so it can be analysed.


### The Pipeline architecture
<img width="594" alt="ar" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/c0164b2f-a965-4251-8679-91ccc7e3c591">

### Final product
The following video shows the final product which is the data shown in graphs on Grafana that is connected to Redshift and shows the pipeline working through adding new data to the pipeline

https://github.com/mahmoud-mahdy/My_Portfolio/assets/121267693/946dec27-6188-4d18-8b00-edfb6a7ea242


### Normalisation process:
the following graph shows the normalisation process and how the data transforms from the left to the right forum before being stored in the database.

![Screenshot 2024-01-04 233145](https://github.com/mahmoud-mahdy/My_Portfolio/assets/121267693/2b6db6b9-20e2-4024-8cd9-04c38d81d905)


### Tools and technology used
<img width="249" alt="Screenshot 2023-12-13 154251" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/faa25c6b-a843-4b4d-8987-c2e93aa949c2">
<img width="134" alt="Screenshot 2023-12-13 154308" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/5d02c04b-2a14-4ad8-9bad-f6c9c23ab80d">
<img width="219" alt="Screenshot 2023-12-13 154208" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/b918912b-ba10-4476-a405-5f773aaa5fa3">
<img width="200" alt="Screenshot 2023-12-13 154447" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/9dc053be-f06d-44c5-a43d-4bf0212f0949">
<img width="164" alt="Screenshot 2023-12-13 154405" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/2bb27680-4179-43cb-b4fc-904bb9343eff">
<img width="242" alt="Screenshot 2023-12-13 154430" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/90c427de-8725-4251-806f-9a238bbcc544">
<img width="215" alt="Screenshot 2023-12-13 154352" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/f7db7e4b-0b31-48b9-b8ca-9cde42b2735f">
<img width="154" alt="Screenshot 2023-12-13 154227" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/809b26b3-a78c-41cc-9cb6-684df342db4a">
<img width="153" alt="Screenshot 2023-12-13 154502" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/e2d27f75-9908-4dbf-85f0-6531b2ba7da6">
<img width="176" alt="Screenshot 2023-12-13 154522" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/919eda8c-e7bf-4552-8598-a7ccd24fb7a6">
<img width="123" alt="Screenshot 2023-12-13 163220" src="https://github.com/DE-X5-LLE/team-2-project/assets/147624401/cbc8444a-91eb-491b-b43a-847012b9d77b">

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
