# 🧠 MSME Credit Agent

This is a fully self-contained backend for onboarding and scoring small businesses using your own APIs and machine learning.

# 🌍 Project Overview

Over 60% of Ethiopian MSMEs operate informally, making it difficult for banks to evaluate creditworthiness.
This project aims to change that — by helping small businesses collect financial data digitally and generate AI-powered credit scores using alternative data sources like mobile money or digital payments.
 

## 🚀 Current Progress

### ✅ Week 1 — Custom API Foundation
- Set up FastAPI backend from scratch  
- Created clean folder structure  
- Implemented `/onboard` endpoint to collect MSME data  
- Added `README.md` and tested routes via Swagger  

### ✅ Week 2 — Onboarding Chatbot *(Planned)*
- Telegram/WhatsApp chatbot integration (Twilio or Telegram Bot API)  
- Sends collected info to `/onboard` endpoint  

### ✅ Week 3 — Backend & Database Integration
- Added SQLite database (auto-created via SQLAlchemy)  
- Created tables:
  - `businesses` (stores MSME info)
  - `transactions` (stores uploaded transactions)
- Added new endpoints:
  - `/onboard/` — onboard new MSMEs
  - `/transactions/upload` — upload fake or real transaction data
  - `/score/{business_id}` — mock credit scoring endpoint

---



### Project Structure

```
mesaaiagent/
├── backend/
│ ├── main.py # FastAPI app entry
│ ├── db.py # Database connection
│ ├── models.py # SQLAlchemy models
│ ├── routers/
│ │ ├── onboarding.py # /onboard endpoint
│ │ ├── transactions.py # /transactions/upload endpoint
│ │ └── scoring.py # /score/{business_id} endpoint
│ └── init.py
├── ml/ # Future ML models (LightGBM, SHAP)
├── chatbot/ # Future chatbot integration (Telegram/Twilio)
├── simulator/ # Fake transaction generator
├── dashboard/ # Web UI (coming later)
├── requirements.txt
└── README.md
```



### Run Locally

### 1️⃣ Clone the repository

```bash

git clone https://github.com/Hayat373/msme-credit-agent.git
cd msme-credit-agent
```

### 2️⃣ Create virtual environment

```bash 

python -m venv venv
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install dependencies

```bash 
cd backend
pip install -r requirements.txt

```

### 4️⃣ Run the FastAPI app
``` bash

uvicorn backend.main:app --reload

```



## Test Endpoints

   Visit http://127.0.0.1:8000/docs

    Try the /onboard POST endpoint to onboard a business.

## 🧪 Test Your API (Thunder Client or Swagger UI) 

### 1️⃣ Onboard a Business

    POST -> http://127.0.0.1:8000/onboard/

###  2️⃣ Upload a Transaction

      POST-> http://127.0.0.1:8000/transactions/upload

### 3️⃣ Request a (Mock) Credit Score 

GET -> http://127.0.0.1:8000/score/id 