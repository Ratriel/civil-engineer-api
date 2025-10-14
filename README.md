# Civil Engineer Consulting — AI Portfolio & Seismic Data API

This project combines AI-powered portfolio generation and real-time civil engineering data analysis.

## 🚀 Overview

- **Frontend:** Static React app deployed on [Vercel](https://civilengineerconsulting.vercel.app/)
- **Backend:** Django REST API with AI integration (LangChain + OpenAI)
- **Future Microservice:** Web scraping module for seismic data (Costa Rica + USGS)

## 🧩 Tech Stack

- Python 3.11 / Django 4.2
- Django REST Framework
- LangChain + OpenAI API
- CORS Headers + Dotenv
- Deployed on [Render.com](https://render.com)

## ⚙️ Local Setup

```bash
git clone <repo-url>
cd django_rest
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py runserver


🌐 Deployment

Create a new Web Service on Render

Connect to this GitHub repository

Add environment variables:

OPENAI_API_KEY=your-key

DEBUG=False

Render will automatically build and serve your app using:
gunicorn backend.wsgi


🤖 AI Agent Modules

ai/portfolio_agent.py: Generates personalized AI-based CVs.

ai/civil_engineering_agent.py: Responds to seismic and structural questions.

earthquakes/: Data scrapers and integration with USGS API.

📦 Next Steps

Add Docker support for microservice-based scraping.

Extend API endpoints for structured portfolio rendering.

Introduce database (PostgreSQL or SQLite-to-Postgres migration).

🧠 Developed by Ariel Lopez Castillo