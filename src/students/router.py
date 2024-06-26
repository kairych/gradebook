from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .models import Student as StudentModel
from .schemas import StudentRead, StudentUpdate, StudentCreate
from ..database import get_async_session

router = APIRouter(
    prefix="/student",
    tags=["Student"]
)


@router.post("/", response_model=StudentRead)
async def add_student(student: StudentCreate, session: AsyncSession = Depends(get_async_session)):
    """
    Add a new student.

    Parameters:
    - `student` (StudentCreate): The student data to be created.
    - `session` (AsyncSession): A database session.

    Returns:
    - `StudentRead`: The created student object.

    Raises:
    - `HTTPException` 500: If there is an internal server error.
    """
    try:
        new_student = StudentModel(**student.dict())
        session.add(new_student)

        await session.commit()
        await session.refresh(new_student)
        return new_student
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Email already exists. Please use a different email.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{student_id}", response_model=StudentRead)
async def get_student(student_id: int, session: AsyncSession = Depends(get_async_session)):
    """
    Read a student by ID.

    Parameters:
    - `student_id` (int): The ID of the student to retrieve.
    - `session` (AsyncSession): A database session.

    Returns:
    - `StudentRead`: A retrieved student data.

    Raises:
    - `HTTPException` 404: If the student with the given ID is not found.
    - `HTTPException` 500: If there is an internal server error.
    """
    try:
        stmt = select(StudentModel).options(selectinload(StudentModel.scores)).where(StudentModel.id == student_id)
        result = await session.execute(stmt)
        student = result.scalar_one_or_none()

        if not student:
            raise NoResultFound

        return student
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Student not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{student_id}", response_model=StudentRead)
async def update_student(student_id: int, student: StudentUpdate, session: AsyncSession = Depends(get_async_session)):
    """
    Update a student by its ID.

    Parameters:
    - `student_id` (int): The ID of the student to be updated.
    - `student` (StudentUpdate): New data for the student.
    - `session` (AsyncSession, optional): A database session.

    Returns:
    - `StudentRead`: The updated student data.

    Raises:
    - `HTTPException` 404: If the student with the given ID is not found.
    - `HTTPException` 500: If there is an internal server error.
    """
    try:
        stmt = select(StudentModel).options(selectinload(StudentModel.scores)).where(StudentModel.id == student_id)
        result = await session.execute(stmt)
        existing_student = result.scalar_one_or_none()

        if not existing_student:
            raise HTTPException(status_code=404, detail="Student not found")

        for key, value in student.dict(exclude_unset=True).items():
            setattr(existing_student, key, value)

        session.add(existing_student)
        await session.commit()
        await session.refresh(existing_student)

        return existing_student
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{student_id}")
async def delete_student(student_id: int, session: AsyncSession = Depends(get_async_session)):
    """
    Delete a student by its ID.

    Parameters:
    - `student_id` (int): The ID of the student to be deleted.
    - `session` (AsyncSession, optional): A database session .

    Returns:
    - `dict`: A message confirming the deletion.

    Raises:
    - `HTTPException` 404: If the student with the given ID is not found.
    - `HTTPException` 500: If there is an internal server error.
    """
    try:
        stmt = select(StudentModel).where(StudentModel.id == student_id)
        result = await session.execute(stmt)
        student = result.scalar_one_or_none()

        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        await session.delete(student)
        await session.commit()

        return {"detail": "Student deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
