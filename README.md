# MSME Credit Agent

This is a fully self-contained backend for onboarding and scoring small businesses using your own APIs and machine learning.

## Week 1: Custom API Foundation

**Goal:** Build your own FastAPI backend (no external APIs).

### Project Structure

```
backend/    - FastAPI API backend
ml/         - Machine learning model code
chatbot/    - Chatbot integration (e.g., Telegram)
simulator/  - Fake transaction generator for testing
dashboard/  - Simple web UI for monitoring and interaction
```



### Run Locally
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```


## Test Endpoints

   Visit http://127.0.0.1:8000/docs

    Try the /onboard POST endpoint to onboard a business.

## Next Week

Add a Telegram chatbot that connects to this API

Save onboarding data into a database (PostgreSQL)

Return a “mock credit score” from your backeend

```
---

## ✅ Week 1 Deliverables

| Deliverable | Description | Status |
|--------------|-------------|--------|
| ✅ Folder structure | Organized project directories | |
| ✅ Custom FastAPI backend | Runs locally | |
| ✅ `/onboard` API endpoint | Collects business info | |
| ✅ Working docs | `/docs` page works | |
| ✅ README.md | Explains setup and usage | |

---

## 🎯 What you’ll learn this week

- How REST APIs work (requests, responses, JSON)
- How to build endpoints using FastAPI
- How to define data models using Pydantic
- How to organize a backend project
- How to test APIs using Swagger UI

---

Would you like me to add a **Week 1 extension task** that shows you how to **save onboarded data to a local SQLite database** (so it doesn’t disappear when you restart)?  
It’s the perfect small “extra credit” step before Week 2 (when we’ll connect the chatbot).
```