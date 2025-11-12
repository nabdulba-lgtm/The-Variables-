from typing import List, Dict, Optional

class Gradebook:
    """Represents a collection of student grades with filtering and analysis capabilities.
    
    This class encapsulates all grade-related data and provides methods
    to filter and analyze grades based on assignment type, score range, 
    student name, lateness, and week number.
    
    Example:
        >>> grades = [
        ...     {'name': 'Alex', 'assignment_type': 'quiz', 'score': 85, 'is_late': False, 'week': 2},
        ...     {'name': 'Maria', 'assignment_type': 'exam', 'score': 92, 'is_late': True, 'week': 2},
        ...     {'name': 'Sam', 'assignment_type': 'homework', 'score': 70, 'is_late': False, 'week': 3}
        ... ]
        >>> gb = Gradebook(grades)
        >>> gb.filter_by_assignment_type('quiz')
        [{'name': 'Alex', 'assignment_type': 'quiz', 'score': 85, 'is_late': False, 'week': 2}]
    """

    def __init__(self, grades_list: List[Dict]):
        """Initialize the Gradebook with a list of grade records.
        
        Args:
            grades_list (list of dict): List containing grade data.
                Each record should have at least 'name', 'assignment_type', and 'score' keys.
        
        Raises:
            ValueError: If grades_list is not a list or contains invalid entries.
        """
        if not isinstance(grades_list, list):
            raise ValueError("grades_list must be a list of dictionaries")
        for grade in grades_list:
            if not isinstance(grade, dict):
                raise ValueError("Each grade record must be a dictionary")
        
        self._grades = grades_list  # encapsulated data (private)

    # -------------------- PROPERTIES --------------------

    @property
    def grades(self) -> List[Dict]:
        """list of dict: Return all grade records."""
        return self._grades

    @grades.setter
    def grades(self, new_grades: List[Dict]):
        """Set a new list of grades, ensuring valid input."""
        if not isinstance(new_grades, list):
            raise ValueError("grades must be a list of dictionaries")
        self._grades = new_grades

    # -------------------- METHODS --------------------

    def filter_by_assignment_type(self, assignment_type: str) -> List[Dict]:
        """Return all grades for a given assignment type."""
        return [g for g in self._grades if g.get('assignment_type') == assignment_type]

    def filter_late_submissions(self) -> List[Dict]:
        """Return all late submissions (is_late == True)."""
        return [g for g in self._grades if g.get('is_late', False)]

    def filter_by_score_range(self, min_score: int = 0, max_score: int = 100) -> List[Dict]:
        """Return grades with scores within the given range."""
        return [g for g in self._grades if min_score <= g.get('score', 0) <= max_score]

    def filter_by_student_name(self, student_name: str) -> List[Dict]:
        """Return all records for a given student name (case-insensitive)."""
        return [g for g in self._grades if g.get('name', '').lower() == student_name.lower()]

    def filter_by_week(self, week_number: int) -> List[Dict]:
        """Return all grades submitted during a specific week."""
        return [g for g in self._grades if g.get('week') == week_number]

    def add_grade(self, record: Dict):
        """Add a new grade record to the gradebook.
        
        Args:
            record (dict): A dictionary representing a student's grade record.
        
        Raises:
            ValueError: If the record is not a valid dictionary or missing required fields.
        """
        required_keys = {'name', 'assignment_type', 'score'}
        if not isinstance(record, dict) or not required_keys.issubset(record):
            raise ValueError(f"Record must be a dictionary containing {required_keys}")
        self._grades.append(record)

    # -------------------- REPRESENTATIONS --------------------

    def __str__(self):
        return f"Gradebook with {len(self._grades)} records"

    def __repr__(self):
        return f"Gradebook(num_records={len(self._grades)})"

from typing import List, Dict


#--------------------------------------------

class Student:
    """Represents a student with personal info and their grades.

    This class encapsulates student details and allows interaction with
    their grade records through a Gradebook instance.

    Example:
        >>> grades = [
        ...     {'name': 'Alex', 'assignment_type': 'quiz', 'score': 85, 'is_late': False, 'week': 2},
        ...     {'name': 'Alex', 'assignment_type': 'exam', 'score': 92, 'is_late': True, 'week': 2}
        ... ]
        >>> from gradebook import Gradebook
        >>> gb = Gradebook(grades)
        >>> student = Student('Alex Johnson', 'INST326', gb)
        >>> student.get_average()
        88.5
        >>> student.add_grade({'name': 'Alex Johnson', 'assignment_type': 'homework', 'score': 78, 'is_late': False, 'week': 3})
        >>> student.get_average()
        85.0
    """

    def __init__(self, name: str, course: str, gradebook):
        """
        Initialize a student.

        Args:
            name (str): Full name of the student.
            course (str): Course name or code.
            gradebook (Gradebook): Gradebook instance containing this student's grades.

        Raises:
            ValueError: If name or course is empty, or gradebook is not a Gradebook instance.
        """
        if not name.strip():
            raise ValueError("Student name cannot be empty")
        if not course.strip():
            raise ValueError("Course cannot be empty")
        if not hasattr(gradebook, 'grades'):
            raise ValueError("gradebook must be a Gradebook instance")

        self._name = name
        self._course = course
        self._gradebook = gradebook

    # -------------------- PROPERTIES --------------------
    @property
    def name(self) -> str:
        """str: Get the student's name (read-only)."""
        return self._name

    @property
    def course(self) -> str:
        """str: Get the course name (read-only)."""
        return self._course

    @property
    def gradebook(self):
        """Gradebook: Get the gradebook instance associated with the student."""
        return self._gradebook

    # -------------------- METHODS --------------------
    def get_grades(self) -> List[Dict]:
        """Return all grade records for this student."""
        return self._gradebook.filter_by_student_name(self._name)

    def get_average(self) -> float:
        """Calculate and return the average score for this student.

        Returns:
            float: Average score across all assignments, or 0 if no grades.
        """
        grades = self.get_grades()
        if not grades:
            return 0.0
        total = sum(g['score'] for g in grades)
        return round(total / len(grades), 2)

    def add_grade(self, record: Dict):
        """Add a new grade record for this student.

        Args:
            record (dict): Dictionary containing grade info.

        Raises:
            ValueError: If the record does not belong to this student.
        """
        if record.get('name') != self._name:
            raise ValueError("Cannot add grade for a different student")
        self._gradebook.add_grade(record)

    # -------------------- REPRESENTATIONS --------------------
    def __str__(self):
        return f"{self._name} ({self._course}) - Average: {self.get_average()}"

    def __repr__(self):
        return f"Student(name='{self._name}', course='{self._course}', average={self.get_average()})"

class Assignment:
    """Represents an assignment with grading information.
    
    Example:
        >>> assignment = Assignment('Midterm', 'exam', max_points=100, week=8)
        >>> assignment.calculate_percentage(85)
        85.0
    """

    def __init__(self, name: str, assignment_type: str, max_points: float = 100, week: int = 1):
        """Initialize an assignment."""
        if not name.strip():
            raise ValueError("Assignment name cannot be empty")
        if max_points <= 0:
            raise ValueError("max_points must be positive")
        self._name = name
        self._assignment_type = assignment_type.lower()
        self._max_points = float(max_points)
        self._week = week

    @property
    def name(self) -> str:
        return self._name

    @property
    def assignment_type(self) -> str:
        return self._assignment_type

    @property
    def max_points(self) -> float:
        return self._max_points

    @property
    def week(self) -> int:
        return self._week

    def calculate_percentage(self, points_earned: float) -> Optional[float]:
        """Calculate percentage grade."""
        if points_earned < 0:
            return None
        return round((points_earned / self._max_points) * 100, 2)

    def create_grade_record(self, student_name: str, points_earned: float, is_late: bool = False) -> Dict:
        """Create a grade record dictionary."""
        if not student_name.strip():
            raise ValueError("student_name cannot be empty")
        if points_earned < 0 or points_earned > self._max_points:
            raise ValueError(f"points_earned must be between 0 and {self._max_points}")
        return {
            'name': student_name,
            'assignment_type': self._assignment_type,
            'score': points_earned,
            'is_late': is_late,
            'week': self._week
        }

    def __str__(self):
        return f"{self._name} ({self._assignment_type}) - {self._max_points} pts, Week {self._week}"

    def __repr__(self):
        return f"Assignment('{self._name}', '{self._assignment_type}', {self._max_points}, week={self._week})"


class Course:
    """Represents a course with enrolled students.
    
    Example:
        >>> course = Course('INST326', 'Object-Oriented Programming', 'Dr. Johnson')
        >>> course.get_enrollment_count()
        0
    """

    def __init__(self, course_code: str, course_name: str, instructor_name: str):
        """Initialize a course."""
        if not course_code.strip():
            raise ValueError("course_code cannot be empty")
        if not course_name.strip():
            raise ValueError("course_name cannot be empty")
        if not instructor_name.strip():
            raise ValueError("instructor_name cannot be empty")
        self._course_code = course_code.upper()
        self._course_name = course_name
        self._instructor_name = instructor_name
        self._students = []

    @property
    def course_code(self) -> str:
        return self._course_code

    @property
    def course_name(self) -> str:
        return self._course_name

    @property
    def instructor_name(self) -> str:
        return self._instructor_name

    @property
    def students(self) -> List:
        return self._students

    def add_student(self, student):
        """Enroll a student."""
        if not isinstance(student, Student):
            raise ValueError("Must provide a Student instance")
        if student in self._students:
            raise ValueError(f"{student.name} already enrolled")
        self._students.append(student)

    def get_enrollment_count(self) -> int:
        """Get number of enrolled students."""
        return len(self._students)

    def get_course_average(self) -> float:
        """Calculate average grade across all students."""
        if not self._students:
            return 0.0
        total = sum(s.get_average() for s in self._students)
        return round(total / len(self._students), 2)

    def get_students_by_performance(self, min_score: float = 0, max_score: float = 100) -> List:
        """Get students with averages in score range."""
        return [s for s in self._students if min_score <= s.get_average() <= max_score]

    def __str__(self):
        return f"{self._course_code}: {self._course_name} ({len(self._students)} students)"

    def __repr__(self):
        return f"Course('{self._course_code}', '{self._course_name}')"


class Teacher:
    """Represents a teacher who manages courses.
    
    Example:
        >>> teacher = Teacher('Dr. Johnson', 'Information Science')
        >>> teacher.get_courses_taught()
        []
    """

    def __init__(self, name: str, department: str, username: str = None):
        """Initialize a teacher."""
        if not name.strip():
            raise ValueError("Teacher name cannot be empty")
        if not department.strip():
            raise ValueError("Department cannot be empty")
        self._name = name
        self._department = department
        self._username = username if username else name.lower().replace(' ', '_')
        self._courses = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def department(self) -> str:
        return self._department

    @property
    def username(self) -> str:
        return self._username

    @property
    def courses(self) -> List:
        return self._courses

    def add_course(self, course):
        """Add a course to teaching load."""
        if not isinstance(course, Course):
            raise ValueError("Must provide a Course instance")
        if course in self._courses:
            raise ValueError(f"Already teaching {course.course_code}")
        self._courses.append(course)

    def get_courses_taught(self) -> List[str]:
        """Get list of course codes taught."""
        return [c.course_code for c in self._courses]

    def add_grade_to_student(self, course, student, assignment, points_earned: float, is_late: bool = False):
        """Add a grade for a student in a course."""
        if course not in self._courses:
            raise ValueError(f"Not teaching {course.course_code}")
        if student not in course.students:
            raise ValueError(f"{student.name} not enrolled in {course.course_code}")
        grade_record = assignment.create_grade_record(student.name, points_earned, is_late)
        student.add_grade(grade_record)

    def get_total_students(self) -> int:
        """Get total unique students across all courses."""
        all_students = set()
        for course in self._courses:
            all_students.update(course.students)
        return len(all_students)

    def __str__(self):
        return f"Teacher: {self._name} ({self._department}) - {len(self._courses)} course(s)"

    def __repr__(self):
        return f"Teacher('{self._name}', '{self._department}')"
