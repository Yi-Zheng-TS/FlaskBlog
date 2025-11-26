✅ Flask Blog Web Application

📌 Project Overview
This is a full-stack blog web application built with Flask. The project focuses on building a complete blogging system with user authentication, post management, and a clean front-end interface. It was developed to strengthen my skills in Python web development, backend logic, database modeling, and front-end integration.
Users can register, log in, create blog posts, and view content through a simple and user-friendly interface. The application follows a clear project structure and demonstrates real-world web development practices.

🚀 Tech Stack
Backend: Python, Flask
Database: SQLite (via SQLAlchemy)
Frontend: HTML, CSS
Form Handling: Flask-WTF
Authentication: Flask-Login
Deployment Interface: WSGI
Environment Management: Virtual Environment, requirements.txt

🗂 Project Structure
flask-blog/
│
├── blog/
│   ├── static/
│   │   ├── img/
│   │   └── style.css
│   │
│   ├── templates/
│   │   ├── layout.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── post.html
│   │   ├── posts.html
│   │   ├── success.html
│   │   └── thank.html
│   │
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   └── routes.py
│
├── .gitignore
├── requirements.txt
└── wsgi.py

⚙️ How to Run the Project
1. Clone the repository:
git clone <your-repo-url>
2. Create a virtual environment:
python -m venv venv
3. Activate the environment:
Windows:
venv\Scripts\activate
4. Install dependencies:
pip install -r requirements.txt
5. Run the application:
python wsgi.py
6. Open in browser:
http://127.0.0.1:5000/

🧠 What I Learned
Building REST-style routes with Flask
Structuring a scalable Flask project
Handling user authentication and sessions
Working with databases using SQLAlchemy
Front-end and back-end integration
Debugging and testing web applications
Managing project dependencies with requirements.txt

📈 Future Improvements
Add image uploads for posts
Implement user roles (admin/editor)
Improve UI with a modern frontend framework
Add unit tests for backend routes
Deploy to a cloud platform (e.g. AWS or Render)

👤 Author
Yi Zheng
Junior Software Engineer
Python | Flask | SQL | C++
