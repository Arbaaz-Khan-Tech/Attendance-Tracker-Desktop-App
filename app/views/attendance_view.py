import customtkinter as ctk
from datetime import datetime
from attendance_app.app.models.attendance_model import Attendance

class AttendanceView(ctk.CTkFrame):
    def __init__(self, parent, controller, department):
        super().__init__(parent)
        self.controller = controller
        self.appwrite = controller.appwrite
        self.department = department
        self.attendance_data = {}

        ctk.CTkLabel(self, text=f"Take Attendance - {self.department}", font=("Arial", 20)).pack(pady=10)

        self.date_entry = ctk.CTkEntry(self, placeholder_text="YYYY-MM-DD")
        self.date_entry.pack(pady=5)
        self.date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

        self.subject_entry = ctk.CTkEntry(self, placeholder_text="Subject")
        self.subject_entry.pack(pady=5)

        self.student_container = ctk.CTkScrollableFrame(self, height=300)
        self.student_container.pack(pady=10, fill="both", expand=True)

        self.mark_buttons = {}
        self.build_student_list()

        ctk.CTkButton(self, text="✅ Submit Attendance", command=self.submit_attendance).pack(pady=10)
        ctk.CTkButton(self, text="⬅ Back", command=self.go_back).pack(pady=5)

    def build_student_list(self):
        students = self.appwrite.get_students_by_department(self.department)
        for student in students:
            student_id = student.student_id
            frame = ctk.CTkFrame(self.student_container)
            frame.pack(fill="x", pady=5, padx=10)

            label = ctk.CTkLabel(frame, text=f"{student.name} ({student.roll_number})")
            label.pack(side="left")

            button = ctk.CTkButton(
                frame,
                text="Mark Present",
                command=lambda sid=student_id: self.mark_present(sid)
            )
            button.pack(side="right")
            self.mark_buttons[student_id] = button

    def mark_present(self, student_id):
        self.attendance_data[student_id] = "present"
        self.mark_buttons[student_id].configure(text="Present ✅", fg_color="green", state="disabled")

    def submit_attendance(self):
        subject = self.subject_entry.get().strip().upper()
        date = self.date_entry.get().strip()
        students = self.appwrite.get_students_by_department(self.department)

        for student in students:
            status = self.attendance_data.get(student.student_id, "absent")
            attendance = Attendance(
                attendance_id=f"att_{student.student_id}_{date}",
                student_id=student.student_id,
                faculty_id="FAC_001",  # replace or fetch dynamically if needed
                subject=subject,
                date=date,
                status=status
            )
            self.appwrite.mark_attendance(attendance)
        print("✅ Attendance submitted!")

    def go_back(self):
        from attendance_app.app.views.department_detail_view import DepartmentDetailView
        self.controller.show_view(DepartmentDetailView, self.department)
