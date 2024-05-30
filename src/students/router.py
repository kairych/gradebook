from fastapi import APIRouter

router = APIRouter(
    prefix="/student",
    tags=["Student"]
)


@router.get("/")
async def get_student():
    return {"message": "Hello student"}
