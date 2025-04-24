from sqlalchemy.ext.asyncio import AsyncSession
from models import Note
from typing import List
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from schemas import Note_Schema


class NoteRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, note_data: Note_Schema) -> Note:
        try:
            self.db.add(note_data)
            await self.db.commit()
            await self.db.refresh(note_data)
            return note_data

        except SQLAlchemyError:
            await self.db.rollback()
            return None

    async def get_all(self) -> List:
        try:
            result = await self.db.execute(select(Note))
            queries = result.scalars().all()
            return queries
        except SQLAlchemyError:
            return None
