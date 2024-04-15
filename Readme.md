# Galactic Travel API

## Overview
Galactic Travel is a Django-based API that enables users to create, manage, and query interplanetary travel routes. It supports creating routes between planets, finding the fastest path based on travel time and ship autonomy, and managing these routes through a comprehensive API. This project is containerized with Docker for easy setup and scalability.

## Prerequisites
- Docker
- Docker Compose (optional for managing multi-container Docker applications)

## Setup Instructions

### Cloning the Repository
First, clone the repository to your local machine:
```bash
git clone [repository-url]
cd [repository-directory]
```


### Cloning the Repository
To build and run the project using Docker, execute the following commands:
```bash
docker build -t galactic_routes .
docker run -p 8000:8000 galactic_routes
```
This will start the Django application accessible via localhost:8000.

## API Docs
### CRUD Operations for Routes

1. Create a Route: You can use Postman or CURL or something similar:

Constraints:

- origin, destination, and travel_time cannot be null or empty.
- travel_time must be a positive integer.

the full url is : http://localhost:8000/api/all_routes_crud/

```http
POST /api/all_routes_crud/
Content-Type: application/json

{
    "origin": "Tatooine",
    "destination": "Hoth",
    "travel_time": 6
}
```

2. Retrieve all Routes:

```http
GET /api/all_routes_crud/
```

3. Retrieve a Route by id:

```http
GET /api/all_routes_crud/{id}/
```

4. Update a Route:

```http
PUT /api/all_routes_crud/{id}/
Content-Type: application/json

{
    "origin": "Tatooine",
    "destination": "Hoth",
    "travel_time": 8
}
```

4. Delete a Route by id:

```http
DELETE /api/all_routes_crud/{id}/
```
## Finding the Fastest Route

To find the shortest path to a specified destination:

```http
POST /api/all_routes_crud/find_fastest_way/
Content-Type: application/json

{
    "arrival": "Endor"
}
```

## Initial Config

When starting the project for the first time, the application will use a JSON file for initial settings:

```json
{
    "autonomy": 6,
    "departure": "Tatooine",
    "routes_db": "db.sqlite3"
}
```
## Config Options

- autonomy: Represents the maximum travel time a ship can travel without refueling.
- departure: The starting planet for route calculations.
- routes_db: The database file used by the application. If the database is empty, you must create routes as described above.

### Safe Travels and may be the Force be with you Jedi.