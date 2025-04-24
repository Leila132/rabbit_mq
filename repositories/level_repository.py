from sqlalchemy.ext.asyncio import AsyncSession
from models import Level
from typing import List, Optional
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from schemas import Level_Schema


class LevelRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, level_data: Level_Schema) -> Level:
        try:
            self.db.add(level_data)
            await self.db.commit()
            await self.db.refresh(level_data)
            return level_data
        except SQLAlchemyError as e:
            await self.db.rollback()
            return None

    async def get_all(self) -> List[Level]:
        try:
            result = await self.db.execute(select(Level))
            queries = result.scalars().all()
            return queries
        except SQLAlchemyError:
            return None

    async def get_by_name(self, name: str) -> Optional[Level]:
        try:
            result = await self.db.execute(
                select(Level).where(Level.level_name == name)
            )
            status = result.scalars().first()
            return status
        except SQLAlchemyError:
            return None
