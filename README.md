# Django Ecommerce API

Welcome to the Django Ecommerce API project! This project is a result of following the comprehensive course by Mosh Hamedani, designed to provide a robust foundation for building a fully functional Ecommerce API using Django.

## Getting Started

To set up and run this project on your local machine, follow these steps:

1. **Clone the Repository:**
   ```
   git clone <repository_url>
   ```

2. **Activate Virtual Environment:**
   ```
   pipenv shell
   ```

3. **Install Dependencies:**
   ```
   pipenv install
   ```

4. **Database Migration:**
   - Package up your model changes into individual migration files:
     ```
     python manage.py makemigrations
     ```
   - Apply the migrations to create tables, modify columns, add indexes, and perform any other database-related operations needed to reflect the changes:
     ```
     python manage.py migrate
     ```

5. **Create Admin Identity:**
   Create an admin identity from which you will log in to manage the system:
   ```
   python manage.py createsuperuser
   ```

6. **Run the Server:**
   ```
   python manage.py runserver
   ```

Access the development server at [http://localhost:8000/](http://localhost:8000/) and start exploring the features of the Ecommerce API.

## Project Structure

The project follows best practices for Django application architecture, ensuring maintainability and scalability. Key components include:

- **Models:** Defines the structure of the database tables.
- **Views:** Handles the presentation logic and renders data to the user.
- **Serializers:** Converts complex data types, such as Django QuerySets, into Python data types that can be easily rendered into JSON.
- **URLs:** Maps URLs to views, allowing for a clear and organized URL structure.

## Contributing

Feel free to contribute to the project by submitting issues, feature requests, or pull requests. Follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

Thank you for using the Django Ecommerce API! Happy coding!
