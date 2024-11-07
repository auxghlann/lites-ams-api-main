import os
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


if __name__ == "__main__":
    # print(url)
    # print(key)
    # response = (
    # supabase.table("student")
    # .insert({
    #     "student_id": 12345, 
    #     "fName": "Added",
    #     "lName": "Added",
    #     "program": "BSCS",
    #     "year": 4})
    # .execute()
    # )
    # # print(response)
    response1 = supabase.table("student").select("*").execute()
    print(type(response1))
    ...
