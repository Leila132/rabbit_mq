from config.database import engine, Base
from models import Level
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSession(engine) as session:
        required_levels = ["INFO", "WARNING", "ERROR"]
        for name in required_levels:
            result = await session.execute(
                select(Level).where(Level.level_name == name)
            )
            if not result.scalars().first():
                session.add(Level(level_name=name))
        await session.commit()
