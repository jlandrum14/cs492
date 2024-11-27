
import tkinter as tk
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = "sqlite:///school_management_system.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class StudentManagement:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Management")

    def add_student(self, first_name, last_name, dob):
        session = Session()
        session.execute(
            f"INSERT INTO students (first_name, last_name, date_of_birth) VALUES ('{first_name}', '{last_name}', '{dob}')"
        )
        session.commit()
        session.close()
        self.display_students()

    def display_students(self):
        session = Session()
        df = pd.read_sql("SELECT * FROM students", con=engine)
        print(df)  # Debugging: Replace with GUI table display
        session.close()

    def run(self):
        tk.Label(self.root, text="First Name").grid(row=0, column=0)
        first_name_entry = tk.Entry(self.root)
        first_name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Last Name").grid(row=1, column=0)
        last_name_entry = tk.Entry(self.root)
        last_name_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Date of Birth").grid(row=2, column=0)
        dob_entry = tk.Entry(self.root)
        dob_entry.grid(row=2, column=1)

        tk.Button(self.root, text="Add Student", command=lambda: self.add_student(
            first_name_entry.get(),
            last_name_entry.get(),
            dob_entry.get()
        )).grid(row=3, column=1)

        tk.Button(self.root, text="Display Students", command=self.display_students).grid(row=4, column=1)
        tk.Button(self.root, text="Exit", command=self.root.destroy).grid(row=5, column=1)
        self.root.mainloop()
