# Django Blog API

This project provides two main API services using Django and Django REST Framework (DRF):
1. **User API**: For managing user authentication and registration.
2. **Article API**: For managing articles where authenticated users can create, view, update, and delete articles.

## Features
- User authentication using Django's built-in user model.
- RESTful API for article management (Create, Retrieve, Update, Delete).
- Permission management to ensure only the article author can update or delete the article.
- Support for creating articles where the logged-in user is automatically set as the author.

## Tech Stack
- **Python**: Programming language.
- **Django**: Web framework for backend logic and structure.
- **Django REST Framework**: To create and manage APIs.
- **SQLite** (default): Database (you can change it to any other database like PostgreSQL or MySQL).

## Requirements

Make sure you have the following installed:
- Python (>=3.10)
- Django (>=4.2)
- Django REST Framework (>=3.12)

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/hopedeveloper08/blog.git
   cd blog
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:

   Apply migrations to initialize the database:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:

   To create an admin user to access the Django Admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   The project will now be running at: `http://127.0.0.1:8000/`.

## API Endpoints

### 1. User API
- **Registration**: Allow users to register.
- **Login**: Obtain a token for authentication.
- **Logout**: Invalidate the token.
- **List**: Retrieve all users.
- **Update**: Authenticated users can update information.
- **View**: View information of a single user.
  
   | Method | Endpoint                | Description       |
   |--------|-------------------------|-------------------|
   | POST   | `/api/auth/login/`      | User login        |
   | POST   | `/api/auth/logout/`     | User logout       |
   | POST   | `/api/auth/users/`      | User registration |
   | GET    | `/api/auth/users/`      | Users List        |
   | GET    | `/api/auth/users/<id>/` | User information  |
   | PUT    | `/api/auth/users/<id>/` | User Update       |
- 
### 2. Article API
- **List Articles**: Retrieve all articles.
- **Create Article**: Authenticated users can create an article.
- **View Article**: View details of a single article.
- **Update Article**: Only the author can update the article.
- **Delete Article**: Only the author can delete the article.

   | Method | Endpoint                   | Description                      |
   |--------|----------------------------|----------------------------------|
   | GET    | `/api/blog/articles/`      | Get all articles                 |
   | POST   | `/api/blog/articles/`      | Create a new article             |
   | GET    | `/api/blog/articles/<id>/` | Get a specific article           |
   | PUT    | `/api/blog/articles/<id>/` | Update an existing article       |
   | DELETE | `/api/blog/articles/<id>/` | Delete an article                |

## Permissions

- Only authenticated users can create articles.
- Any user can read articles.
- Only the author of an article can update or delete it.

## Running Tests

To run the tests for this project:

```bash
python manage.py test
```

## Deployment

For deploying to a production environment:
1. Set up a production database (e.g., PostgreSQL).
2. Update the `DATABASES` settings in `settings.py`.
3. Use a WSGI server (e.g., Gunicorn) and configure the server (e.g., Nginx) accordingly.

## Authors

- **Reza Shahraki** - *Initial work* - [hopedeveloper08](https://github.com/hopedeveloper08)
