# Personal Assistant

The **Personal Assistant** is a web application built with Django that helps users manage their contacts, notes, and files, and provides a daily news summary. The application is designed to store important information in a PostgreSQL database, ensuring data reliability and security.

## Features

- **Contact Management**: Store contacts with names, addresses, phone numbers, emails, and birthdays. Search, edit, and delete contacts. Validate phone numbers and emails during creation or editing. Display contacts with upcoming birthdays.
- **Notes Management**: Create, edit, delete, and search notes with text information. Add tags to notes for easy categorization and search by keywords.
- **File Management**: Upload and store user files in a cloud service. Categorize files by type (images, documents, videos, etc.) and filter files by category.
- **Daily News Summary**: Provide a brief summary of daily news in a chosen field (e.g., finance, sports, politics, weather). Collect and display information from selected news sources, such as news headlines, currency rates, and sports results.

## Project Requirements

- The web interface is implemented using the Django framework.
- The project is stored in a public repository (GitHub, GitLab, or BitBucket).
- Detailed installation and usage instructions are included.
- The application uses a PostgreSQL database to store information and can be restarted without data loss.
- All critical data for database access and application configuration is stored in environment variables and not uploaded to the repository.

## Installation and Setup

### Prerequisites

- Python 3.x
- Poetry
- PostgreSQL

## Setup Instructions

To set up and run the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone git@github.com:PYOrm/Personal_Assistant.git
    cd Personal_Assistant
    ```

2. **Create a virtual environment**:

    This project uses Poetry to manage dependencies. If you haven't installed Poetry yet, you can do so by following the [official guide](https://python-poetry.org/docs/#installation).

3. **Add `.env` file**:

    Add a `.env` file to the root of your project directory with the following content:

    ```dotenv
    DB_ENGINE='django.db.backends.postgresql'
    DB_NAME='postgres'  
    DB_USER='postgres'  
    DB_PASSWORD='postgres'  
    DB_HOST='localhost'  
    DB_PORT='5432'
    FILESHARE_API_KEY=*************** # Generate a development token from box.com
    ```

4. **Install dependencies**:

    Run the following command to install all necessary dependencies:

    ```bash
    poetry install
    ```

5. **Run database migrations**:

    Apply the necessary database migrations using Django's migrate command:

    ```bash
    poetry run python manage.py migrate
    ```

6. **Start the application**:

    Run the main application:

    ```bash
    poetry run python main.py
    ```

## Features

- User registration and login
- Author and quote management
- Integration with external file-sharing service (Box)
- PostgreSQL database support

## Environment Variables

The project requires several environment variables defined in a `.env` file:

- `DB_ENGINE`: Database engine, set to use PostgreSQL.
- `DB_NAME`: Name of the database.
- `DB_USER`: Database user.
- `DB_PASSWORD`: Password for the database user.
- `DB_HOST`: Host for the database.
- `DB_PORT`: Port for the database connection.
- `FILESHARE_API_KEY`: API key for file-sharing service.

Make sure to generate a development token from [Box.com](https://box.com) for `FILESHARE_API_KEY`.
