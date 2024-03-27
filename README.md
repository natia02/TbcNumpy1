# Student Grade Analysis

This is a Python project that analyzes student grades and provides various statistics and information about a group of students. The project uses NumPy for numerical operations and Tabulate for creating a tabular representation of the data.

## Features

- Generates random grades for a given number of students across multiple subjects.
- Displays a tabular representation of the student data, including names, grades, and subjects.
- Finds the student with the highest average score across all subjects.
- Identifies the students with the highest and lowest scores in mathematics.
- Lists all students whose English scores are above the average English score.

## Requirements

- Python 3.x
- NumPy
- Tabulate

To install the required packages, run the following command:

```bash
    pip install -r requirements.txt
```


## Usage

1. Clone or download the project repository.
2. Open the project in your preferred Python IDE or editor.
3. Navigate to the project directory.
4. Run the `main.py` file.

The program will execute and display the following outputs:

- A tabular representation of the student data.
- The student with the highest average score across all subjects.
- The students with the highest and lowest scores in mathematics.
- A list of students whose English scores are above the average English score.

## Method Descriptions

1. `__init__(self)`:
   - Initializes the class instance with student names, subject names, and random grades.
   - Creates the `table` NumPy array containing student names and grades.

2. `print_table(self)`:
   - Converts the `table` NumPy array to a list of lists.
   - Prints the table in a tabular format using the `tabulate` function.

3. `find_highest_average_student(self)`:
   - Finds the student with the highest average score across all subjects.
   - Prints the student's name and highest average score.

4. `find_highest_lowest_math_score(self)`:
   - Finds the students with the highest and lowest scores in mathematics.
   - Prints the student names and corresponding math scores.

5. `print_students_above_avg_english(self)`:
   - Prints a list of students whose English scores are above the average English score.

6. `main(self)`:
   - The entry point for executing the program.
   - Calls the other methods in the desired order.

## Customization

You can customize the project by modifying the following variables in the `__init__` method of the `Main` class:

- `first_names`: A list of first names for the students.
- `last_names`: A list of last names for the students.
- `subjects`: A list of subject names.
- `num_students`: The number of students to generate data for.

Additionally, you can modify the existing methods or add new methods to perform different analyses or operations on the student data.

