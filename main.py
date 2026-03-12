from dotenv import load_dotenv
import os
import sys

# Ensure src is in the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.infrastructure.scheduler.cron_jobs import start_scheduler
from src.application.workflows.daily_news_workflow import execute_daily_news_workflow
from src.application.workflows.weekly_career_workflow import execute_weekly_career_workflow

def main():
    # Load environment variables from .env
    print("Loading environment variables...")
    load_dotenv()
    
    print("WhatsApp Multi-Agent System Initializing...")
    
    # Optional testing arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test-news":
            print("Triggering News Workflow directly...")
            execute_daily_news_workflow()
            return
        elif sys.argv[1] == "--test-career":
            print("Triggering Career Workflow directly...")
            execute_weekly_career_workflow()
            return

    # Start the continuous scheduler
    start_scheduler()

if __name__ == "__main__":
    main()
