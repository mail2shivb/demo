# Spring Boot Trade CRUD Demo

This project is a Spring Boot application with PostgreSQL database. It provides CRUD operations for a `Trade` entity
via REST API.

## Features

- Spring Boot 3
- PostgreSQL Database
- JPA Entity: Trade
- REST Controller for CRUD
- Service layer for business logic

## API Endpoints

- `GET /api/trades` - List all trades
- `GET /api/trades/{id}` - Get trade by ID
- `POST /api/trades` - Create a new trade
- `PUT /api/trades/{id}` - Update a trade
- `DELETE /api/trades/{id}` - Delete a trade

## How to Run

1. Ensure you have Java 17+, Maven, and a running PostgreSQL instance.
2. Create a database named `trades` in PostgreSQL:
   ```bash
   createdb -U postgres trades
   ```
   (You can change the username/password in `src/main/resources/application.yml` as needed.)
3. Run:
   ```bash
   mvn spring-boot:run
   ```
4. docker run -d -p 5432:5432 -e POSTGRES_USER=postgres-e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=trades postgres 
4. Access the API at `http://localhost:8080/api/trades`.
4. The application will connect to PostgreSQL at `jdbc:postgresql://localhost:5432/trades` by default.

## Notes

- The database is persistent in PostgreSQL.
- Update the datasource settings in `src/main/resources/application.yml` if your PostgreSQL instance uses different credentials or host/port.
