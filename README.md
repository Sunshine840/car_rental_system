# car_rental_system

Master of Software Engineering Assignment_1 — Car Rental System

## Project_description

This application is CLI-based Car Rental System for streamlining car bookings. Guest Visitors can browse the car menu but only authenticated(Registered users) can book available cars. In this app we have tried to integrate some personalisation and recommending cars to the user by asking them about 5 questions.
Admins can manage cars, bookings, and user data. Payments can be made partially or fully

## Features(User side)

1. View available cars (Guest users/Registered users)
2. CarMatch (optional): Special feature that will allow users to view cars matching their personality in other words app will make recommendations by asking 5 questions.
3. Display all main features of selected cars once a car image selected
4. Setup account using email, password, address, phone numbers
5. User dashboard (Authenticated users only), will allow users to view their email, phone and booked or cancelled bookings, booking history and payments made.
6. Select and book available car (Authenticated users only)
7. Cancel or update bookings (Authenticated users only)
8. Make special request (Authenticated users only)
9. Update user accounts including forgot password
10. Make payments

## Features(Admins)

1. View bookings and confirm
2. View users and their relevant data including (Email, phone number, address)
3. View any special request
4. View Payments
5. Upload new cars images(Multiple)
6. CRUD operations on car features/details
7. CRUD operations on users account

## Technologies Used

- Python 3.x
- SQLite

## Installation / Setup

- git clone https://github.com/Sunshine840/car_rental_system.git
- cd car-rental-system
- pip install -r requirements.txt
- python main.py

## Usage

- Run python main.py
- Follow the menu prompts to
- Browse cars
- Rent a car
- Return a car
- View rental history
- Admin users can log in with predefined credentials to manage cars and bookings

## Database Design

- The ERD diagram can be found here docs/ERD.pdf

## UML Diagrams

- The UML Class diagram can be found here docs/UML_Class_Diagram.pdf
- The UML Use Case diagram can be found here docs/UML_UseCase_Diagram.pdf
