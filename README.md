🎮 Real-Time Gaming Leaderboard & Analytics System

A backend system designed to simulate how real online gaming platforms (such as Teen Patti, Rummy, etc.) store gameplay data, process match results, generate rankings, and compute daily analytics.
This project demonstrates backend engineering, SQL-based analytics, REST API design, and data modeling commonly used in game data pipelines.

🚀 Features
Submit player match results (score, game type, duration)
Real-time leaderboard sorted by total score
Daily analytics: top player, total matches, average score
REST API with auto documentation (Swagger/OpenAPI)
SQL schema optimized for ranking & aggregation
Sample dataset generator for testing

🧪 API Endpoints
Method	Endpoint	Description
POST	/players	Create a new player
GET	/players/{player_id}	Fetch player details
POST	/games	Register a game
POST	/submit_score	Submit match result
GET	/leaderboard	Get top players
POST	/analytics/daily/{date}	Compute analytics for a day
GET	/analytics/daily/{date}	View analytics results

📌 Full interactive API documentation available at:

http://127.0.0.1:8000/docs

🛠️ Tech Stack
Layer	Technology
Language	Python
Framework	FastAPI
Database	MySQL
ORM	SQLAlchemy
Data Modeling	Pydantic
Docs	Swagger / OpenAPI
📁 Project Structure
📦 real-time-game-leaderboard
 ┣ 📂 src
 ┃ ┣ main.py
 ┃ ┣ database.py
 ┃ ┣ models.py
 ┃ ┣ schemas.py
 ┃ ┣ crud.py
 ┃ ┗ 📂 analytics
 ┃   ┗ daily_aggregator.py
 ┣ fake_data.py
 ┣ requirements.txt
 ┣ .env.example
 ┗ README.md

🔧 Setup & Installation
1️⃣ Clone Repository
git clone https://github.com/<your-username>/real-time-game-leaderboard.git
cd real-time-game-leaderboard

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create Database

Using phpMyAdmin:

Name: game_leaderboard
Collation: utf8mb4_general_ci

4️⃣ Configure Environment

Create .env file:

DB_USER=root
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_NAME=game_leaderboard

5️⃣ Generate Sample Data
python fake_data.py

6️⃣ Run Server
uvicorn main:app --reload

📊 Example API Output
[
  {
    "player_id": 1,
    "username": "player_3",
    "total_score": 1520,
    "matches_played": 20
  }
]

🧭 Future Enhancements
Redis caching for leaderboard
Kafka for real-time event streaming
Authentication & roles (admin / player)
Full frontend dashboard (React/Next.js)

👤 Author
Divyanshu Gautam
📧 Email: div911975@gmail.com
🔗 GitHub: https://github.com/dishu39

⭐ Support
If this project helps you, consider giving it a star ⭐ on GitHub — it helps visibility.
Want me to also generate:
LICENSE file

Project GIF demo badge

A pinned GitHub project image banner
