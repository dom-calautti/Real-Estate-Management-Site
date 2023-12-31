# Real-Estate-Management-Site
www.dcrealestate.shop <br />
A demo real estate website built with Python, Django, Bootstrap, PostgreSQL, and HTML/CSS.

## Overview

This Django-based real estate website is a comprehensive platform that facilitates property search, user inquiries, and administrative management. Users can filter home listings based on parameters such as bedroom count, price, keywords, state, and city. Additionally, the website supports user account creation and inquiries with agents for each listing, allowing users to provide their contact information. Admin accounts are available for administrators to manage listings, realtors, and site content.

## Features

- **Property Listings:** Display a list of available properties with detailed information.
- **Search Functionality:** Users can filter home listings based on parameters such as bedroom count, price, keywords, state, and city.
- **User Authentication:** Users can register, log in, and manage their profiles.
- **Inquiries with Agents:** Users can make inquiries with agents for each listing, providing their contact information.
- **Admin Panel:** An intuitive admin interface to manage property listings, realtors, user accounts, and site content.
- **Admin Capabilities:** Admins can add new property listings and manage realtor accounts in the admin section.
- **Responsive Design:** Ensures a seamless experience across various devices and screen sizes.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/real-estate-django.git
    cd real-estate-django
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to [http://localhost:8000](http://localhost:8000) to view the application.

## Usage

1. Access the admin panel at [http://localhost:8000/admin](http://localhost:8000/admin) to manage property listings, realtors, and user accounts.
2. Explore the public site to browse and search for properties, make inquiries, and create an account.

## Contributing

Contributions are welcome! 
