# #TODO(): 
import pandas as pd

def create_excel_from_records(records: list[dict], file_path) -> None:
    df = pd.DataFrame(records)
    df.to_excel(file_path, index=False)


