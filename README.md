Student Class Analyzer

A beginner-friendly Python program that analyzes the marks of a class of students. It calculates total marks, average marks, and the number of students who passed or failed.

About the Project

I am a freshman undergraduate learning Python. This is a beginner Python practice project focused on loops, conditions, variables, user input, and basic calculations.

What the Program Does

Asks how many students are in the class.

Takes each student's name and marks.

Calculates total marks.

Counts students who passed and failed.

Calculates the class average.

Displays the results.

A student is considered to have passed when their marks are 40 or above.

Concepts Used

input()

int()

Variables

for loops

range()

if/else

Comparison operators

Counters

Accumulators

Arithmetic operations

f-strings

Code

how_many = int(input("How many students: "))

total = 0
passed = 0
failed = 0

for i in range(1, how_many + 1):
    student_name = input(f"Student {i} name: ")
    marks = int(input(f"Student {i} marks: "))

    total = total + marks

    if marks >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

average = total / how_many

print()
print("===== STUDENT CLASS ANALYZER =====")
print(f"Total marks: {total}")
print(f"Average marks: {average}")
print(f"Students passed: {passed}")
print(f"Students failed: {failed}")

How It Works

Getting the Number of Students

how_many = int(input("How many students: "))

The program asks for the number of students and converts the input into an integer.

Counting Students

if marks >= 40:
    passed = passed + 1
else:
    failed = failed + 1

Students with marks of 40 or above are counted as passed. Others are counted as failed.

Calculating the Average

average = total / how_many

The total marks are divided by the number of students.

Example

How many students: 3
Student 1 name: A
Student 1 marks: 80
Student 2 name: B
Student 2 marks: 35
Student 3 name: C
Student 3 marks: 65

===== STUDENT CLASS ANALYZER =====
Total marks: 180
Average marks: 60.0
Students passed: 2
Students failed: 1

Requirements

Python 3.x

No external libraries

How to Run

Save the program as:

Student Class Analyzer.py

Then run:

python "Student Class Analyzer.py"

Learning Status

Level: Beginner
Project Type: Python Practice Project
Focus: Loops, conditions, counters, accumulators, and calculations

Future Improvements

Display each student's result.

Store student information in lists or dictionaries.

Find the highest and lowest marks.

Add input validation.

Calculate grades.

Move the analysis into functions.

Create a menu-driven version.

Author

A freshman undergraduate learning Python and building small projects to develop programming fundamentals.
