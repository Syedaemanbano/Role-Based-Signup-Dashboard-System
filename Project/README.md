# Django Role-Based Signup & Dashboard System

A Django-based web application implementing role-based access control (RBAC) with separate dashboards for Admin and Customer users.

## Features

### Core Features

- **User Signup**: Registration with Username, Password, and Role selection (Admin/Customer)
- **User Login**: Django Authentication with role-based redirection
- **Customer Dashboard**: Displays logged-in user's Username and Email
- **Admin Dashboard**: Displays a table of all registered users (ID, Username, Role)

### Bonus Features (CRUD Operations)

- **Delete User**: Admin can delete users from the system
- **Update User**: Admin can update user details (Username, Email, Role)

## Technology Stack

- **Framework**: Django 5.2.8
- **Database**: SQLite (db.sqlite3)
- **Language**: Python 3.12+
- **Authentication**: Django Authentication System

## Project Structure

```
Project/
├── accounts/              # Main application
│   ├── models.py         # CustomUser model with role field
│   ├── views.py          # All view functions
│   ├── forms.py          # UserCreationForm and UpdateForm
│   ├── urls.py           # URL routing
│   └── templates/        # HTML templates
│       └── accounts/
│           ├── base.html
│           ├── login.html
│           ├── signup.html
│           ├── customer_dashboard.html
│           ├── admin_dashboard.html
│           └── update_user.html
├── Project/              # Django project settings
│   ├── settings.py      # Django configuration
│   └── urls.py          # Root URL configuration
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## Installation & Setup

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/Syedaemanbano/Project_task.git
   cd Project_task/Project
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**

   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional, for Django admin)**

   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:8000/`

## Usage

### Signup

1. Navigate to the signup page: `http://127.0.0.1:8000/signup/`
2. Fill in:
   - Username
   - Password
   - Email (optional)
   - Role (Admin or Customer)
3. Click "Register"

### Login

1. Navigate to: `http://127.0.0.1:8000/`
2. Enter your username and password
3. Click "Log In"
4. You will be redirected based on your role:
   - **Admin** → `/dashboard/admin/`
   - **Customer** → `/dashboard/customer/`

### Admin Dashboard

- View all registered users in a table
- Delete users (except yourself)
- Update user information (Username, Email, Role)

### Customer Dashboard

- View your own profile information
- Username and Email display

## Security Features

- **Role-Based Access Control**: Customers cannot access Admin dashboard
- **Authentication Required**: All dashboards require login
- **CSRF Protection**: All forms include CSRF tokens
- **Password Security**: Django's built-in password hashing

## Database

The project uses SQLite database (`db.sqlite3`). The database includes:

- CustomUser model with role field
- All user registrations and authentication data

## Testing

To test the application:

1. **Create an Admin user**:

   - Sign up with role "Admin"
   - Login and access admin dashboard

2. **Create a Customer user**:

   - Sign up with role "Customer"
   - Login and access customer dashboard

3. **Test Security**:
   - Try accessing `/dashboard/admin/` as a customer (should be denied)
   - Try accessing `/dashboard/customer/` as an admin (should be denied)

## Author

**SYEDA EMAN BANO GILANI**

- Email: syedaemanbanogilani@gmail.com
- GitHub: [Syedaemanbano](https://github.com/Syedaemanbano)
