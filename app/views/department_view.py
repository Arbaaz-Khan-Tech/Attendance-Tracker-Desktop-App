# app/views/department_selector_view.py

import customtkinter as ctk
from attendance_app.app.views.department_detail_view import DepartmentDetailView
from attendance_app.app.views.AddStudentView import AddStudentView
from attendance_app.app.views.AddFacultyView import AddFacultyView


class DepartmentSelectorView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.appwrite = controller.appwrite

        ctk.CTkLabel(self, text="Select a Department", font=("Arial", 20)).pack(pady=20)

        self.build_department_buttons()

        ctk.CTkButton(self, text="➕ Add Student", command=self.open_add_student_form).pack(pady=5)
        ctk.CTkButton(self, text="➕ Add Faculty", command=self.open_add_faculty_form).pack(pady=5)

    def build_department_buttons(self):
        departments = self.appwrite.get_all_departments()
        for dept in departments:
            btn = ctk.CTkButton(
                self,
                text=dept,
                command=lambda d=dept: self.open_department_page(d)
            )
            btn.pack(pady=10, padx=20, fill="x")

    def open_department_page(self, dept_name):
        self.controller.show_view(DepartmentDetailView, dept_name)

    def open_add_student_form(self):
        self.controller.show_view(AddStudentView)

    def open_add_faculty_form(self):
        self.controller.show_view(AddFacultyView)
