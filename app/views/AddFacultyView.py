# app/views/add_faculty_view.py

import customtkinter as ctk
from attendance_app.app.models.faculty_model import Faculty

class AddFacultyView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.appwrite = controller.appwrite

        ctk.CTkLabel(self, text="Add Faculty", font=("Arial", 20)).pack(pady=20)

        self.entries = {}

        for label in ["ID", "Name", "Department"]:
            ctk.CTkLabel(self, text=label).pack()
            entry = ctk.CTkEntry(self)
            entry.pack()
            self.entries[label.lower().replace(" ", "_")] = entry
            from attendance_app.app.views.department_view import DepartmentSelectorView 

        ctk.CTkButton(self, text="Submit", command=self.submit_faculty).pack(pady=10)
        ctk.CTkButton(self, text="⬅ Back", command=lambda: self.controller.show_view(DepartmentSelectorView)).pack(pady=5)
        

    def submit_faculty(self):
        faculty = Faculty(
            faculty_id=self.entries["id"].get(),
            faculty_name=self.entries["name"].get(),
            faculty_department=self.entries["department"].get()
        )
        result = self.appwrite.create_faculty(faculty)
        print("Faculty added:", result)
        self.go_back()

    def go_back(self):
        from attendance_app.app.views.department_view import DepartmentSelectorView  # ✅ Move import here
        self.controller.show_view(DepartmentSelectorView)
