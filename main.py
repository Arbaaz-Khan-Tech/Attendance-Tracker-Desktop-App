# attendance_app/main.py

from attendance_app.app.services.appwrite_service import AppwriteService
from attendance_app.app.models.student_model import Student

from attendance_app.app.models.faculty_model import Faculty
from attendance_app.app.models.attendance_model import Attendance

from attendance_app.app.views.department_view import DepartmentSelectorView

import customtkinter as ctk





class MainApp(ctk.CTk):
    def __init__(self, appwrite):
        super().__init__()
        self.title("Attendance App")
        self.geometry("1000x600")
        self.appwrite = appwrite

        # Main container where pages will load
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.current_view = None
        self.show_view(DepartmentSelectorView)

    def show_view(self, ViewClass, *args, **kwargs):
        # Remove current view if exists
        if self.current_view:
            self.current_view.destroy()

        # Load new page inside container
        self.current_view = ViewClass(self.container, self, *args, **kwargs)
        self.current_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    appwrite = AppwriteService()
    app = MainApp(appwrite)
    app.mainloop()


