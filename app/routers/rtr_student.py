from fastapi import APIRouter, HTTPException
from app.core.monitorStudent import MonitorStudent
from pydantic import BaseModel

student_router = APIRouter(prefix="/student")

class StudentRecord(BaseModel):
    student_id: int
    new_student_id: int | None = None
    fName: str
    lName: str
    program: str
    year: int


@student_router.post("/add")
def add_student(student_record: StudentRecord) -> dict:
    ...


@student_router.put("/update")
def update_student(student_record: StudentRecord):
    ...
    

@student_router.delete("/delete/{student_id}")
def delete_student(student_id: int):
    ...


@student_router.get("/get")
def get_all_students() -> list[dict]:
    try:
        records = MonitorStudent.get_students()
        if not records:
            raise HTTPException(status_code=404, detail="No students found")
    
        return records.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))