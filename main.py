# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from database import Base, engine, get_db
import models, schemas, crud

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Game Leaderboard & Analytics API")


@app.get("/")
def root():
    return {"message": "Game Leaderboard API is running"}


# ---- Player Endpoints ----
@app.post("/players", response_model=schemas.PlayerRead)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    db_player = crud.create_player(db, player)
    return db_player


@app.get("/players/{player_id}", response_model=schemas.PlayerRead)
def get_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.get_player(db, player_id)
    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player


# ---- Game Endpoints ----
@app.post("/games", response_model=schemas.GameRead)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    db_game = crud.create_game(db, game)
    return db_game


@app.get("/games/{game_id}", response_model=schemas.GameRead)
def get_game(game_id: int, db: Session = Depends(get_db)):
    db_game = crud.get_game(db, game_id)
    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game


# ---- Score / Leaderboard ----
@app.post("/submit_score")
def submit_score(data: schemas.SubmitScoreRequest, db: Session = Depends(get_db)):
    # You can validate if player_id and game_id exist:
    if not crud.get_player(db, data.player_id):
        raise HTTPException(status_code=400, detail="Invalid player_id")
    if not crud.get_game(db, data.game_id):
        raise HTTPException(status_code=400, detail="Invalid game_id")

    event = crud.submit_score(db, data)
    return {"message": "Score submitted", "event_id": event.event_id}


@app.get("/leaderboard", response_model=list[schemas.LeaderboardEntry])
def get_leaderboard(limit: int = 10, db: Session = Depends(get_db)):
    rows = crud.get_leaderboard(db, limit=limit)
    result = [
        schemas.LeaderboardEntry(
            player_id=row.player_id,
            username=row.username,
            total_score=int(row.total_score),
            matches_played=row.matches_played,
        )
        for row in rows
    ]
    return result


# ---- Analytics (Daily Metrics) ----
@app.post("/analytics/daily/{metric_date}", response_model=schemas.DailyMetricRead)
def compute_daily_metrics(metric_date: date, db: Session = Depends(get_db)):
    metric = crud.upsert_daily_metric(db, metric_date)
    return metric


@app.get("/analytics/daily/{metric_date}", response_model=schemas.DailyMetricRead)
def get_daily_metrics(metric_date: date, db: Session = Depends(get_db)):
    metric = crud.get_daily_metric(db, metric_date)
    if not metric:
        raise HTTPException(status_code=404, detail="No metrics for this date")
    return metric
