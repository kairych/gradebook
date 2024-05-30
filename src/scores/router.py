from fastapi import APIRouter

router = APIRouter(
    prefix="/score",
    tags=["Score"]
)


@router.get("/111")
async def get_score():
    return {"message": "Hello score"}
