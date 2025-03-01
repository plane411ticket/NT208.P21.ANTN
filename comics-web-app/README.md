# Comics Web App

This project is a web application designed to support various types of comics, including reading comics, listening to audio comics, and reading stories in Vietnamese. The application is structured into two main parts: the client and the server.

## Project Structure

```
comics-web-app
├── client                # Frontend application built with React
│   ├── public            # Static files (images, icons, etc.)
│   ├── src               # Source files for the React application
│   │   ├── assets        # Various assets (images, fonts)
│   │   ├── components    # Reusable React components
│   │   ├── pages         # Main pages of the application
│   │   ├── App.js        # Main component for application structure and routing
│   │   └── index.js      # Entry point of the React application
│   ├── package.json      # npm configuration file
│   └── README.md         # Documentation for the client-side application
├── server                # Backend application built with Django
│   ├── comics            # Django app for managing comics
│   │   ├── __init__.py   # Marks the comics directory as a Python package
│   │   ├── admin.py      # Admin site configuration
│   │   ├── apps.py       # Application configuration
│   │   ├── models.py     # Data models for comics
│   │   ├── tests.py      # Tests for the comics application
│   │   └── views.py      # View functions for handling requests
│   ├── project           # Django project configuration
│   │   ├── __init__.py   # Marks the project directory as a Python package
│   │   ├── settings.py    # Project settings (including MySQL database configuration)
│   │   ├── urls.py       # URL routing for the application
│   │   └── wsgi.py       # WSGI entry point for serving the application
│   ├── manage.py         # Command-line utility for Django project
│   ├── requirements.txt   # Required Python packages for the server
│   └── README.md         # Documentation for the server-side application
├── .gitignore            # Files and directories to ignore by Git
└── README.md             # General documentation for the entire project
```

## Technologies Used

- **Frontend**: React
- **Backend**: Django
- **Database**: MySQL

## Getting Started

To get started with the project, clone the repository and install the necessary dependencies for both the client and server.

### Client

1. Navigate to the `client` directory.
2. Run `npm install` to install the required packages.
3. Start the development server with `npm start`.

### Server

1. Navigate to the `server` directory.
2. Create a virtual environment and activate it.
3. Run `pip install -r requirements.txt` to install the required packages.
4. Run the server with `python manage.py runserver`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.