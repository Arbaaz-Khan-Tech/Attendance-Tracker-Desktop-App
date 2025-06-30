# attendance_app/app/models/student_model.py

class Student:
    def __init__(self, student_id: str, name: str, roll_number: str, department: str):
        self.student_id = student_id
        self.name = name
        self.roll_number = roll_number
        self.department = department

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "roll_number": self.roll_number,
            "department": self.department
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            student_id=data.get("student_id", ""),
            name=data.get("name", ""),
            roll_number=data.get("roll_number", ""),
            department=data.get("department", "")
        )

    def __str__(self):
        return f"{self.name} ({self.roll_number}) - {self.department}"
