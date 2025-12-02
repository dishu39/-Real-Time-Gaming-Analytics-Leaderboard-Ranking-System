# fake_data.py
import random
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from database import SessionLocal, engine
import models, schemas, crud

# Make sure tables exist
models.Base.metadata.create_all(bind=engine)

db: Session = SessionLocal()

# Create players
usernames = ["player_1", "player_2", "player_3", "player_4", "player_5"]
players = []

for name in usernames:
    player = crud.create_player(
        db, schemas.PlayerCreate(username=name, country="India")
    )
    players.append(player)

# Create a game
game = crud.create_game(
    db,
    schemas.GameCreate(game_name="Teen Patti Clone", game_type="cards"),
)

# Create events
now = datetime.utcnow()
for _ in range(100):
    p = random.choice(players)
    score = random.randint(10, 200)
    duration = random.randint(30, 600)

    event = models.GameEvent(
        player_id=p.player_id,
        game_id=game.game_id,
        score=score,
        duration_secs=duration,
        played_at=now - timedelta(minutes=random.randint(0, 1440)),
    )
    db.add(event)

db.commit()
db.close()
print("Fake data generated.")
