from datetime import datetime
import os
from src.infrastructure.scraping.web_scraper import WebScraper
from src.infrastructure.whatsapp.meta_client import MetaWhatsAppClient
from src.application.agents.news_agent import NewsAgent
from src.application.agents.coordinator_agent import CoordinatorAgent

def execute_daily_news_workflow():
    target_number = os.getenv("WHATSAPP_TARGET_NUMBER")
    if not target_number:
        print("WHATSAPP_TARGET_NUMBER is missing. Cannot send messages.")
        return

    print("Starting Daily News Workflow...")
    
    # 1. Scrape raw news
    scraper = WebScraper()
    raw_articles = scraper.fetch_top_news(limit=10)
    
    if not raw_articles:
        print("No articles fetched today.")
        return

    # 2. Curate using AI Agent
    news_agent = NewsAgent()
    today_str = datetime.now().strftime("%B %d, %Y")
    curated_news = news_agent.process_news(raw_articles, today_str)

    # 3. Format and Dispatch via WhatsApp Coordinator
    whatsapp_client = MetaWhatsAppClient()
    coordinator = CoordinatorAgent(whatsapp_client)
    
    coordinator.dispatch_daily_news(curated_news, target_number)
    print("Daily News Workflow Completed Successfully.")
