from app.core.database import supabase
from datetime import datetime

class MonitorAttendance:

    @staticmethod
    def add_attendance(stud_id: int, time_status: int, date_time: datetime) -> None:
       ...

    @staticmethod
    def delete_attendance(stud_id: int) -> None:
        ...

    @staticmethod
    def update_attendance(stud_id: int,
                          new_time_status: int | None = None) -> None:
        ...

    @staticmethod
    def get_attendances():
        ...


if __name__ == '__main__':
    # MonitorAttendance.add_attendance(stud_id=2203173, time_status=1, date_time=datetime.now())
    # MonitorAttendance.add_attendance(stud_id=2203174, time_status=1, date_time=datetime.now())
    # MonitorAttendance.update_attendance(stud_id=2203173, new_time_status=0)
    # MonitorAttendance.delete_attendance(stud_id=2203173)

    # print(MonitorAttendance.get_attendances(stud_id=2203173))
    # for record in MonitorAttendance.get_attendances():
    #     print(record)
    attendances = MonitorAttendance.get_attendances()
    for attendance in attendances:
        print(attendance)

