🚀 Features
🔐 Authentication

User registration & login

JWT authentication

Password encryption

Email verification (optional)

👤 User Profiles

Create & update profile

Upload profile pictures

Set dating preferences

View other profiles

Profile filtering & search

❤️ Matchmaking

Swipe-like “like / dislike” system

Suggested matches based on preferences

Mutual match detection

Block/report users

💬 Messaging

Chat between matched users

Message history endpoints

Real-time support (optional via WebSockets)

📍 Location-Based Features

Search or match by distance

Geolocation filters

🏗 Tech Stack

Python 3.x

Django 4.x

Django REST Framework

SimpleJWT


dating_app/
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── profiles/
│   ├── models.py
│   ├── views.py
│   └── serializers.py
├── matches/
│   ├── models.py
│   ├── views.py
│   └── serializers.py
├── messages/
│   ├── models.py
│   ├── views.py
│   └── serializers.py
├── settings.py
├── urls.py
└── requirements.txt



PostgreSQL / SQLite

Cloud storage support (AWS S3 / Cloudinary)


⚙ Installation

Clone the repository:

git clone https://github.com/hamzabajwa79-web/dating-py
cd dating-py


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Run the server:

python manage.py runserver
