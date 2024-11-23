from sqlalchemy import create_engine
from tables import students_df, courses_df, enrollments_df


# Create a SQLite database
engine = create_engine('sqlite:///school_management_system.db')

# Save DataFrames to the database
students_df.to_sql('students', con=engine, if_exists='replace', index=False)
courses_df.to_sql('courses', con=engine, if_exists='replace', index=False)
enrollments_df.to_sql('enrollments', con=engine, if_exists='replace', index=False)