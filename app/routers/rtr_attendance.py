from fastapi import APIRouter, HTTPException
from app.core.monitorAttendance import MonitorAttendance
from datetime import datetime
from pydantic import BaseModel
from postgrest.exceptions import APIError

attendance_router = APIRouter(prefix="/attendance")

class AttendanceRecord(BaseModel):
    student_id: int
    time_status: int | None

@attendance_router.post("/add")
def add_attendance(attendance_record: AttendanceRecord) -> dict:
    try:
        student_id: int = attendance_record.student_id
        time_status: int = attendance_record.time_status

        response = MonitorAttendance.add_attendance(
                                    stud_id=student_id, time_status=time_status)

        if response.data:
            return {
                "status_code": 200,
                "message": f"Attendance of Student {student_id} Added Successfully"
            }
        
    except APIError as e:
        raise HTTPException(status_code=400, detail=str(e.details))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @attendance_router.put("/update")
# def update_attendance(attendance_record: AttendanceRecord):
#     #TODO()
#     !TBA if required
#     ...
@attendance_router.delete("/delete/{student_id}")
def delete_attendance(student_id: int) -> dict:
    try:
        response = MonitorAttendance.delete_attendance(stud_id=student_id)

        if response.data:
            return {
                "status_code": 200,
                "message": f"Attendance of Student {student_id} Deleted Successfully"
            }
        else:
            return {
                "status_code": 404,
                "message": f"Attendance of Student {student_id} does not exist"
            }
    except APIError as e:
        raise HTTPException(status_code=400, detail=str(e.details))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@attendance_router.delete("/clear")
def clear_attendance():
    try:
        response = MonitorAttendance.clear_attendance()
        if response.data:
            return {
                "status_code": 200,
                "message": "All attendance records cleared successfully"
            }
    except APIError as e:
        raise HTTPException(status_code=400, detail=str(e.details))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@attendance_router.get("/get")
def get_all_attendance() -> list[dict]:
    try:
        records = MonitorAttendance.get_attendances()
        if not records:
            raise HTTPException(status_code=404, detail="No attendance found")
    
        return records.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))