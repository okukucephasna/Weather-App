# 🌦 Weather App

A full-stack weather application built with **Flask**, **React**, and **PostgreSQL**, featuring user authentication, weather data from OpenWeather API, and Dockerized deployment.

---

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Getting Started](#getting-started)
* [Environment Variables](#environment-variables)
* [Docker Setup](#docker-setup)
* [Usage](#usage)
* [API Endpoints](#api-endpoints)
* [Project Structure](#project-structure)
* [License](#license)

---

## Features

* User **Sign Up** and **Sign In**
* Fetch **current weather** for any city using **OpenWeather API**
* Full-stack Dockerized application
* PostgreSQL database for user management
* React frontend with Tailwind CSS styling

---

## Tech Stack

* **Backend:** Flask, Python, psycopg2
* **Frontend:** React, Tailwind CSS, Axios
* **Database:** PostgreSQL
* **Deployment:** Docker, Docker Compose

---

## Getting Started

### Prerequisites

* Docker & Docker Compose installed
* OpenWeather API key

### Clone the repository

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

---

## Environment Variables

Create a `.env` file in the `backend/` folder:

```env
DATABASE_URL=postgresql://postgres:postgres@weather_postgres:5432/weatherdb
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
```

* `DATABASE_URL`: Postgres connection string
* `OPENWEATHER_API_KEY`: Your OpenWeather API key

---

## Docker Setup

1. Build and start the containers:

```bash
docker-compose up --build
```

2. Stop containers:

```bash
docker-compose down
```

> If you change Postgres credentials, remove volumes with `docker-compose down -v` to avoid authentication issues.

---

## Usage

* Frontend runs on [http://localhost:3000](http://localhost:3000)
* Backend runs on [http://localhost:5000](http://localhost:5000)

### React Routes

* `/` - Sign Up
* `/signin` - Sign In
* `/dashboard` - Weather dashboard (after login)

---

## API Endpoints

| Method | Endpoint   | Description                 |
| ------ | ---------- | --------------------------- |
| POST   | `/signup`  | Register a new user         |
| POST   | `/signin`  | Log in an existing user     |
| GET    | `/weather` | Get weather data for a city |
| GET    | `/test-db` | Test database connection    |

**Request Example for Sign Up:**

```json
POST /signup
{
  "username": "john@example.com",
  "password": "securepassword"
}
```

---

## Project Structure

```
weather-app/
├── backend/
│   ├── app.py
│   ├── signup.py
│   ├── signin.py
│   ├── db.py
│   ├── init_db.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── api.js
│   │   ├── pages/
│   │   │   ├── Signin.jsx
│   │   │   └── Signup.jsx
│   │   └── index.js
│   ├── package.json
│   └── tailwind.config.js
├── docker-compose.yml
└── README.md
```

---

## License

This project is licensed under the **MIT License**.

Do you want me to enhance it that way?
