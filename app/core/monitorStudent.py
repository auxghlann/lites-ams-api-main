from app.core.database import supabase



class MonitorStudent:

    @staticmethod
    def add_student(stud_id: int, fName: str, lName: str, program: str, year: int) -> None:
        response = (
            supabase.table("student")
            .insert({
                "student_id": stud_id, 
                "fName": fName,
                "lName": lName,
                "program": program,
                "year": year})
            .execute()
        )

        return response

    @staticmethod 
    def update_student(stud_id: int, new_fName: str, 
                       new_lName: str, new_program: str, new_year: int):
        response = (
            supabase.table("student")
            .update({
                "fName": new_fName,
                "lName": new_lName,
                "program": new_program,
                "year": new_year})
            .eq("student_id", stud_id)
            .execute()
        )

        return response

    @staticmethod
    def delete_student(stud_id: int) -> None:
        response = supabase.table('student').delete().eq('student_id', stud_id).execute()

        return response

    
    @staticmethod
    def get_students():
        response = supabase.table("student").select("*").execute()
        
        return response

if __name__ == '__main__':
    # MonitorStudent.add_student(stud_id=2203173, fName="Allan Khester", lName="Mesa", program="BSCS", year=3)
    # MonitorStudent.add_student(stud_id=2203174, fName="Juan", lName="Dela Cruz", program="BSCS", year=3)
    students = MonitorStudent.get_students()

    for student in students:
        print(student)