from fastapi import APIRouter, HTTPException
from app.core.monitorAttendance import MonitorAttendance
from datetime import datetime
from pydantic import BaseModel

attendance_router = APIRouter(prefix="/attendance")

class AttendanceRecord(BaseModel):
    student_id: int
    time_status: int | None

@attendance_router.post("/add")
def add_attendance(attendance_record: AttendanceRecord):
    ...

@attendance_router.put("/update")
def update_attendance(attendance_record: AttendanceRecord):
    ...
@attendance_router.delete("/delete/{student_id}")
def delete_attendance(student_id: int):
    ...

@attendance_router.get("/get")
def get_all_attendance():
    ...