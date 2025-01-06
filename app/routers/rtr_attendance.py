import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.core.monitorAttendance import MonitorAttendance
from datetime import datetime
from pydantic import BaseModel
from postgrest.exceptions import APIError
from app.utils.excel_util import create_excel_from_records

attendance_router = APIRouter(prefix="/attendance")

class AttendanceRecord(BaseModel):
    student_id: str
    time_status: int | None

class FilePath(BaseModel):
    file_path: str
    file_name: str = "attendance.xlsx"

@attendance_router.post("/add")
def add_attendance(attendance_record: AttendanceRecord) -> dict:
    try:
        student_id: str = attendance_record.student_id
        time_status: int = attendance_record.time_status

        # Check for duplicates
        if MonitorAttendance.check_duplicates(stud_id=student_id, time_status=time_status):
            raise HTTPException(status_code=409, detail="Duplicate entry found for student_id and time_status")
        
        else:
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
@attendance_router.delete("/delete")
def delete_attendance(student_id: str, time_status: int) -> dict:
    try:
        response = MonitorAttendance.delete_attendance(stud_id=student_id, time_status=time_status)

        if response.data:
            return {
                "status_code": 200,
                "message": f"Attendance of Student {student_id} with time status {time_status} Deleted Successfully"
            }
        else:
            return {
                "status_code": 404,
                "message": f"Attendance of Student {student_id} with time status {time_status} does not exist"
            }
    except APIError as e:
        raise HTTPException(status_code=400, detail=str(e.details))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@attendance_router.delete("/clear")
def clear_attendance() -> dict:
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


@attendance_router.post("/export")
def export_attendances_to_excel(file_path: FilePath) -> FileResponse:
    try:
        records = MonitorAttendance.get_attendances()
        if not records:
            raise HTTPException(status_code=404, detail="No students found")
        
        excel_file_path = os.path.join(file_path.file_path, file_path.file_name)
        create_excel_from_records(records.data, excel_file_path)
        
        if not os.path.exists(excel_file_path):
            raise HTTPException(status_code=500, detail="Failed to create Excel file")
        
        return FileResponse(path=excel_file_path, filename=file_path.file_name, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))