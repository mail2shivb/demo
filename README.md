# Spring Boot Trade CRUD Demo

This project is a Spring Boot application with H2 in-memory database. It provides CRUD operations for a `Trade` entity
via REST API.

## Features

- Spring Boot 3
- H2 Database (in-memory)
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

1. Ensure you have Java 17+ and Maven installed.
2. Run:
   ```bash
   mvn spring-boot:run
   ```
3. Access H2 Console at [http://localhost:8080/h2-console](http://localhost:8080/h2-console)

## Notes

- The database is in-memory and resets on restart.
- Replace sample data and endpoints as needed for your use case.
