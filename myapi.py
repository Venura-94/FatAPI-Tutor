from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": "17",
        "year": "year 12"
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str
    
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age :Optional[int] = None
    year: Optional[str]  = None

#first api 

@app.get("/")   # show some information # this is the end point "home Page"
def index():
    return {"name": "First Data"} 

#Path Parameters

@app.get("/get-student/{student_id}") 
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0)):
    return students.get(student_id, {"error": "Student not found"})

#Query Paramaters combined with path parameter

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id :int, name:Optional[str] = None, test :int ): # with * default parameters work
    for students_id in students:
        if students[students_id]["name"] ==name:
            return students[students_id]
    return {"Data":"Not Found"}

#Request Body and The Post Method

@app.post("/create-students/{student_id}")
def create_student(student_id:int,student:Student):
    if student_id in students:
        return{"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]

#Put Method (new end point)

@app.put("/update-student/{student_id}")
def update_student(student_id:int, student:UpdateStudent):
    if student_id not in students:
        return{"Error : Student does not exist"}
    
    if student.name != None:
        students[student_id],name = student.name

    if student.age != None:
        students[student_id],age = student.age

    if student.year != None:
        students[student_id],year = student.year

    return students [student_id]

#Delete Method

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    

    del students[student_id]
    return{"Message":"Student deleted successfully"}
    