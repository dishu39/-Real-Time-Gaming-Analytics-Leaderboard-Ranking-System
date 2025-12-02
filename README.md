# 🎮 Real-Time Gaming Leaderboard & Analytics System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-brightgreen.svg)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange.svg)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red.svg)
![Swagger](https://img.shields.io/badge/API-OpenAPI%20%2F%20Swagger-lightblue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

A backend system designed to simulate how real online gaming platforms (such as Teen Patti, Rummy, etc.) store gameplay data, process match results, generate rankings, and compute daily analytics.

This project demonstrates backend engineering, SQL-based analytics, REST API design, and data modeling commonly used in game data pipelines.

---

## 🚀 Features

- Submit player match results (score, game type, duration)
- Real-time leaderboard sorted by total score
- Daily analytics: top player, total matches, average score
- REST API with auto documentation (Swagger/OpenAPI)
- SQL schema optimized for ranking & aggregation
- Sample dataset generator for testing

---

## 🧪 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/players` | Create a new player |
| GET | `/players/{player_id}` | Fetch player details |
| POST | `/games` | Register a game |
| POST | `/submit_score` | Submit match result |
| GET | `/leaderboard` | Get top players |
| POST | `/analytics/daily/{date}` | Compute analytics for a day |
| GET | `/analytics/daily/{date}` | View analytics results |

📌 API Docs:
```
http://127.0.0.1:8000/docs
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python |
| Framework | FastAPI |
| Database | MySQL |
| ORM | SQLAlchemy |
| Data Modeling | Pydantic |
| Docs | Swagger / OpenAPI |

---

## 👤 Author

**Divyanshu Gautam**

📧 Email: `div911975@gmail.com`  
🔗 GitHub: `https://github.com/dishu39`
