from app.core.database import supabase
from datetime import datetime
from postgrest import APIResponse

class MonitorAttendance:

    @staticmethod
    def add_attendance(stud_id: str, time_status: int) -> APIResponse:
        now = datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        response = (
            supabase.table("attendance")
            .insert({
                "student_id": stud_id, 
                "time_status": time_status,
                "date_time": formatted_datetime})
            .execute()
        )
        
        return response

    @staticmethod
    def delete_attendance(stud_id: str) -> APIResponse:
        response = (
            supabase.table("attendance")
            .delete().eq("student_id", stud_id)
            .execute()
        )

        return response


    @staticmethod
    def clear_attendance() -> APIResponse:
        response = (
            supabase.table("attendance")
            .delete().neq("student_id", 0)
            .execute()
        )

        return response
    # @staticmethod
    # def update_attendance(stud_id: int,
    #                       new_time_status: int | None = None) -> None:
    #     #TODO()
    #     !TBA if required
    #     ...

    @staticmethod
    def get_attendances() -> APIResponse:
        response = (
            supabase.table("attendance")
            .select("*").execute()
        )

        return response


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

