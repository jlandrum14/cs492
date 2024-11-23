import pandas as pd
import numpy as np
from faker import Faker
from sqlalchemy import create_engine

# Initialize Faker for generating random data
fake = Faker()

# Set a random seed for reproducibility
np.random.seed(42)

# Generate seed data for Students
num_students = 10
students_data = {
    'student_id': np.arange(1, num_students + 1),
    'first_name': [fake.first_name() for _ in range(num_students)],
    'last_name': [fake.last_name() for _ in range(num_students)],
    'date_of_birth': [fake.date_of_birth(minimum_age=18, maximum_age=25) for _ in range(num_students)]
}
students_df = pd.DataFrame(students_data)

# Generate seed data for Courses
num_courses = 5
courses_data = {
    'course_id': np.arange(101, 101 + num_courses),
    'course_name': [fake.word().capitalize() + " 101" for _ in range(num_courses)],
    'credits': np.random.choice([3, 4], size=num_courses)
}
courses_df = pd.DataFrame(courses_data)

# Generate seed data for Enrollments
num_enrollments = 15
enrollments_data = {
    'enrollment_id': np.arange(1, num_enrollments + 1),
    'student_id': np.random.choice(students_df['student_id'], size=num_enrollments),
    'course_id': np.random.choice(courses_df['course_id'], size=num_enrollments),
    'enrollment_date': [fake.date_this_year() for _ in range(num_enrollments)]
}
enrollments_df = pd.DataFrame(enrollments_data)

# Display the generated data
print("Students DataFrame:")
print(students_df)
print("\nCourses DataFrame:")
print(courses_df)
print("\nEnrollments DataFrame:")
print(enrollments_df)


# Create a SQLite database
engine = create_engine('sqlite:///school_management_system.db')

# Save the generated DataFrames to the database
students_df.to_sql('students', con=engine, if_exists='replace', index=False)
courses_df.to_sql('courses', con=engine, if_exists='replace', index=False)
enrollments_df.to_sql('enrollments', con=engine, if_exists='replace', index=False)