from app.core.database import supabase
from datetime import datetime
from postgrest import APIResponse
import pytz
class MonitorAttendance:

    @staticmethod
    def check_duplicates(stud_id: str, time_status:int) -> bool:
        is_exist = (
            supabase.table("attendance")
            .select("student_id")
            .eq("student_id", stud_id)
            .eq("time_status", time_status)
            .execute()
        )

        if is_exist.data:
            return True
    
        return False
    
    @staticmethod
    def add_attendance(stud_id: str, time_status: int) -> APIResponse:
        local_tz = pytz.timezone("Asia/Manila")
        # Create a time zone-aware datetime object representing the current local time
        now_local = datetime.now(local_tz)
        formatted_datetime = now_local.strftime("%Y-%m-%d %H:%M:%S")
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

