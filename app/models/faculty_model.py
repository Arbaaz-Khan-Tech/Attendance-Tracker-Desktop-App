# attendance_app/app/models/faculty_model.py

class Faculty:
    def __init__(self, faculty_name: str, faculty_id: str, faculty_department: str):
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name
        self.faculty_department = faculty_department

    def to_dict(self) -> dict:
        return {
            "faculty_id": self.faculty_id,
            "faculty_name": self.faculty_name,
            "faculty_department": self.faculty_department
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            faculty_id=data.get("faculty_id", ""),
            faculty_name=data.get("faculty_name", ""),
            faculty_department=data.get("faculty_department", "")
        )

    def __str__(self):
        return f"{self.faculty_name} ({self.faculty_id}) - {self.faculty_department}"
