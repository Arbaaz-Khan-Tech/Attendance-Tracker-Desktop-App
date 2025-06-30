# app/views/add_student_view.py

import customtkinter as ctk
from attendance_app.app.models.student_model import Student

class AddStudentView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.appwrite = controller.appwrite

        ctk.CTkLabel(self, text="Add Student", font=("Arial", 20)).pack(pady=20)

        self.entries = {}

        for label in ["ID", "Name", "Roll Number", "Department"]:
            ctk.CTkLabel(self, text=label).pack()
            entry = ctk.CTkEntry(self)
            entry.pack()
            self.entries[label.lower().replace(" ", "_")] = entry

        ctk.CTkButton(self, text="Submit", command=self.submit_student).pack(pady=10)
        ctk.CTkButton(self, text="⬅ Back", command=self.go_back).pack(pady=5)

    def submit_student(self):
        student = Student(
            student_id=self.entries["id"].get(),
            name=self.entries["name"].get(),
            roll_number=self.entries["roll_number"].get(),
            department=self.entries["department"].get()
        )
        result = self.appwrite.create_student(student)
        print("Student added:", result)
        self.go_back()

    def go_back(self):
        from attendance_app.app.views.department_view import DepartmentSelectorView  # ✅ Move import here
        self.controller.show_view(DepartmentSelectorView)
