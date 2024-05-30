from fastapi import FastAPI
from .scores.router import router as scores_router
from .students.router import router as students_router


description = """
This is a Student Scores API that allows you to manage students and their scores.\n
You can perform CRUD operations on students and scores, including creating, reading, updating, and deleting records.

### Students
* **Get information about a student**;
* **Add new student**;
* **Update information about a student**;
* **Delete a student**.

### Scores
* **Get a score value**;
* **Add a score to a certain student**;
* **Update a score information**;
* **Delete a score**.
"""

app = FastAPI(
    title="Online grades book",
    description=description,
    version="1.0.0",
    contact={
        "name": "Kairat Tussupbekov: tussupbekov@gmail.com",
        "email": "tussupbekov@gmail.com",
    },
)

app.include_router(students_router)
app.include_router(scores_router)
