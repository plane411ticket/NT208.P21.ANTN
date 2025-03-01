# FILE: /comics-web-app/comics-web-app/server/README.md

# Comics Web App - Server

This is the server-side of the Comics Web App project, built using Django and MySQL. The server handles all backend operations, including data storage, user authentication, and serving comic content.

## Project Structure

- **comics/**: Contains the Django application for managing comics.
  - **admin.py**: Register models with the Django admin site.
  - **apps.py**: Configuration for the comics application.
  - **models.py**: Defines data models for comics, including fields for comic details.
  - **tests.py**: Contains tests for the comics application.
  - **views.py**: Handles requests and returns responses for the comics.

- **project/**: Contains the main Django project settings and configurations.
  - **settings.py**: Configuration settings for the Django project, including MySQL database settings.
  - **urls.py**: Defines URL routing for the application.
  - **wsgi.py**: Entry point for WSGI-compatible web servers.

- **manage.py**: Command-line utility for interacting with the Django project.

- **requirements.txt**: Lists the Python packages required for the server-side application.

## Setup Instructions

1. **Install Dependencies**: 
   Ensure you have Python and pip installed. Then, install the required packages using:
   ```
   pip install -r requirements.txt
   ```

2. **Database Configuration**: 
   Update the `settings.py` file with your MySQL database credentials.

3. **Run Migrations**: 
   Apply database migrations with:
   ```
   python manage.py migrate
   ```

4. **Start the Server**: 
   Run the development server using:
   ```
   python manage.py runserver
   ```

## Features

- Support for reading comics.
- Audio comics for listening.
- Reading stories in Vietnamese.

## License

This project is licensed under the MIT License.