import customtkinter as ctk
from datetime import datetime


class AttendanceSummaryView(ctk.CTkFrame):
    def __init__(self, parent, controller, department):
        super().__init__(parent)
        self.controller = controller
        self.appwrite = controller.appwrite
        self.department = department

        self.from_date = ctk.StringVar()
        self.to_date = ctk.StringVar()
        self.sort_by = ctk.StringVar(value="name")

        ctk.CTkLabel(self, text=f"📊 Attendance Summary - {self.department}", font=("Arial", 20)).pack(pady=10)

        self.build_filter_section()
        self.result_frame = ctk.CTkScrollableFrame(self)
        self.result_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Back Button
        ctk.CTkButton(self, text="⬅ Back", command=self.go_back).pack(pady=10)

    def build_filter_section(self):
        filter_frame = ctk.CTkFrame(self)
        filter_frame.pack(pady=10, fill="x")

        # Date inputs
        ctk.CTkLabel(filter_frame, text="From:").pack(side="left", padx=5)
        ctk.CTkEntry(filter_frame, textvariable=self.from_date, width=100).pack(side="left")
        ctk.CTkLabel(filter_frame, text="To:").pack(side="left", padx=5)
        ctk.CTkEntry(filter_frame, textvariable=self.to_date, width=100).pack(side="left")

        # Sorting dropdown
        ctk.CTkLabel(filter_frame, text="Sort by:").pack(side="left", padx=10)
        ctk.CTkOptionMenu(filter_frame, variable=self.sort_by,
                          values=["name", "roll_number", "subject", "attendance_percent"],
                          command=lambda x: self.fetch_attendance()).pack(side="left")

        ctk.CTkButton(filter_frame, text="🔍 Show", command=self.fetch_attendance).pack(side="left", padx=10)

    def fetch_attendance(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        from_date = self.from_date.get()
        to_date = self.to_date.get()
        records = self.appwrite.get_attendance_in_range(from_date, to_date)

        grouped = {}
        for rec in records:
            sid = rec["student_id"]
            grouped.setdefault(sid, []).append(rec)

        summary = []
        for sid, recs in grouped.items():
            student = self.appwrite.get_student_by_id(sid)
            if not student or student.department != self.department:
                continue

            total = len(recs)
            present = sum(1 for r in recs if r["status"] == "present")
            percent = round((present / total) * 100, 2) if total else 0
            summary.append({
                "name": student.name,
                "roll": student.roll_number,
                "subject": recs[0]["subject"] if recs else "UNKNOWN",
                "present": present,
                "total": total,
                "percent": percent
            })

        key = self.sort_by.get()
        summary.sort(key=lambda x: x[key] if key != "attendance_percent" else -x["percent"])

        for i, s in enumerate(summary):
            ctk.CTkLabel(
                self.result_frame,
                text=f"{i+1}. {s['name']} ({s['roll']}) | {s['subject']} | {s['present']}/{s['total']} | {s['percent']}%"
            ).pack(anchor="w", padx=10, pady=3)

    def go_back(self):
        from attendance_app.app.views.department_detail_view import DepartmentDetailView
        self.controller.show_view(DepartmentDetailView, self.department)
