import customtkinter as ctk
from attendance_app.app.views.attendance_summary_view import AttendanceSummaryView

class DepartmentDetailView(ctk.CTkFrame):
    def __init__(self, parent, controller, department_name):
        super().__init__(parent)
        self.controller = controller
        self.appwrite = controller.appwrite
        self.department = department_name

        ctk.CTkLabel(self, text=f"Department: {self.department}", font=("Arial", 20)).pack(pady=20)

        ctk.CTkButton(self, text="📚 Show Students", command=self.show_students).pack(pady=5)
        ctk.CTkButton(self, text="👩‍🏫 Show Faculty", command=self.show_faculty).pack(pady=5)
        ctk.CTkButton(self, text="✅ Take Attendance", command=self.take_attendance).pack(pady=10)
        ctk.CTkButton(self, text="📊 View Attendance Summary", command=self.view_summary).pack(pady=5)
        ctk.CTkButton(self, text="⬅ Back", command=self.go_back).pack(pady=10)
        # Add below existing buttons
        self.output_frame = ctk.CTkScrollableFrame(self, width=500, height=300)
        self.output_frame.pack(pady=10, fill="both", expand=True)


    def show_students(self):
     for widget in self.output_frame.winfo_children():
        widget.destroy()

     students = self.appwrite.get_students_by_department(self.department)
     print(f"[DEBUG] Students in {self.department}:", students)

     if not students:
        ctk.CTkLabel(self.output_frame, text="No students found").pack(pady=5)
        return

     for s in students:
        ctk.CTkLabel(
            self.output_frame,
            text=f"{s.name} ({s.roll_number})",
            anchor="w"
        ).pack(fill="x", padx=10, pady=2)

    def show_faculty(self):
     for widget in self.output_frame.winfo_children():
        widget.destroy()

     faculty = self.appwrite.get_faculty_by_department(self.department)
     print(f"[DEBUG] Faculty in {self.department}:", faculty)

     if not faculty:
        ctk.CTkLabel(self.output_frame, text="No faculty found").pack(pady=5)
        return

     for f in faculty:
        ctk.CTkLabel(
            self.output_frame,
            text=f"{f.faculty_name} (ID: {f.faculty_id})",
            anchor="w"
        ).pack(fill="x", padx=10, pady=2)


    def take_attendance(self):
        from attendance_app.app.views.attendance_view import AttendanceView
        self.controller.show_view(AttendanceView, self.department)

    def view_summary(self):
        self.controller.show_view(AttendanceSummaryView, self.department)


    def go_back(self):
        from attendance_app.app.views.department_view import DepartmentSelectorView
        self.controller.show_view(DepartmentSelectorView)
