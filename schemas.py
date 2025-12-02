# schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


class PlayerBase(BaseModel):
    username: str
    country: Optional[str] = None


class PlayerCreate(PlayerBase):
    pass


class PlayerRead(PlayerBase):
    player_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class GameBase(BaseModel):
    game_name: str
    game_type: Optional[str] = None


class GameCreate(GameBase):
    pass


class GameRead(GameBase):
    game_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class SubmitScoreRequest(BaseModel):
    player_id: int
    game_id: int
    score: int
    duration_secs: Optional[int] = None


class LeaderboardEntry(BaseModel):
    player_id: int
    username: str
    total_score: int
    matches_played: int


class DailyMetricRead(BaseModel):
    metric_date: date
    total_matches: int
    avg_score: float
    top_player_id: Optional[int] = None

    class Config:
        from_attributes = True
