Here’s a detailed `README.md` for your **Attendance Tracker** desktop app project based on everything you’ve shared:

---

```markdown
# 🎓 Attendance Tracker Desktop App

This is a **Python-based student attendance management desktop application** built with **CustomTkinter** for the frontend and **Appwrite** as the backend-as-a-service platform. The app supports real-time CRUD operations for students, faculty, and attendance data. It is modular, easy to maintain, and scalable for multiple departments.

---

## 📁 Folder Structure

```

Attendance\_Track/
│
├── attendance\_app/
│   ├── app/
│   │   ├── models/
│   │   │   ├── student\_model.py
│   │   │   ├── faculty\_model.py
│   │   │   └── attendance\_model.py
│   │   ├── services/
│   │   │   └── appwrite\_service.py
│   │   └── views/
│   │       ├── department\_view\.py
│   │       ├── department\_detail\_view\.py
│   │       ├── attendance\_view\.py
│   │       ├── attendance\_summary\_view\.py
│   │       └── add\_student\_view\.py
│   ├── config/
│   │   └── config.py
│   └── main.py
│
├── README.md
└── requirements.txt

````

---

## 💡 Features

### ✅ Core Functionalities
- **Department Selection Page**  
  Displays available departments fetched from Appwrite DB. Users can:
  - View students & faculty
  - Add new students or faculty
  - Navigate to attendance or summary views

- **Student & Faculty Management**
  - Add students/faculty via form popups.
  - Retrieve lists department-wise.
  - Display them dynamically in the UI.

- **Attendance Management**
  - Select department → View all students with attendance toggle buttons.
  - Set the subject (auto-converted to uppercase).
  - Select the date.
  - Mark attendance with default set to "Absent" if not explicitly marked.

- **Attendance Summary View**
  - Select a date range (e.g., `2025-06-01` to `2025-06-30`).
  - Automatically fetch attendance records in that range.
  - Group by student → calculate present count, total sessions, and attendance percentage.
  - Sort by: Name, Roll Number, Subject, or Attendance %.
  
### 🔁 Seamless UI Navigation
- All views (attendance, department, summary, etc.) are managed **within the same window** using a `show_view()` controller method.
- No new windows unless modal popups (e.g., add student).

---

## 🧠 Tech Stack

| Layer        | Technology        |
|--------------|-------------------|
| Frontend UI  | `CustomTkinter`   |
| Backend      | `Appwrite` (Cloud)|
| Language     | `Python 3.10+`    |
| Others       | `UUID`, `Datetime`, `Appwrite SDK` |

---

## 🔧 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/Attendance_Track.git
cd Attendance_Track
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

> Make sure your Appwrite project is configured with:
>
> * Database ID
> * Collections: students, faculty, attendance
> * Proper attributes: student\_id, name, roll\_number, date, subject, status, etc.

### 4. Add `config.py`

Inside `attendance_app/config/config.py`:

```python
class config:
    APPWRITE_ENDPOINT = "https://cloud.appwrite.io/v1"
    APPWRITE_PROJECT_ID = "your-project-id"
    APPWRITE_API_KEY = "your-api-key"
    DATABASE_ID = "your-db-id"
    STUDENT_COLLECTION = "students"
    FACULTY_COLLECTION = "faculty"
    ATTENDANCE_COLLECTION = "attendance"
```

---

## 🚀 Run the App

```bash
python -m attendance_app.main
```

---

## 🧪 Sample Appwrite Data Schema

### 🎓 Students Collection

| Attribute    | Type   |
| ------------ | ------ |
| student\_id  | string |
| name         | string |
| roll\_number | string |
| department   | string |

### 👨‍🏫 Faculty Collection

| Attribute           | Type   |
| ------------------- | ------ |
| faculty\_id         | string |
| faculty\_name       | string |
| faculty\_department | string |

### 📅 Attendance Collection

| Attribute      | Type                        |
| -------------- | --------------------------- |
| attendance\_id | string (max 10 chars)       |
| student\_id    | string                      |
| faculty\_id    | string                      |
| subject        | string                      |
| date           | string (e.g., "2025-06-28") |
| status         | string ("present"/"absent") |

---

## 📌 Key Highlights

* Modular MVC-like structure
* Appwrite integration for secure DB operations
* All Tkinter windows unified into single-window views
* Built-in sorting, filtering, grouping
* Dynamic date & subject marking for attendance
* Clean and intuitive UI with CustomTkinter

---

## 🙌 Contributions

Feel free to fork the repo and contribute. Feature requests and bug reports are welcome!

---

## 📃 License

MIT License — use freely for personal or educational purposes.

```

---

Let me know if you want a lighter version for GitHub, or want badges, screenshots, or GIFs added too!
```
