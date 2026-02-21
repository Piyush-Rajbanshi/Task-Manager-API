# Task Manager API

A JWT-authenticated REST API built using Flask and MySQL.

## Features

User Registration

Secure Login Authentication

JWT-based Authorization

Protected CRUD Endpoints

MySQL Relational Database Integration

API Tested using Postman

## Tech Stack

Python 3

Flask

Flask-JWT-Extended

MySQL

Postman

## API Endpoints
Method	Endpoint	Description
POST	/register	Register new user
POST	/login	Authenticate user
POST	/tasks	Create task (Protected)
GET	/tasks	Get user tasks

## Setup Instructions

Clone repository

Create virtual environment
python -m venv venv

Activate environment
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Configure database credentials

Run application
python app.py
