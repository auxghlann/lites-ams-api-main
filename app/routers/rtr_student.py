from fastapi import APIRouter, HTTPException
from app.core.monitorStudent import MonitorStudent
from pydantic import BaseModel
from postgrest.exceptions import APIError

student_router = APIRouter(prefix="/student")

class StudentRecord(BaseModel):
    student_id: int
    fName: str
    lName: str
    program: str
    year: int


@student_router.post("/add")
def add_student(student_record: StudentRecord) -> dict:
    
    try:
        student_id: int = student_record.student_id
        fName: str = student_record.fName
        lName: str = student_record.lName
        program: str = student_record.program
        year: int = student_record.year

        response = MonitorStudent.add_student(stud_id=student_id, fName=fName, lName=lName, program=program, year=year)

        if response.data:
            return {
                "status_code": 200,
                "message": f"Student {student_id} Added Successfully"
            }
        
    except APIError as e:
        if e.code == '23505':
            raise HTTPException(status_code=409, detail=str(e.details))
        else:
            raise HTTPException(status_code=400, detail=str(e.details))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@student_router.put("/update")
def update_student(student_record: StudentRecord) -> dict:
    try:
        student_id: int = student_record.student_id
        fName: str = student_record.fName
        lName: str = student_record.lName
        program: str = student_record.program
        year: int = student_record.year

        response = MonitorStudent.update_student(stud_id=student_id, new_fName=fName, 
                                                new_lName=lName, new_program=program, new_year=year)

        if response.data:
            return {
                "status_code": 200,
                "message": f"Student {student_id} Updated Successfully"
            }
        else:
            return {
                "status_code": 404,
                "message": f"Student {student_id} does not exist"
            }
        
    except APIError as e:
        raise HTTPException(status_code=400, detail=str(e.details))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@student_router.delete("/delete/{student_id}")
def delete_student(student_id: int) -> dict:
    try:
        response = MonitorStudent.delete_student(stud_id=student_id)

        if response.data:
            return {
                "status_code": 200,
                "message": f"Student {student_id} Deleted Successfully"
            }
        else:
            return {
                "status_code": 404,
                "message": f"Student {student_id} does not exist"
            }
    except APIError as e:
        raise HTTPException(status_code=400, detail=str(e.details))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@student_router.get("/get")
def get_all_students() -> list[dict]:
    try:
        records = MonitorStudent.get_students()
        if not records:
            raise HTTPException(status_code=404, detail="No students found")
    
        return records.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))