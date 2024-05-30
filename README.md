# Read Me

## Running the Project

1. Make sure you have PostgreSQL installed and running on your machine.
2. Create a new PostgreSQL database for the project.
3. Copy the .env.example file to a new file called .env and update the database connection details (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME) with your local PostgreSQL configuration.
4. Create virtual environment: `python3 -m venv venv`
5. Activate virtual environment: `source venv/bin/activate`
6. Install the required Python packages by running `pip install -r requirements.txt`
7. Implement migrations: `alembic upgrade head`
8. Run the application using `uvicorn src.main:app --reload`
9. The API will be accessible at http://localhost:8000 or http://127.0.0.1:8000.

## API Endpoints

### Students

#### Create a Student

**Endpoint:** `POST /student/`

**Request Body:**

```
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}
```

**Response:** Created student object

#### Get a Student

**Endpoint:** `GET /student/{student_id}`

**Response:** Student object with associated scores

#### Update a Student

**Endpoint:** `PATCH /student/{student_id}`

**Request Body:**

```
{
  "first_name": "Jane",
  "last_name": "Doe"
}
```

**Response:** Updated student object

#### Delete a Student

**Endpoint:** `DELETE /student/{student_id}`

**Response:** `{"detail": "Student deleted successfully"}`

### Scores

#### Create a Score

**Endpoint:** `POST /score/`

**Request Body:**

```
{
  "score": 85,
  "student_id": 1
}
```

**Response:** Created score object

#### Get a Score

**Endpoint:** `GET /score/{score_id}`

**Response:** Score object

#### Update a Score

**Endpoint:** `PATCH /score/{score_id}`

**Request Body:**

```
{
  "score": 90
}
```

**Response:** Updated score object

#### Delete a Score

**Endpoint:** `DELETE /score/{score_id}`

**Response:** `{"detail": "Score deleted successfully"}`

> Note: Make sure to replace {student_id} and {score_id} with the actual IDs in the endpoint URLs.
> Endpoints can be tested in Postman.