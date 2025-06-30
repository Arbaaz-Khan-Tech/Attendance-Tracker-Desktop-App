# attendance_app/app/models/attendance_model.py

class Attendance:
    def __init__(self, attendance_id: str, student_id: str, faculty_id: str, subject: str, date: str, status: str):
        self.attendance_id = attendance_id        # Unique ID for attendance entry
        self.student_id = student_id              # ID of the student (foreign key)
        self.faculty_id = faculty_id              # ID of faculty who marked attendance
        self.subject = subject                    # Subject name
        self.date = date                          # Date as string (e.g., "2025-06-25")
        self.status = status                      # "present" or "absent"

    def to_dict(self) -> dict:
        return {
            "attendance_id": self.attendance_id,
            "student_id": self.student_id,
            "faculty_id": self.faculty_id,
            "subject": self.subject,
            "date": self.date,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            attendance_id=data.get("attendance_id", ""),
            student_id=data.get("student_id", ""),
            faculty_id=data.get("faculty_id", ""),
            subject=data.get("subject", ""),
            date=data.get("date", ""),
            status=data.get("status", "")
        )

    def __str__(self):
        return f"[{self.date}] {self.student_id} - {self.subject}: {self.status.upper()}"
