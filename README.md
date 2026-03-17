Arrowood Landscaping Full-Stack Web Application
Overview

This is a full-stack web application for Arrowood Landscaping, providing an interactive platform to manage business operations including customer and service management.

Key features include:

Customer and service tracking

Dynamic reservation and booking system

Visual showcase of completed work via a gallery

Database-driven content using MySQL

Responsive, mobile-friendly interface

The app is built using Flask (Python), HTML/CSS/Jinja templates, and a relational database.

Features
Customer Management

Add, view, update, and delete customer records

Fields: Customer ID, First & Last Name, Phone, Email, Address

Automatically handles new vs. existing customers

Service Management

Add and view landscaping services requested by customers

Track service dates, service types, and assigned staff

Supports full CRUD operations

Reservation / Booking System

Customers can submit service requests via a contact form

Admin interface shows upcoming service bookings dynamically

Gallery / Our Work Page

Before & After photos of yard projects

1×4 grid layout with responsive images

Images pulled from the static folder using Flask’s url_for

Full CRUD Functionality

Users can create, read, update, and delete both customers and services

Data dynamically updated in the database

Technologies Used

Python 3.x

Flask (with Jinja templating)

HTML / CSS / JavaScript

MySQL (Arrowood database)

Bootstrap (optional for responsive styling)

Installation & Setup

Clone the repository

git clone https://github.com/graftonatwit/Arrowood-Landscaping-HTML-Page.git
cd Arrowood-Landscaping-HTML-Page

Install dependencies

pip install flask mysql-connector-python

Set up the database

Create the database using the provided SQL schema (arrowooddb).

Tables: customer, service, staff.

Update database credentials in app.py:

host="localhost"
user="root"
password="<your-password>"
database="arrowooddb"

Run the application

python app.py

Open in browser

http://127.0.0.1:5000
Usage

Navigate via the top menu: Home, Contact Us, Our Work, About Us

Submit service requests through the contact form → stored in database

View customer and service records dynamically

Explore the gallery showcasing Before & After yard transformations

Future Improvements

Staff authentication and login system

Enhanced UI/UX design

Reporting and analytics dashboard

Email notifications for scheduled services

Admin dashboard for easier management of customers and services

Author

Trevor Grafton
