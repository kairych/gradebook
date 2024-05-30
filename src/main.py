from fastapi import FastAPI
from .scores.router import router as scores_router
from .students.router import router as students_router


app = FastAPI(
    title="Online grades book"
)

app.include_router(students_router)
app.include_router(scores_router)
