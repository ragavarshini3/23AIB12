# Vehicle Scheduler Backend

## Overview

This project is a backend microservice developed using FastAPI for the Campus Hiring Evaluation. It connects to the protected evaluation APIs and retrieves depot information using Bearer Token authentication.

## Technologies Used

- Python
- FastAPI
- Requests
- Uvicorn

## Features

- FastAPI backend setup
- Authentication using Bearer Token
- Fetch depot details from the evaluation API
- REST API implementation

## Project Structure

```
vehicle_scheduling_be/
├── main.py
├── config.py
└── README.md
```

## Installation

Install the required packages:

```bash
pip install fastapi uvicorn requests
```

## Run the Project

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home Endpoint |
| GET | /depots | Fetch Depot Details |

## Status

Initial backend setup completed.
