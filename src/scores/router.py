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
