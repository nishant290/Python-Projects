# Pyhton-Projects
In this repo, I have shared the projects that includes the concepts loke "Web Scraping" and "News Fetching using Django and API"

# Python Projects

This repository contains two independent Python projects:

1. **Auto News Fetcher & Dashboard (Django-based web app)**  
2. **Flipkart Watch Scraper (Python + BeautifulSoup)**  

Both are included here for learning and demonstration.

---

## 1. Auto News Fetcher & Dashboard

### 📌 Project Goal
A Django web application that:
- Fetches the latest news headlines from a public API.  
- Stores them in a database (`NewsArticle` model).  
- Displays them in a simple dashboard.  
- Allows fetching fresh news via a button or a custom command.  

---

### ⚙️ Setup Instructions (Windows)

```bash
# Clone this repository
git clone https://github.com/nishant290/Python-Projects.git
cd Python-Projects/auto_news

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create a file named .env in the project root (auto_news/) with:
# DEBUG=True
# SECRET_KEY=changeme
# NEWS_API_KEY=your_api_key_here

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver

python -m venv venv
venv\Scripts\activate
```
## Install Dependencies

Auto News Fetcher & Dashboard
Project Explanation

A Django-based web app that:

Fetches the latest news headlines from a news API.

Stores them in a SQLite database (NewsArticle model).

Displays them in a web dashboard.

Allows fetching fresh news manually (button) or via a custom management command.

How to Run
cd auto_news

# Set up environment variables
# Create a file named .env inside auto_news/ with:
# DEBUG=True
# SECRET_KEY=changeme
# NEWS_API_KEY=your_api_key_here

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver


##Open in browser:

Dashboard → http://127.0.0.1:8000/

Admin → http://127.0.0.1:8000/admin

Fetch Latest News

Option 1 → Click "Fetch Latest News" in the dashboard UI.
Option 2 → Run the custom command:

python manage.py fetchnews

