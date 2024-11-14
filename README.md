# LITES Attendance Monitoring System API

## Student Management API

This API provides functionalities to manage student record

**Base URL:** `url/student`


### **Data Model:**

* `StudentRecord`: This model defines the expected data format for student information.
    * `student_id`: (int) Unique identifier for the student.
    * `fName`: (str) First name of the student.
    * `lName`: (str) Last name of the student.
    * `program`: (str) Student's program of study.
    * `year`: (int) Student's year level.

### **Endpoints:**

**1. Add Student**

* **Method:** POST
* **URL:** `/add`
* **Request Body:** JSON data representing a `StudentRecord` object.

```http
POST /student/add
Content-Type: application/json

{
  "student_id": 123,
  "fName": "John",
  "lName": "Doe",
  "program": "BSCS",
  "year": 2
}
```

* **Success (Status Code: 200):**
    * Message: "Student {student_id} Added Successfully"

```json
{
  "status_code": 200,
  "message": "Student 123 Added Successfully"
}
```

* **Conflict (Status Code: 409):**
    * Occurs when a duplicate student ID is provided. Details from the underlying database error will be included.

```json
{
  "status_code": 409,
  "message": "Student 123 already exists"
}
```

* **Bad Request (Status Code: 400):**
    * Occurs for any other validation error with the provided data. Details from the underlying database error will be included.
* **Internal Server Error (Status Code: 500):**
    * Generic error for unexpected server-side issues.

**2. Update Student**

* **Method:** PUT
* **URL:** `/update`
* **Request Body:** JSON data representing a `StudentRecord` object.

```http
PUT /student/update
Content-Type: application/json

{
  "student_id": 123,
  "fName": "John",
  "lName": "Doe",
  "program": "Computer Science",
  "year": 3
}
```

* **Success (Status Code: 200):**
    * Message: "Student {student_id} Updated Successfully"

```json
{
  "status_code": 200,
  "message": "Student 123 Updated Successfully"
}
```

* **Not Found (Status Code: 404):**
    * Occurs when trying to update a non-existent student.

```json
{
  "status_code": 404,
  "message": "Student 123 does not exist"
}
```

* **Bad Request (Status Code: 400):**
    * Occurs for any validation error with the provided data. Details from the underlying database error will be included.
* **Internal Server Error (Status Code: 500):**
    * Generic error for unexpected server-side issues.

**3. Delete Student**

* **Method:** DELETE
* **URL:** `/delete/{student_id}`
* **Path Parameter:**
    * `{student_id}`: (int) Unique identifier of the student to be deleted.
  * **Success (Status Code: 200):**
      * Message: "Student {student_id} Deleted Successfully"

```json
{
  "status_code": 200,
  "message": "Student 123 Deleted Successfully"
}
```

  * **Not Found (Status Code: 404):**
      * Occurs when trying to delete a non-existent student.

```json
{
  "status_code": 404,
  "message": "Student 123 does not exist"
}
```

  * **Bad Request (Status Code: 400):**
      * May occur for unexpected data format issues with the path parameter. Details from the underlying database error will be included.
  * **Internal Server Error (Status Code: 500):**
      * Generic error for unexpected server-side issues.

**4. Get All Students**

* **Method:** GET
* **URL:** `/get`
* **Success (Status Code: 200):**
    * List of dictionaries representing student records. Each dictionary has the same structure as the `StudentRecord` model.

```json
[
  {
    "student_id": 123,
    "fName": "John",
    "lName": "Doe",
    "program": "BSCS",
    "year": 2
  },
  {
    "student_id": 456,
    "fName": "Juan",
    "lName": "Dela Cruz",
    "program": "BSIT",
    "year": 3
  },
  ...
]
```

* **Not Found (Status Code: 404):**
    * Occurs when no students are found in the database.
* **Internal Server Error (Status Code: 500):**
    * Generic error for unexpected server-side issues.

## Attendance Management API

This API provides functionalities to manage attendance record.

**Base URL:** `url/attendance`

### Data Models

* **AttendanceRecord:**
    * `student_id`: (int) Unique identifier of the student.
    * `time_status`: (int | None) Storing time-related information (e.g., 1: time-out, 0: time-out).

* **FilePath:**
    * `file_path`: (str) Path where the exported Excel file should be saved.
    * `file_name`: (str, default="attendance.xlsx") Name of the exported Excel file.



### Endpoints

**1. Add Attendance:**

* **Method:** POST
* **URL:** `/add`
* **Request Body:** Attendance record details in JSON format (refer to `AttendanceRecord` model).

```http
POST /attendance/add
Content-Type: application/json

{
  "student_id": 123,
  "time_status": 1
}
```
* **Success Response:**
    * Status Code: 200
    * Body: JSON object containing a success message with student ID.
  
```json
{
  "status_code": 200,
  "message": "Attendance of Student 123 Added Successfully"
}
```

* **Error Responses:**
    * Status Code: 400 (Bad Request) with details of the error encountered during attendance recording.
    * Status Code: 500 (Internal Server Error) for unexpected errors.

**2. Delete Attendance (by student ID):**

* **Method:** DELETE
* **URL:** `/delete/{student_id}`
* **Path Parameter:**
    * `student_id`: (int) Unique identifier of the student.
* **Success Response:**
    * Status Code: 200
    * Body: JSON object containing a success message with student ID if deleted or a message indicating the student's attendance record doesn't exist.
  
```json
{
  "status_code": 200,
  "message": "Attendance of Student 123 Deleted Successfully"
}
```

* **Error Responses:**
    * Status Code: 400 (Bad Request) with details of the error encountered during deletion.
    * Status Code: 404 (Not found) with details of the error encountered during record clearing.
    * Status Code: 500 (Internal Server Error) for unexpected errors.


**3. Clear All Attendance record:**

* **Method:** DELETE
* **URL:** `/clear`
* **Success Response:**
    * Status Code: 200
    * Body: JSON object containing a success message confirming all attendance record are cleared.

```json
{
  "status_code": 200,
  "message": "All attendance records cleared successfully"
}
```

* **Error Responses:**
    * Status Code: 400 (Bad Request) with details of the error encountered during record clearing.
    * Status Code: 500 (Internal Server Error) for unexpected errors.

**4. Get All Attendance record:**

* **Method:** GET
* **URL:** `/get`
* **Success Response:**
    * Status Code: 200
    * Body: JSON array containing retrieved attendance record.

```json
[
  {
    "student_id": 123,
    "time_status": 1
  },
  {
    "student_id": 456,
    "time_status": 1
  },
  ...
]
```

* **Error Response:**
    * Status Code: 404 (Not Found) if no attendance record are found.
    * Status Code: 500 (Internal Server Error) for unexpected errors.

**5. Export Attendance record to Excel:**

* **Method:** POST
* **URL:** `/export`
* **Request Body:** File path details in JSON format (refer to `FilePath` model).

```http
POST /attendance/export
Content-Type: application/json

{
  "file_path": "/path/to/save",
  "file_name": "attendance.xlsx"
}
```

* **Success Response:**
    * Status Code: 200
    * Body: Automatic download of the generated Excel file named "attendance.xlsx" containing attendance record.

```
returns the Excel file as a download
```

* **Error Responses:**
    * Status Code: 404 (Not Found) if there is no attendance record.
    * Status Code: 500 (Internal Server Error) for unexpected errors during file creation.