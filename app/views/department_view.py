import customtkinter as ctk
from attendance_app.app.views.department_detail_view import DepartmentDetailView
from attendance_app.app.views.AddStudentView import AddStudentView
from attendance_app.app.views.AddFacultyView import AddFacultyView


class DepartmentSelectorView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.appwrite = controller.appwrite
        self.configure(fg_color="#F8FBFF")  # white-blue background

        title = ctk.CTkLabel(
            self,
            text="🏢 Select a Department",
            font=ctk.CTkFont("Quicksand", 26, weight="bold"),
            text_color="#1B3C73"
        )
        title.pack(pady=(40, 20))

        self.card_container = ctk.CTkScrollableFrame(self, fg_color="#F8FBFF")
        self.card_container.pack(expand=True, fill="both", padx=30, pady=10)

        self.build_department_cards()

        # Add action cards
        self.build_action_card("➕ Add Student", self.open_add_student_form)
        self.build_action_card("➕ Add Faculty", self.open_add_faculty_form)

    def build_department_cards(self):
        departments = self.appwrite.get_all_departments()

        for dept in departments:
            frame = ctk.CTkFrame(self.card_container,
                                 fg_color="#E5F1FB",
                                 corner_radius=16,
                                 height=80)
            frame.pack(pady=15, fill="x", padx=10)

            label = ctk.CTkLabel(frame,
                                 text=f"🏷️  {dept}",
                                 font=ctk.CTkFont("Quicksand", 20),
                                 text_color="#1A4D7D")
            label.pack(side="left", padx=20)

            open_btn = ctk.CTkButton(frame,
                                     text="➡️ Open",
                                     width=100,
                                     font=("Quicksand", 14),
                                     fg_color="#3DBE29",
                                     hover_color="#32A119",
                                     command=lambda d=dept: self.controller.show_view(DepartmentDetailView, d))
            open_btn.pack(side="right", padx=20)

    def build_action_card(self, label_text, command):
        frame = ctk.CTkFrame(self.card_container,
                             fg_color="#D9FBE8",
                             corner_radius=16,
                             height=80)
        frame.pack(pady=15, fill="x", padx=10)

        label = ctk.CTkLabel(frame,
                             text=label_text,
                             font=ctk.CTkFont("Quicksand", 20),
                             text_color="#14532D")
        label.pack(side="left", padx=20)

        action_btn = ctk.CTkButton(frame,
                                   text="Open Form",
                                   width=120,
                                   font=("Quicksand", 14),
                                   fg_color="#199A63",
                                   hover_color="#157F52",
                                   command=command)
        action_btn.pack(side="right", padx=20)

    def open_add_student_form(self):
        self.controller.show_view(AddStudentView)

    def open_add_faculty_form(self):
        self.controller.show_view(AddFacultyView)
