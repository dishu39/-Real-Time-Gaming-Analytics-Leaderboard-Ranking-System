# crud.py
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
import models, schemas


# Player
def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(username=player.username, country=player.country)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.player_id == player_id).first()


# Game
def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(game_name=game.game_name, game_type=game.game_type)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.game_id == game_id).first()


# Game Events / Scores
def submit_score(db: Session, data: schemas.SubmitScoreRequest):
    # validation could be added here
    event = models.GameEvent(
        player_id=data.player_id,
        game_id=data.game_id,
        score=data.score,
        duration_secs=data.duration_secs,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def get_leaderboard(db: Session, limit: int = 10):
    """
    Returns leaderboard sorted by total_score desc
    """
    q = (
        db.query(
            models.Player.player_id.label("player_id"),
            models.Player.username.label("username"),
            func.sum(models.GameEvent.score).label("total_score"),
            func.count(models.GameEvent.event_id).label("matches_played"),
        )
        .join(models.GameEvent, models.Player.player_id == models.GameEvent.player_id)
        .group_by(models.Player.player_id, models.Player.username)
        .order_by(func.sum(models.GameEvent.score).desc())
        .limit(limit)
    )
    return q.all()


# Daily Metrics
def upsert_daily_metric(db: Session, metric_date: date):
    """
    Aggregates metrics for a given date and upserts into daily_metrics.
    """
    # Aggregate for that date
    q = (
        db.query(
            func.count(models.GameEvent.event_id).label("total_matches"),
            func.avg(models.GameEvent.score).label("avg_score"),
        )
        .filter(func.date(models.GameEvent.played_at) == metric_date)
    ).one()

    total_matches = q.total_matches or 0
    avg_score = float(q.avg_score) if q.avg_score is not None else 0.0

    # Top player for that date
    top_q = (
        db.query(
            models.GameEvent.player_id,
            func.sum(models.GameEvent.score).label("total_score"),
        )
        .filter(func.date(models.GameEvent.played_at) == metric_date)
        .group_by(models.GameEvent.player_id)
        .order_by(func.sum(models.GameEvent.score).desc())
        .limit(1)
        .all()
    )

    top_player_id = top_q[0].player_id if top_q else None

    metric = (
        db.query(models.DailyMetric)
        .filter(models.DailyMetric.metric_date == metric_date)
        .first()
    )

    if metric:
        metric.total_matches = total_matches
        metric.avg_score = avg_score
        metric.top_player_id = top_player_id
    else:
        metric = models.DailyMetric(
            metric_date=metric_date,
            total_matches=total_matches,
            avg_score=avg_score,
            top_player_id=top_player_id,
        )
        db.add(metric)

    db.commit()
    db.refresh(metric)
    return metric


def get_daily_metric(db: Session, metric_date: date):
    return (
        db.query(models.DailyMetric)
        .filter(models.DailyMetric.metric_date == metric_date)
        .first()
    )
