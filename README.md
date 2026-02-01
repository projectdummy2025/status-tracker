# Status Tracker API

A FastAPI-based REST API for tracking statuses with SQLite database integration.

## Overview

The Status Tracker API is a lightweight web application built with FastAPI and SQLAlchemy. It provides endpoints to create and retrieve status records stored in a SQLite database. Each status record contains a title and status field along with a unique ID.

## Features

- Create new status records via POST endpoint
- Retrieve specific status records via GET endpoint
- SQLite database integration for data persistence
- Pydantic models for request/response validation
- Automatic API documentation with Swagger UI and ReDoc

## Tech Stack

- **Framework**: FastAPI
- **Database**: SQLite (with SQLAlchemy ORM)
- **Validation**: Pydantic
- **Web Server**: Uvicorn

## Dependencies

- fastapi==0.128.0
- uvicorn==0.40.0
- sqlalchemy==2.0.46
- pydantic==2.12.5
- sqlite3 (built-in with Python)

## Project Structure

```
/home/fedora/projects/status-tracker/
├── app/
│   ├── __init__.py
│   ├── main.py          # Application entry point
│   ├── database.py      # Database configuration
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   └── routes/
│       ├── __init__.py
│       └── status.py    # Status endpoints
├── requirements.txt     # Project dependencies
├── .gitignore          # Git ignore rules
└── venv/              # Virtual environment
```

## API Endpoints

### Create Status
- **Endpoint**: `POST /status/`
- **Request Body**:
  ```json
  {
    "title": "string",
    "status": "string"
  }
  ```
- **Response**: Created status object with ID
- **Example**: `curl -X POST "http://localhost:8000/status/" -H "Content-Type: application/json" -d '{"title": "Project Alpha", "status": "In Progress"}'`

### Get Status by ID
- **Endpoint**: `GET /status/{status_id}`
- **Parameters**: `status_id` (integer)
- **Response**: Status object with ID, title, and status
- **Example**: `curl -X GET "http://localhost:8000/status/1"`

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd status-tracker
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Access the API:
   - Application: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - Alternative API docs: http://localhost:8000/redoc

## Database

The application uses SQLite as the database, with the database file stored as `status.db` in the project root. SQLAlchemy is used as the ORM to interact with the database.

## Models

### Status Model
- `id` (Integer, Primary Key): Unique identifier for each status
- `title` (String): Title of the status
- `status` (String): Current status value

### Schemas

#### StatusCreate
- `title` (String): Title of the status (required)
- `status` (String): Current status value (required)

#### StatusResponse (inherits from StatusCreate)
- `id` (Integer): Unique identifier for the status (required)

## Error Handling

- 404 Not Found: Returned when requesting a status with an ID that doesn't exist
- Validation errors: Automatically handled by Pydantic with detailed error messages

## Development

To run the application in development mode with auto-reload:
```bash
uvicorn app.main:app --reload
```

## Testing

To test the API endpoints, you can use the interactive documentation at `/docs` or use command-line tools like curl:

```bash
# Create a new status
curl -X POST "http://localhost:8000/status/" \
  -H "Content-Type: application/json" \
  -d '{"title": "My Project", "status": "Active"}'

# Get a status by ID
curl -X GET "http://localhost:8000/status/1"
```

## License

This project is open-source and available under the MIT License.