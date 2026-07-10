# Module 4 Django Tutorial

This project was created for the SDEV 220 Django tutorial assignment.

## Completed Tutorial Sections

- Django installation
- First Django project
- Django models
- Django admin

## Project Description

This Django project contains a simple food pantry app named pantry. The app includes a FoodItem model with fields for item name, category, quantity, and expiration date.

The FoodItem model is registered with the Django admin site so food items can be added, viewed, edited, and deleted through the admin interface.

## Model Used

FoodItem fields:

- item_name
- category
- quantity
- expiration_date

## How to Run

1. Open the project in VS Code.
2. Activate the virtual environment with this command:

   .venv\Scripts\activate

3. Run the Django server with this command:

   python manage.py runserver

4. Open the site in a browser:

   http://127.0.0.1:8000/

5. Open the admin page:

   http://127.0.0.1:8000/admin/

## Screenshots / Testing

The project was tested by running the Django development server, opening the Django welcome page, logging into the Django admin panel, and adding a sample food item named Canned Corn.