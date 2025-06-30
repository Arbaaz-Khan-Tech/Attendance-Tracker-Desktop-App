# attendance_app/app/services/appwrite_service.py
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.services.account import Account
from attendance_app.config import config
from appwrite.query import Query  # ← Add this at the top


 # safer absolute path


from attendance_app.app.models.student_model import Student
from attendance_app.app.models.faculty_model import Faculty

from attendance_app.app.models.attendance_model import Attendance


from appwrite.input_file import InputFile
import uuid

class AppwriteService:
    def __init__(self):
        self.client = Client()
        self.client.set_endpoint(config.APPWRITE_ENDPOINT)
        self.client.set_project(config.APPWRITE_PROJECT_ID)
        self.client.set_key(config.APPWRITE_API_KEY)

        self.account = Account(self.client)
        self.databases = Databases(self.client)

        self.database_id = config.DATABASE_ID
        self.student_collection = config.STUDENT_COLLECTION
        self.faculty_collection = config.FACULTY_COLLECTION
        self.attendance_collection = config.ATTENDANCE_COLLECTION

    def create_student(self, student: Student):
        doc_id = str(uuid.uuid4())
        result = self.databases.create_document(
            database_id=self.database_id,
            collection_id=self.student_collection,
            document_id=doc_id,
            data=student.to_dict()
        )
        return result
    
    def mark_attendance(self, attendance: Attendance):
     try:
        doc_id = str(uuid.uuid4())
        result = self.databases.create_document(
            database_id=self.database_id,
            collection_id=self.attendance_collection,
            document_id=doc_id,
            data=attendance.to_dict()
        )
        return result
     except Exception as e:
        print("Error marking attendance:", e)
        return None

    
    def create_faculty(self, faculty: Faculty):
        doc_id = str(uuid.uuid4())
        result = self.databases.create_document(
            database_id=self.database_id,
            collection_id=self.faculty_collection,
            document_id=doc_id,
            data=faculty.to_dict()
        )
        return result
    
    def mark_attendance(self, attendance: Attendance):
        doc_id = str(uuid.uuid4())
        result = self.databases.create_document(
            database_id=self.database_id,
            collection_id=self.attendance_collection,
            document_id=doc_id,
            data=attendance.to_dict()
        )
        return result
    

    def get_student_by_id(self, student_id: str):
     try:
        result = self.databases.list_documents(
            database_id=self.database_id,
            collection_id=self.student_collection,
            queries=[Query.equal("student_id", student_id)]
        )
        if result["documents"]:
            return Student.from_dict(result["documents"][0])
        else:
            return None
     except Exception as e:
        print("Error fetching student:", e)
        return None




    def get_faculty_by_id(self, faculty_id: str):
        try:
         result = self.databases.list_documents(
            database_id=self.database_id,
            collection_id=self.faculty_collection,
            queries=[Query.equal("faculty_id", faculty_id)]
        )
         if result["documents"]:
            return Faculty.from_dict(result["documents"][0])
         else:
            return None
        except Exception as e:
         print("Error fetching faculty:", e)
         return None


        
    def get_attendance_for_student(self, student_id: str):
        try:
         result = self.databases.list_documents(
            database_id=self.database_id,
            collection_id=self.attendance_collection,
            queries=[Query.equal("student_id", student_id)]
        )
         return [Attendance.from_dict(doc) for doc in result["documents"]]
        except Exception as e:
            print("Error fetching attendance:", e)
            return []
        
    def get_all_students(self):
     try:
        result = self.databases.list_documents(
            database_id=self.database_id,
            collection_id=self.student_collection
        )
        return [Student.from_dict(doc) for doc in result["documents"]]
     except Exception as e:
        print("Error fetching all students:", e)
        return []
     
    def get_all_departments(self):
      try:
        result = self.databases.list_documents(
            database_id=self.database_id,
            collection_id=self.student_collection
        )
        departments = {doc["department"] for doc in result["documents"]}
        return list(departments)
      except Exception as e:
        print("Error fetching departments:", e)
        return []
      
    def get_faculty_by_department(self, department: str):
     try:
        result = self.databases.list_documents(
            database_id=self.database_id,
            collection_id=self.faculty_collection,
            queries=[Query.equal("faculty_department", department)]
        )
        return [Faculty.from_dict(doc) for doc in result["documents"]]
     except Exception as e:
        print("Error fetching faculty:", e)
        return []
     

    def get_students_by_department(self, department: str):
     try:
        result = self.databases.list_documents(
            database_id=self.database_id,
            collection_id=self.student_collection,
            queries=[Query.equal("department", department)]
        )
        return [Student.from_dict(doc) for doc in result["documents"]]
     except Exception as e:
        print("Error fetching students:", e)
        return []
     


    def get_attendance_in_range(self, from_date: str, to_date: str):
     try:
        queries = [
             Query.greater_than_equal("date", from_date),
            Query.less_than_equal("date", to_date)
        ]

        print("[DEBUG] Attendance Range Query →", queries)

        response = self.databases.list_documents(
            database_id=self.database_id,
            collection_id=self.attendance_collection,
            queries=queries
        )

        print("[DEBUG] Fetched Documents Count →", len(response.get("documents", [])))
        return response["documents"]

     except Exception as e:
        print("Error fetching attendance in range:", e)
        return []

  
  


  
 
    
    

        
    








   

    