def filter_by_assignment_type(grades_list, assignment_type):
    """Filter grades by assignment type.
    
    Args:
        grades_list (list of dict): List of grade records. 
            Each record should include 'assignment_type' key.
        assignment_type (str): Type of assignment (e.g., 'quiz', 'exam', 'homework') to filter by.
    
    Returns:
        list of dict: Filtered list containing only grades matching the assignment type.
    
    Example:
        >>> grades = [{'name': 'Alex', 'assignment_type': 'quiz', 'score': 85},
        ...           {'name': 'Maria', 'assignment_type': 'exam', 'score': 92}]
        >>> filter_by_assignment_type(grades, 'quiz')
        [{'name': 'Alex', 'assignment_type': 'quiz', 'score': 85}]
    """
    return [grade for grade in grades_list if grade.get('assignment_type') == assignment_type]

def filter_late_submissions(grades_list):
    """Filter out all assignments that were submitted late.
    
    Args:
        grades_list (list of dict): List of grade records. 
            Each record should include a boolean key 'is_late'.
    
    Returns:
        list of dict: List containing only late submissions.
    
    Example:
        >>> grades = [{'name': 'Alex', 'is_late': True}, {'name': 'Maria', 'is_late': False}]
        >>> filter_late_submissions(grades)
        [{'name': 'Alex', 'is_late': True}]
    """
    return [grade for grade in grades_list if grade.get('is_late', False)]

def filter_by_score_range(grades_list, min_score=0, max_score=100):
    """Filter students based on a score range.
    
    Args:
        grades_list (list of dict): List of grade records.
            Each record should include a 'score' key.
        min_score (int, optional): Minimum score to include. Defaults to 0.
        max_score (int, optional): Maximum score to include. Defaults to 100.
    
    Returns:
        list of dict: List of grades where scores fall within the given range.
    
    Example:
        >>> grades = [{'name': 'Alex', 'score': 85}, {'name': 'Maria', 'score': 60}]
        >>> filter_by_score_range(grades, 70, 90)
        [{'name': 'Alex', 'score': 85}]
    """
    return [grade for grade in grades_list if min_score <= grade.get('score', 0) <= max_score]

def filter_by_student_name(grades_list, student_name):
    """Filter all records for a specific student.
    
    Args:
        grades_list (list of dict): List of grade records.
            Each record should include a 'name' key.
        student_name (str): Student name to filter by (case-insensitive).
    
    Returns:
        list of dict: List of all grade entries for the given student.
    
    Example:
        >>> grades = [{'name': 'Alex', 'score': 85}, {'name': 'alex', 'score': 90}]
        >>> filter_by_student_name(grades, 'Alex')
        [{'name': 'Alex', 'score': 85}, {'name': 'alex', 'score': 90}]
    """
    return [grade for grade in grades_list if grade.get('name', '').lower() == student_name.lower()]

def filter_by_week(grades_list, week_number):
    """Filter grades submitted in a specific week.
    
    Args:
        grades_list (list of dict): List of grade records.
            Each record should include a 'week' key.
        week_number (int): Week number to filter (e.g., 1–16).
    
    Returns:
        list of dict: Grades recorded in the specified week.
    
    Example:
        >>> grades = [{'name': 'Alex', 'week': 1, 'score': 80},
        ...           {'name': 'Maria', 'week': 2, 'score': 90}]
        >>> filter_by_week(grades, 1)
        [{'name': 'Alex', 'week': 1, 'score': 80}]
    """
    return [grade for grade in grades_list if grade.get('week') == week_number]
