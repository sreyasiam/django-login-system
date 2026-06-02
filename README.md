# Django Login System

A simple Django website featuring:

- Home page
- User registration
- User login
- Welcome page after login
- Static image support

## Technologies Used

- Python
- Django
- HTML
- CSS
- MySQL
- XAMPP (Apache & MySQL)

## Database

The application uses MySQL as the backend database, managed through XAMPP.

User information such as:

- Name
- Gender
- Qualification
- Phone Number
- Email
- Username
- Password

is stored in the MySQL database and used for user authentication.

## Requirements

- Python
- Django
- XAMPP
- MySQL
- mysqlclient (or PyMySQL)

## Database Setup

1. Start Apache and MySQL from XAMPP.
2. Create a database in phpMyAdmin.
3. Update `settings.py` with your MySQL credentials.
4. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
