# Shopify Backend Intern Summer 2022 Challenge

**TASK**: Build an inventory tracking web application for a logistics company.

**Additional feature**: Push a button to export product data to a CSV. This can be achieved by pressing the "Export to CSV" button on the home page.

## Installation instructions

### Python

To install Python, use one of the installers [here](https://www.python.org/downloads/release/python-3101/).

### Poetry (Python dependency manager)

To install Poetry, follow the instructions [here](https://python-poetry.org/docs/#installation).

## Usage instructions

1. Clone the project using the following command:

    ```
    git clone git@github.com:Gadiguibou/shopify-backend-intern-challenge-summer-2022.git
    ```

    or by downloading it as a zip file from the GitHub UI and unzipping it into the directory of your choice.

2. Run the following command to install the dependencies (the only direct dependency is Django):

    ```
    poetry install
    ```
    
3. `cd` into `inventorytracker`, then run the following command to initialize the database (Django uses SQLite by default):

    ```
    poetry run python manage.py migrate
    ```

4. Run the following command to start the development server:

    ```
    poetry run python manage.py runserver
    ```

5. Open a browser and navigate to http://localhost:8000/ to see the home page or http://localhost:8000/admin/ to see the admin page.[^1]

[^1]: To create a superuser account for the admin page use the following command:

    ```
    poetry run python manage.py createsuperuser
    ```

## Downloading the entire inventory as a CSV

To download the inventory as a CSV, run the dev server, navigate to the home page (http://localhost:8000/) and click on the link named "Download inventory as CSV". 
