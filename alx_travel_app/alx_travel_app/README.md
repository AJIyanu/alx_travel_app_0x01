# ALX Travel App

---

## Overview

The ALX Travel App is a robust, real-world Django application designed as a comprehensive platform for travel listings. This project emphasizes industry-standard best practices, focusing on a scalable backend, efficient database management, and seamless API documentation. Built with a passion for clean code and maintainable configurations, this application serves as a foundational example of how to develop and manage a high-quality Django-based service.

---

## Features

- **Scalable Backend Architecture:** Engineered with a modular and extensible Django framework, ready to handle future features and increased user loads.
- **MySQL Database Integration:** Utilizes MySQL for reliable and efficient data storage and retrieval, ensuring data integrity and performance.
- **Automated API Documentation with Swagger:** Integrates Swagger (via DRF Spectacular) to provide interactive and up-to-date API documentation, facilitating seamless team collaboration and external integrations.
- **Maintainable Configurations:** Implements structured environment variables and settings management for easy deployment and configuration across different environments.

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip (Python package installer)
- MySQL Server

### Installation

1.  **Clone the repository:**

    ```
    git clone [https://github.com/AJIyanu/alx_travel_app](https://github.com/AJIyanu/alx_travel_app)
    cd alxtravelapp
    ```

2.  **Create and activate a virtual environment:**

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory of the project with your database credentials and other sensitive information. Refer to ` .env.example` for required variables.

    ```
    # .env example
    DATABASE_NAME=alxtravelapp_db
    DATABASE_USER=your_mysql_user
    DATABASE_PASSWORD=your_mysql_password
    DATABASE_HOST=127.0.0.1
    DATABASE_PORT=3306
    SECRET_KEY=your_django_secret_key
    DEBUG=True
    ```

5.  **Run Migrations:**

    ```
    python manage.py migrate
    ```

6.  **Run the Development Server:**

    ```
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

---

## API Documentation

Access the interactive API documentation via Swagger UI at:

`http://127.0.0.1:8000/api/docs/`

This documentation provides a comprehensive overview of all available API endpoints, their expected inputs, and sample responses.

---

## Built With

- **Django:** The web framework used for crafting the robust backend.
- **Django REST Framework:** For building powerful and flexible APIs.
- **MySQL:** The relational database management system.
- **DRF Spectacular:** For automatic API schema generation and Swagger UI.

---

## Contributing

This project is a personal endeavor showcasing best practices in Django development. While not actively seeking external contributions for feature development, feedback on code quality and architectural improvements is always welcome.

---

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## Acknowledgments

- Special thanks to the ALX Holberton School curriculum for inspiring this project's foundational structure and best practices.
