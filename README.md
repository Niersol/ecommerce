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

# Django Ecommerce API Project Structure

## Introduction

Welcome to the Django Ecommerce API project! This project serves as a fully functional Ecommerce API developed by following the comprehensive course created by Mosh Hamedani. Below is an overview of the project structure and key components.

## Project Overview

### 1. **Models**
   - Location: `store/models.py`
   - Description: Defines the database models used in the application, including Product, Collection, Customer, Order, OrderItem, Review, and ProductImage.
   - Notable Features:
     - Utilizes Django's built-in `SimpleListFilter` for inventory filtering.
     - Implements inline administration for Product Images.

### 2. **Admin Interface**
   - Location: `store/admin.py`
   - Description: Configures the Django admin interface for managing products, collections, customers, and orders.
   - Notable Features:
     - Custom admin actions such as clearing inventory.
     - Inline editing and display of Product Images.
     - Integration of custom CSS for enhanced styling.

### 3. **Views**
   - Location: `store/views.py`
   - Description: Contains viewsets for handling API requests related to products, collections, customers, orders, reviews, cart, and cart items.
   - Notable Features:
     - Utilizes Django REST Framework for creating powerful API views.
     - Implements custom permissions for viewing customer history.

### 4. **Serializers**
   - Location: `store/serializers.py`
   - Description: Defines serializers for converting complex data types, such as Django QuerySets, into JSON format.
   - Notable Features:
     - Utilizes serializers for products, collections, reviews, cart, cart items, customers, and orders.
     - Handles image serialization for products.

### 5. **Filters**
   - Location: `store/filters.py`
   - Description: Implements filters using Django Filter for product-related queries.

### 6. **Signals**
   - Location: `store/signals.py`
   - Description: Defines signals, such as `order_created`, for handling events like order creation.

### 7. **Permissions**
   - Location: `store/permissions.py`
   - Description: Contains custom permission classes, including `FullDjangoModelPermissions`, `IsAdminOrReadOnly`, and `ViewCustomerHistoryPermission`.

### 8. **Pagination**
   - Location: `store/pagination.py`
   - Description: Implements a custom pagination class (`DefaultPagination`) for controlling the number of items displayed per page in API views.

### 9. **URLs**
   - Location: `store/urls.py`
   - Description: Configures URL patterns for the API, including routes for products, collections, carts, customers, orders, reviews, and cart items.

### 10. **External Libraries**
   - Django REST Framework: Utilized for building robust APIs.
   - Django Filter: Employed for implementing filters in API views.

## Getting Started

To set up and run this project on your local machine, follow the instructions provided in the README.md file. Detailed steps include cloning the repository, activating the virtual environment, installing dependencies, performing database migrations, creating an admin identity, and running the development server.

## Contribution Guidelines

Contributions to the project are welcome! Please refer to the CONTRIBUTING.md file for guidelines on submitting issues, feature requests, or pull requests.

Thank you for choosing the Django Ecommerce API. Happy coding!
