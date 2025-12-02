Real-Time Gaming Leaderboard & Analytics System 🎮
Overview
This project is a backend system that simulates how online gaming platforms (such as Teen Patti, Rummy, etc.) store gameplay data, process match results, generate rankings, and compute daily analytics. It demonstrates backend engineering, SQL-based analytics, REST API design, and data modeling commonly used in game data pipelines.

The system allows real-time leaderboard updates, daily analytics computations, and detailed player statistics. It is designed with scalability in mind, using technologies like FastAPI, SQLAlchemy, and MySQL, with a sample dataset generator to help with testing and development.

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
Full interactive API documentation available at:
Swagger UI Docs

🛠️ Tech Stack
Layer	Technology
Language	Python
Framework	FastAPI
Database	MySQL
ORM	SQLAlchemy
Data Modeling	Pydantic
Docs	Swagger/OpenAPI
📁 Project Structure
real-time-game-leaderboard/
 ┣ 📂 src/
 ┃ ┣ main.py              # FastAPI application entry point
 ┃ ┣ database.py          # Database connection & setup
 ┃ ┣ models.py            # SQLAlchemy database models
 ┃ ┣ schemas.py           # Pydantic models for data validation
 ┃ ┣ crud.py              # CRUD operations
 ┃ ┗ 📂 analytics/
 ┃   ┗ daily_aggregator.py # Computes daily analytics
 ┣ fake_data.py           # Sample data generator
 ┣ requirements.txt       # Python dependencies
 ┣ .env.example           # Example environment configuration file
 ┗ README.md              # Project documentation
🔧 Setup & Installation
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/real-time-game-leaderboard.git
cd real-time-game-leaderboard
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Create the Database
Using phpMyAdmin or your preferred MySQL management tool:

Database Name: game_leaderboard
Collation: utf8mb4_general_ci
4️⃣ Configure Environment
Create a .env file in the project root directory with the following values:

DB_USER=root
DB_PASSWORD=<your-db-password>
DB_HOST=127.0.0.1
DB_NAME=game_leaderboard
Note: Make sure to replace <your-db-password> with the actual password for your MySQL root user.

5️⃣ Generate Sample Data
You can use the fake_data.py script to generate sample data for testing purposes.

bash
Copy code
python fake_data.py
6️⃣ Run the Server
Start the FastAPI development server with uvicorn:

bash
Copy code
uvicorn main:app --reload
The server will be running at http://127.0.0.1:8000.

📊 Example API Output
When fetching the leaderboard:

json
Copy code
[
  {
    "player_id": 1,
    "username": "player_3",
    "total_score": 1520,
    "matches_played": 20
  },
  {
    "player_id": 2,
    "username": "player_7",
    "total_score": 1410,
    "matches_played": 18
  }
]
🧭 Future Enhancements
Here are some planned features for future releases:

Redis caching for leaderboard to improve performance
Kafka for real-time event streaming
Authentication & roles (admin/player) for secure access
Full frontend dashboard using React/Next.js
Automated testing for critical functionality
Match history and replay system for detailed player analytics
Advanced machine learning models for player ranking prediction
👤 Author
Name: Divyanshu Gautam
Email: div911975@gmail.com
GitHub: https://github.com/dishu39
⭐ Support
If this project helps you, consider giving it a star ⭐ on GitHub to help increase its visibility!

🔧 License
You may want to add a license file here. For now, here’s a simple placeholder:

MIT License
Feel free to customize this as per your preferences.

Additional Notes:
SQLAlchemy Migrations: If you plan to scale or make changes to the database schema, you can integrate Alembic for handling database migrations.

Logging & Monitoring: For production environments, consider setting up logging (with logging or tools like Sentry or Logstash) and monitoring (with Prometheus and Grafana).
