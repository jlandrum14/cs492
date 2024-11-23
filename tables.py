import pandas as pd

# Define the Students table
students_data = {
    'student_id': [1, 2, 3],
    'first_name': ['John', 'Jane', 'Jim'],
    'last_name': ['Doe', 'Smith', 'Brown'],
    'date_of_birth': pd.to_datetime(['2000-01-01', '2001-02-02', '2002-03-03'])
}
students_df = pd.DataFrame(students_data)

# Define the Courses table
courses_data = {
    'course_id': [101, 102, 103],
    'course_name': ['Mathematics', 'Science', 'History'],
    'credits': [3, 4, 3]
}
courses_df = pd.DataFrame(courses_data)

# Define the Enrollments table
enrollments_data = {
    'enrollment_id': [1, 2, 3],
    'student_id': [1, 2, 1],
    'course_id': [101, 102, 103],
    'enrollment_date': pd.to_datetime(['2023-08-01', '2023-08-01', '2023-08-02'])
}
enrollments_df = pd.DataFrame(enrollments_data)