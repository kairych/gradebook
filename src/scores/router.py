from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Score as ScoreModel
from .schemas import ScoreBase, ScoreRead
from ..database import get_async_session

router = APIRouter(
    prefix="/score",
    tags=["Score"]
)


@router.post("/", response_model=ScoreRead)
async def add_score(score: ScoreBase, session: AsyncSession = Depends(get_async_session)):
    """
    Add a new score.

    Parameters:
    - `score` (ScoreBase): The score data to be created.
    - `session` (AsyncSession): A database session.

    Returns:
    - `ScoreRead`: The created score object.

    Raises:
    - `HTTPException` 500: If there is an internal server error.
    """
    try:
        new_score = ScoreModel(score=score.score, student_id=score.student_id)
        session.add(new_score)
        await session.commit()
        await session.refresh(new_score)
        return new_score
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{score_id}", response_model=ScoreRead)
async def get_score(score_id: int, session: AsyncSession = Depends(get_async_session)):
    """
    Read a score by ID.

    Parameters:
    - `score_id` (int): The ID of the score to retrieve.
    - `session` (AsyncSession): A database session.

    Returns:
    - `ScoreRead`: A retrieved score data.

    Raises:
    - `HTTPException` 404: If the score with the given ID is not found.
    - `HTTPException` 500: If there is an internal server error.
    """
    try:
        stmt = select(ScoreModel).where(ScoreModel.id == score_id)
        result = await session.execute(stmt)
        score = result.scalar_one_or_none()

        if not score:
            raise NoResultFound

        return score
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Score not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{score_id}", response_model=ScoreRead)
async def update_score(score_id: int, score: ScoreBase, session: AsyncSession = Depends(get_async_session)):
    """
    Update a score by its ID.

    Parameters:
    - `score_id` (int): The ID of the score to be updated.
    - `score` (ScoreBase): New data for the score.
    - `session` (AsyncSession, optional): A database session.

    Returns:
    - `ScoreRead`: The updated score data.

    Raises:
    - `HTTPException` 404: If the score with the given ID is not found.
    - `HTTPException` 500: If there is an internal server error.
    """
    try:
        query = await session.execute(select(ScoreModel).where(ScoreModel.id == score_id))
        existing_score = query.scalars().first()

        if not score:
            raise HTTPException(status_code=404, detail="Score not found")

        for key, value in score.dict(exclude_unset=True).items():
            setattr(existing_score, key, value)

        await session.commit()
        await session.refresh(existing_score)

        return existing_score
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{score_id}")
async def delete_score(score_id: int, session: AsyncSession = Depends(get_async_session)):
    """
    Delete a score by its ID.

    Parameters:
    - `score_id` (int): The ID of the score to be deleted.
    - `session` (AsyncSession, optional): A database session .

    Returns:
    - `dict`: A message confirming the deletion.

    Raises:
    - `HTTPException` 404: If the score with the given ID is not found.
    - `HTTPException` 500: If there is an internal server error.
    """
    try:
        query = await session.execute(select(ScoreModel).where(ScoreModel.id == score_id))
        score = query.scalars().first()

        if not score:
            raise HTTPException(status_code=404, detail="Score not found")

        await session.delete(score)
        await session.commit()

        return {"detail": "Score deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
