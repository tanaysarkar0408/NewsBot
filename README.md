# Agentic WhatsApp Tech Bot 🤖📱

An automated, multi-agent AI system built using Python and the Google GenAI SDK. This project leverages **Clean Architecture** to deliver highly curated daily tech news and weekly MAANG-focused career advice directly to your WhatsApp.

## 🌟 Features

- **Multi-Agent Orchestration**: Specialized agents handle specific tasks (News Scraping, Career Mentoring, WhatsApp Formatting).
- **Daily Tech News Briefing**: Uses `BeautifulSoup` to scrape Google News RSS and `Gemini 2.5` to distill the top articles.
- **Weekly Career Mentor**: An SDE-1 focused mentor agent that utilizes local memory to prevent repeating advice, providing unique System Design concepts and project ideas every Sunday.
- **WhatsApp Meta integration**: Delivers beautifully formatted markdown messages directly to your phone.
- **Clean Architecture Implementation**: Strict separation of Domain, Application, and Infrastructure layers.

## 🏗️ Architecture

The system is designed with **Dependency Inversion** and **Clean Architecture (Onion)**:

- `src/domain/`: Defines zero-dependency `Pydantic` entities (`NewsArticle`, `CareerGoal`) and abstract component interfaces.
- `src/application/`: Contains the Google GenAI multi-agent workers (`NewsAgent`, `MentorAgent`) and the core orchestrating workflows.
- `src/infrastructure/`: Houses concrete implementations like the `MetaWhatsAppClient`, `BeautifulSoup` WebScraper, and the `APScheduler` Cron jobs.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A Google Gemini API Key
- A Meta Developer Account (WhatsApp Cloud API credentials)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/NewsBot.git
cd NewsBot
```

2. Create and activate a Virtual Environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Environment Variables:
Create a `.env` file in the root directory:
```env
WHATSAPP_PHONE_NUMBER_ID=your_id
WHATSAPP_TOKEN=your_token
WHATSAPP_TARGET_NUMBER=your_phone_number

GEMINI_API_KEY=your_gemini_key
```

### Usage

**Start the Production Scheduler:**
The system will run continuously, triggering the News workflow daily at 8:00 AM, and the Mentor workflow on Sundays at 8:30 AM.
```bash
python main.py
```

**Trigger Single Workflows (Testing):**
```bash
# Test the Morning News Generation
python main.py --test-news

# Test the Weekly Career Advice
python main.py --test-career
```

## 🧠 System Design Concepts Used

1. **Idempotency & Event-Driven triggers**: Handled via APScheduler CRON jobs.
2. **Structured LLM Outputs**: Enforcing Pydantic schemas in the Gemini API.
3. **Agent-to-Agent (A2A) Handoff**: Dedicated Orchestrator agents cleanly receiving payloads from specialist agents.

## 🗺️ Roadmap: Scaling to Multi-Tenant
**Currently, the bot operates as a single-user instance. The next major architectural iteration will transform this into a scalable, multi-tenant service:**

**Two-Way Communication:** Implement FastAPI webhooks to listen for incoming WhatsApp messages, allowing users to opt-in and select their specific tech niches (e.g., "Python Backend", "System Design", "Cloud").

**Persistent Storage:** Integrate a relational database (PostgreSQL) to manage user profiles, active subscriptions, and article delivery history to prevent duplicate content.

**Distributed Task Processing:** Migrate from local APScheduler cron jobs to an asynchronous task queue using Celery with a Redis or Kafka message broker. This will ensure reliable, decoupled message dispatching to hundreds of users simultaneously without bottlenecking the main application thread.

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
