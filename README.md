# The-Variables 
# Team Members: Matti Wakiwaya, Nailah Abdulbarr, Tidjani Sidi Ahmed, Andrew Ly
# Project Title: Student Gradebook 
#Roles: 
* Matti Wakiwaya: Project Manager
* Nailah Abdulbarr: Documentation Manager
* Tidjani Sidi Ahmed: Tester/Coder
* Andrew Ly: Coder

# Description: Many schools face challenges when it comes to efficiently managing and tracking student grades. This project aims to develop a comprehensive user-friendly web designed to simplify grade management for both teachers and students.
* Key Features:
* User-Friendly Interface: A clean, intuitive design for both the website and app that allows users to easily navigate and access relevant features.
* Grade Average Calculator: A smart, easy-to-use grade calculator that accurately computes average scores based on custom weighting or grading policies
* Secure Login System: Role-based secure login portals for students, teachers, and administrators to ensure data privacy and controlled access
* Teacher Gradebook Access: A dedicated interface for teachers to input, view, and update student grades, with tools to analyze performance over time.

#Domain
The domain of this project lies within the field of educational technology, focusing specifically on digital grade management systems. In modern educational environments, teachers and students rely heavily on accurate and accessible tools to track academic performance. However, many existing systems are outdated, difficult to navigate, or lack key features that promote transparency and engagement. Our project seeks to bridge this gap by developing a platform that integrates intuitive design, secure access, and analytical tools, empowering both educators and learners to better understand and manage academic progress.

Problem Statement:Many schools lack an efficient, secure, and user-friendly system for managing and communicating student grades, resulting in disorganization, limited accessibility, and reduced academic transparency.

#Overall Goal:
* To streamline academic performance tracking while ensuring ease of use, data security, and effective communication between students and teachers.

Installation Set-Up
To set up and run the Student Gradebook project locally:

-Clone the repository from GitHub.
-Navigate to the main project directory.
-(Optional) Create and activate a virtual environment to manage dependencies.
-Install all required dependencies listed in the requirements file.
-Open the examples folder to view and run the demo script
-Explore the source code inside the src folder to understand the project’s structure and functionality.
-Refer to the docs directory for detailed documentation and function usage instructions.

Function List
The project’s main functions are organized within the src/ directory to ensure modularity and clarity. Each team member contributed specific functional components:

Nailah – Grade Management Functions

addGrade(student, grade) – Adds a new grade entry for a student.
updateGrade(student, index, new_grade) – Updates an existing grade.
deleteGrade(gradeId) – Removes a grade from the record.
view_grades() – Displays all recorded grades for review.

Andrew – Filtering Functions

filter_by_assignment_type(grades_list, assignment_type) – Filters grades by assignment type (e.g., quiz, exam, homework).
filter_late_submissions(grades_list) – Filters out all assignments that were submitted late.
filter_by_score_range(grades_list, min_score, max_score) – Filters students based on a score range.
filter_by_student_name(grades_list, student_name) – Retrieves all grade entries for a specific student (case-insensitive).
filter_by_week(grades_list, week_number) – Filters grades submitted in a specific week of the semester.

Matti – User Authentication and Profile Management

loginUser(credentials) – Handles secure login for students and teachers.
getUserRole(userId) – Identifies user type (teacher or student).
updateUserProfile(userId, updates) – Allows users to edit their profile information.

Tidjani – Grade Calculation Functions

calculateAverage(grades) – Calculates the average score from a list of grades.
calculateWeightedAverage(grades, weights) – Computes a weighted average for subjects with different importance levels.
getStudentRanking(classId) – (Optional) Ranks students based on their performance.

Organization Summary

Each module and function in the library follows consistent naming conventions and detailed documentation.
library_name.py serves as the main library containing all core functions.
utils.py may store shared helpers or validation functions.
docs/function_reference.md provides detailed documentation and parameters for each function.
examples/demo_script.py includes practical examples to demonstrate functionality.

Function Example: 

from src.library_name import filter_by_assignment_type

grades = [
    {'name': 'Alex', 'assignment_type': 'quiz', 'score': 85},
    {'name': 'Maria', 'assignment_type': 'exam', 'score': 92},
    {'name': 'Chris', 'assignment_type': 'quiz', 'score': 78}
]

filtered = filter_by_assignment_type(grades, 'quiz')
print(filtered)
 Output: [{'name': 'Alex', 'assignment_type': 'quiz', 'score': 85},
          {'name': 'Chris', 'assignment_type': 'quiz', 'score': 78}]


#Guidline for Team Members

To ensure consistency and collaboration, all team members should follow these contribution standards:

- Branching and Workflow
- Create a new branch for each feature, fix, or enhancement.
- When finished, submit a pull request (PR) for review.
- Commit Messages

Use clear and descriptive messages summarizing your changes.
Example:

git commit -m "Added filter_by_assignment_type function and unit tests"

Code Review

- All pull requests must be reviewed by at least one other team member before merging.
- Provide constructive feedback to maintain code quality and consistency.

Testing

- Test all new code locally before pushing.
- Add test cases or examples when new features are introduced.
