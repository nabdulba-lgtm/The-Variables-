import pytest
from assignment_base import AbstractAssignment
from homework_quiz_project import Homework, Quiz, Project
from student import Student
from gradebook import Gradebook

def test_polymorphism():
    hw = Homework("HW", 80, 100)
    qz = Quiz("QZ", 8, 10)
    pj = Project("PJ", 90, 100)

    assert hw.calculate_score_percentage() == 80
    assert round(qz.calculate_score_percentage(), 1) == 96     # 8/10 * 1.2
    assert pj.calculate_score_percentage() == 81               # 90%

def test_inheritance_structure():
    hw = Homework("HW", 10, 10)
    assert isinstance(hw, AbstractAssignment)  # homework inherits from ABC

def test_composition_student_holds_assignments():
    s = Student("1", "Test")
    s.enroll("Math")
    hw = Homework("HW", 100, 100)
    s.add_assignment("Math", hw)
    assert "HW" in s.grades["Math"]

def test_gradebook_add_update_delete():
    g = Gradebook()
    s = Student("1", "Test")
    s.enroll("Math")
    g.add_student(s)

    hw = Homework("HW", 80, 100)
    g.add_assignment_grade("1", "Math", hw)
    assert "HW" in g.students["1"].grades["Math"]

    g.update_assignment_grade("1", "Math", "HW", 90, 100)
    assert g.students["1"].grades["Math"]["HW"].calculate_score_percentage() == 90

    g.delete_assignment_grade("1", "Math", "HW")
    assert "HW" not in g.students["1"].grades["Math"]

import pytest
from abc import ABC
from your_module import AbstractAssignment, Homework, Quiz, Project, Student, Gradebook
# NOTE: replace `your_module` with the actual filename where your classes are


# -------------------------------
#  TEST: POLYMORPHISM SCORING
# -------------------------------
def test_polymorphism():
    hw = Homework("HW", 80, 100)
    qz = Quiz("QZ", 8, 10)
    pj = Project("PJ", 90, 100)

    assert hw.calculate_score_percentage() == 80
    assert round(qz.calculate_score_percentage(), 1) == 96
    assert pj.calculate_score_percentage() == 81


# -------------------------------
#  TEST: INHERITANCE STRUCTURE
# -------------------------------
def test_inheritance_structure():
    hw = Homework("HW", 10, 10)
    assert isinstance(hw, AbstractAssignment)
    assert issubclass(Homework, AbstractAssignment)
    assert issubclass(Quiz, AbstractAssignment)
    assert issubclass(Project, AbstractAssignment)


# -------------------------------
#  TEST: CANNOT INSTANTIATE ABSTRACT CLASS
# -------------------------------
def test_cannot_instantiate_abstract_assignment():
    with pytest.raises(TypeError):
        AbstractAssignment("Test", 10, 10)  # abstract class cannot be instantiated


# -------------------------------
#  TEST: ASSIGNMENT UPDATE LOGIC
# -------------------------------
def test_assignment_update_changes_score():
    hw = Homework("HW", 50, 100)
    hw.update(90, 100)
    assert hw.calculate_score_percentage() == 90


# -------------------------------
#  TEST: COMPOSITION — STUDENT HAS CLASSES
# -------------------------------
def test_composition_student_assignments():
    s = Student("1", "Test")
    s.enroll("Math")
    hw = Homework("HW", 100, 100)
    s.add_assignment("Math", hw)
    assert "HW" in s.grades["Math"]


# -------------------------------
#  TEST: STUDENT MUST ENROLL BEFORE ADDING ASSIGNMENT
# -------------------------------
def test_student_add_assignment_without_enrollment_raises():
    s = Student("1", "Test")
    hw = Homework("HW", 100, 100)
    with pytest.raises(KeyError):
        s.add_assignment("Math", hw)


# -------------------------------
#  TEST: GRADEBOOK REQUIRES STUDENT TO EXIST
# -------------------------------
def test_gradebook_add_assignment_missing_student_raises():
    g = Gradebook()
    hw = Homework("HW", 100, 100)
    with pytest.raises(KeyError):
        g.add_assignment_grade("999", "Math", hw)


# -------------------------------
#  TEST: GRADEBOOK REQUIRES STUDENT TO BE ENROLLED
# -------------------------------
def test_gradebook_assignment_without_enrollment_raises():
    g = Gradebook()
    s = Student("1", "Test")
    g.add_student(s)
    hw = Homework("HW", 100, 100)
    with pytest.raises(KeyError):
        g.add_assignment_grade("1", "Math", hw)


# -------------------------------
#  TEST: DELETE MISSING ASSIGNMENT
# -------------------------------
def test_delete_missing_assignment_raises():
    g = Gradebook()
    s = Student("1", "Test")
    s.enroll("Math")
    g.add_student(s)
    with pytest.raises(KeyError):
        g.delete_assignment_grade("1", "Math", "Fake")


# -------------------------------
#  TEST: MULTIPLE ASSIGNMENT TYPES IN LIST (POLYMORPHISM)
# -------------------------------
def test_polymorphism_score_loop():
    assignments = [
        Homework("HW", 80, 100),
        Quiz("QZ", 8, 10),
        Project("PJ", 90, 100)
    ]
    scores = [a.calculate_score_percentage() for a in assignments]

    assert scores[0] == 80
    assert round(scores[1], 1) == 96
    assert scores[2] == 81


# -------------------------------
#  TEST: MULTIPLE CLASSES PER STUDENT
# -------------------------------
def test_student_multiple_classes_independent_assignments():
    s = Student("1", "Test")
    s.enroll("Math")
    s.enroll("Science")

    hw = Homework("HW", 100, 100)
    quiz = Quiz("Quiz", 9, 10)

    s.add_assignment("Math", hw)
    s.add_assignment("Science", quiz)

    assert "HW" in s.grades["Math"]
    assert "Quiz" in s.grades["Science"]
    assert "Quiz" not in s.grades["Math"]


# -------------------------------
#  TEST: UPDATE THROUGH GRADEBOOK UPDATES SCORE
# -------------------------------
def test_update_assignment_changes_percentage_immediately():
    g = Gradebook()
    s = Student("1", "Test")
    s.enroll("Math")
    g.add_student(s)

    pj = Project("Project 1", 70, 100)
    g.add_assignment_grade("1", "Math", pj)

    g.update_assignment_grade("1", "Math", "Project 1", 90, 100)

    assert pj.calculate_score_percentage() == 81


# -------------------------------
#  TEST: FULL WORKFLOW
# -------------------------------
def test_full_workflow_end_to_end():
    g = Gradebook()
    s = Student("1", "Test")
    s.enroll("Math")
    g.add_student(s)

    hw = Homework("HW 1", 75, 100)
    g.add_assignment_grade("1", "Math", hw)
    assert "HW 1" in s.grades["Math"]

    g.update_assignment_grade("1", "Math", "HW 1", 95, 100)
    assert hw.calculate_score_percentage() == 95

    g.delete_assignment_grade("1", "Math", "HW 1")
    assert "HW 1" not in s.grades["Math"]

Test: 
def test_polymorphism():
    hw = Homework("HW", 80, 100)
    qz = Quiz("QZ", 8, 10)
    pj = Project("PJ", 90, 100)

    assert hw.calculate_score_percentage() == 80
    assert round(qz.calculate_score_percentage(), 1) == 96
    assert pj.calculate_score_percentage() == 81


def test_inheritance_structure():
    hw = Homework("HW", 10, 10)
    assert isinstance(hw, AbstractAssignment)


def test_composition():
    s = Student("1", "Test")
    s.enroll("Math")
    hw = Homework("HW", 100, 100)
    s.add_assignment("Math", hw)
    assert "HW" in s.grades["Math"]

