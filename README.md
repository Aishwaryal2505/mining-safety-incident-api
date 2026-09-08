\# Mining Safety Incident Tracker API

!\[Mining Safety API Tests](https://github.com/Aishwaryal2505/mining-safety-incident-api/actions/workflows/tests.yml/badge.svg)



A REST API built with FastAPI and PostgreSQL for logging and managing mining

safety incidents - continuing the WA mining/resources sector theme from my

other projects. Built to demonstrate full-stack API development: designing

endpoints, request/response validation, a relational database, and automated

testing against a live API.



\## Why this project

Most of my other projects focus on \*testing\* or \*consuming\* APIs. This one

closes the loop - I designed and built a real REST API myself, backed by a

proper relational database (PostgreSQL, not NoSQL/SQLite), matching the two

most commonly requested skills in Perth data/backend job listings: RESTful

API development and SQL databases.



\## Architecture

Client (Swagger UI / pytest / any HTTP client)

|

FastAPI (routing, request validation via Pydantic)

|

SQLAlchemy ORM

|

PostgreSQL (mining\_safety database)





\## Project structure

src/

database.py # DB connection setup, session management

models.py # SQLAlchemy table definition (Incident)

schemas.py # Pydantic request/response models

main.py # FastAPI app and 5 CRUD endpoints

create\_tables.py # One-time table creation script

tests/

test\_incidents.py # pytest suite testing the live API



\## Endpoints (CRUD)

| Method | Endpoint | Description |

|---|---|---|

| POST | /incidents | Log a new safety incident |

| GET | /incidents | List incidents (filterable by site, severity) |

| GET | /incidents/{id} | Get one specific incident |

| PUT | /incidents/{id} | Update an incident's status |

| DELETE | /incidents/{id} | Remove a record |



\## Key design decisions

\- \*\*Separate Pydantic schemas for input vs. output\*\* (`IncidentCreate` vs

&#x20; `IncidentResponse`) - clients can never set system-controlled fields like

&#x20; `id` or override `status` on creation

\- \*\*Dependency injection\*\* (`Depends(get\_db)`) for database sessions, so each

&#x20; request gets a fresh session that's automatically closed afterward

\- \*\*Explicit 404 handling\*\* for all lookups by ID, rather than letting missing

&#x20; records fail silently



\## Running locally

```bash

python -m venv venv

venv\\Scripts\\Activate.ps1

pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv pytest requests

\# create a PostgreSQL database and add its connection string to .env (see .env.example)

python -m src.create\_tables

uvicorn src.main:app --reload

```



Visit `http://127.0.0.1:8000/docs` for interactive Swagger documentation.



\## Running tests

With the server running in one terminal, run in another:

```bash

pytest tests/test\_incidents.py -v

```

