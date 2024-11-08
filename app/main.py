from fastapi import FastAPI
from app.routers import rtr_attendance, rtr_student

app = FastAPI()
app.include_router(rtr_attendance.attendance_router)
app.include_router(rtr_student.student_router)


@app.get('/')
def root():
    return {
        "hello": "world",
        "About": "This is an API of LITES' Attendance Monitoring System"
    }

