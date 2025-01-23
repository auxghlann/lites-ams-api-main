from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import rtr_attendance, rtr_student

app = FastAPI()
app.include_router(rtr_attendance.attendance_router)
app.include_router(rtr_student.student_router)


# Add CORS middleware for localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1", "http://localhost:5173",
                    "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {
        "hello": "world",
        "About": "This is an API of LITES' Attendance Monitoring System"
    }

