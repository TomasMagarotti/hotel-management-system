# Hotel Management System

A Python-based hotel management system developed as a learning project to practice object-oriented programming, modular architecture, date-based reservation management, and asynchronous operations.

## Features

- Room management
- Customer management
- Reservation management
- Date-based room availability checking
- Reservation cancellation
- Asynchronous payment processing simulation
- Modular project structure

## Technologies

- Python 3
- Object-Oriented Programming (OOP)
- asyncio
- datetime
- Git
- GitHub

## Project Structure

```text
hotel-management-system/
├── hotel_management/
│   ├── __init__.py
│   ├── customers.py
│   ├── payments.py
│   ├── reservations.py
│   └── rooms.py
├── .gitignore
├── main.py
└── README.md
```


### File Descriptions

- `main.py` — Entry point of the application. Coordinates the different management systems and the reservation workflow.
- `customers.py` — Handles customer creation and customer management.
- `rooms.py` — Handles room creation and room management.
- `reservations.py` — Manages reservations, date-based room availability, and reservation cancellation.
- `payments.py` — Simulates asynchronous payment processing.
- `__init__.py` — Initializes the `hotel_management` package.
- `.gitignore` — Specifies files and directories that should not be tracked by Git.

## How It Works

The reservation workflow follows these steps:

1. Check room availability for the requested dates.
2. Process the payment asynchronously.
3. Create the reservation if the payment is successful.
4. Store the reservation in the reservation system.
5. Prevent overlapping reservations for the same room.

## Example Output

```text
Habitación 101 agregada
Habitación 103 agregada
Cliente Alice agregado
Cliente Robert agregado
Cliente Carlos agregado

Procesando pago de Alice por $100
Pago de $100 completado para Alice
Reserva creada para Alice en la habitacion 101 del 10/09/2026 al 15/09/2026

Procesando pago de Carlos por $100
Pago de $100 completado para Carlos
Reserva creada para Carlos en la habitacion 101 del 20/09/2026 al 25/09/2026

Procesando pago de Robert por $200
Pago de $200 completado para Robert
Reserva creada para Robert en la habitacion 103 del 20/09/2026 al 25/09/2026
```

## How to Run

### 1. Clone the repository

```bash
git clone git@github.com:TomasMagarotti/hotel-management-system.git
```

### 2. Navigate to the project directory

```bash
cd hotel-management-system
```

### 3. Run the application

```bash
python3 main.py
```

## Learning Goals

This project was created to practice and strengthen the following Python concepts:

- Object-Oriented Programming (OOP)
- Classes and objects
- Modular code organization
- Working with dictionaries and lists
- Date and time management with `datetime`
- Asynchronous programming with `asyncio`
- Using `async` and `await`
- Basic Git and GitHub workflow