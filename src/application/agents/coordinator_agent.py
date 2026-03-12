from src.domain.entities.news import DailyNewsCurated
from src.domain.entities.career import WeeklyCareerAdvice
from src.domain.interfaces.whatsapp_client import IWhatsAppClient

class CoordinatorAgent:
    """Formats the data from other agents into a beautiful WhatsApp message and sends it."""
    
    def __init__(self, whatsapp_client: IWhatsAppClient):
        self.whatsapp_client = whatsapp_client

    def dispatch_daily_news(self, curated_news: DailyNewsCurated, recipient_number: str):
        message = f"🌅 *Good Morning!* {curated_news.intro_message}\n\n*Top Tech News for {curated_news.date}*\n\n"
        
        for i, article in enumerate(curated_news.articles, 1):
            message += f"{i}. *{article.title}*\n"
            message += f"_{article.summary[:100]}..._\n"
            message += f"🔗 {article.url}\n\n"
            
        message += "Stay curious! 🚀\n"
        
        print("\n--- GENERATED NEWS MESSAGE ---")
        print(message)
        print("------------------------------\n")
        
        return self.whatsapp_client.send_message(recipient_number, message)

    def dispatch_weekly_advice(self, advice: WeeklyCareerAdvice, recipient_number: str):
        message = f"🎯 *Your Weekly SDE-1 Masterplan for {advice.date}*\n\n"
        message += f"*{advice.motivational_quote}*\n\n"
        
        message += f"📚 *What to Learn Next:*\n{advice.learning_suggestion}\n\n"
        message += f"🛠️ *Weekly Project Idea:*\n{advice.project_idea}\n\n"
        message += f"🏗️ *System Design Focus:*\n{advice.system_design_concept}\n\n"
        
        message += "Let's get that MAANG offer! 💻✨"
        
        return self.whatsapp_client.send_message(recipient_number, message)
