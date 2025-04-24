from pydantic import BaseModel


class LevelBase(BaseModel):
    tg_id: str
    status_name: str


class Level_Schema(LevelBase):
    class Config:
        from_attributes = True


class NoteBase(BaseModel):
    tg_id: str
    status_name: str


class Note_Schema(NoteBase):
    class Config:
        from_attributes = True
