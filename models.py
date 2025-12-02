# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Player(Base):
    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    country = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    events = relationship("GameEvent", back_populates="player")


class Game(Base):
    __tablename__ = "games"

    game_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    game_name = Column(String(50), nullable=False)
    game_type = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    events = relationship("GameEvent", back_populates="game")


class GameEvent(Base):
    __tablename__ = "game_events"

    event_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey("players.player_id"), nullable=False)
    game_id = Column(Integer, ForeignKey("games.game_id"), nullable=False)
    score = Column(Integer, nullable=False)
    played_at = Column(DateTime, default=datetime.utcnow)
    duration_secs = Column(Integer, nullable=True)

    player = relationship("Player", back_populates="events")
    game = relationship("Game", back_populates="events")


class DailyMetric(Base):
    __tablename__ = "daily_metrics"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    metric_date = Column(Date, nullable=False, unique=True)
    total_matches = Column(Integer, nullable=False)
    avg_score = Column(Float, nullable=True)
    top_player_id = Column(Integer, ForeignKey("players.player_id"))
    created_at = Column(DateTime, default=datetime.utcnow)
