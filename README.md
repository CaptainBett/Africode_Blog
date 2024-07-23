# Flask Blog Application

This is a simple blog application built with Flask, a popular Python web framework. The application allows users to create accounts, post blog posts, and comment on others' posts.

## Table of Contents

- [Getting Started](#getting-started)
- [Cloning the Project](#cloning-the-project)
- [Running the Application](#running-the-application)
- [Contributing to the Project](#contributing-to-the-project)
- [About Africode Academy](#about-africode-academy)

## Getting Started

Before you begin, make sure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)
- Git

## Cloning the Project

To clone the project, open your terminal or command prompt and run the following command:

```bash
git clone https://github.com/your-username/flask-blog-app.git
```

Replace `your-username` with your GitHub username.

## Running the Application

After cloning the project, navigate to the project directory:

```bash
cd flask-blog-app
```

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # For Unix/Linux/MacOS
# or
venv\Scripts\activate  # For Windows
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Set up the database:

```bash
python
from app import db
db.create_all()
exit()
```

Run the application:

```bash
flask run
```

The application will start running on `http://127.0.0.1:5000/`.

## Contributing to the Project

To contribute to the project, follow these steps:

1. Fork the repository on GitHub.
2. Clone your fork: `git clone https://github.com/your-username/flask-blog-app.git`
3. Create a new branch for your changes: `git checkout -b your-feature-branch`
4. Make your changes and commit them: `git commit -m "Add your commit message"`
5. Push your changes to your fork: `git push origin your-feature-branch`
6. Create a pull request on GitHub.

## About Africode Academy

[Africode Academy](https://africodeacademy.com/) is a coding school dedicated to teaching web development, programming, and data science to students from Africa. It offers a variety of courses and workshops, including Python, JavaScript, and web design. Africode Academy is committed to fostering a diverse and inclusive coding community in Africa.
