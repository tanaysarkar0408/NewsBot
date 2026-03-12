from apscheduler.schedulers.blocking import BlockingScheduler
from src.application.workflows.daily_news_workflow import execute_daily_news_workflow
from src.application.workflows.weekly_career_workflow import execute_weekly_career_workflow
import os

def start_scheduler():
    print("Starting APScheduler...")
    scheduler = BlockingScheduler()

    # Daily News at 8:00 AM
    scheduler.add_job(
        execute_daily_news_workflow, 
        'cron', 
        hour=8, 
        minute=0, 
        id='daily_tech_news'
    )
    
    # Weekly Career Advice on Sunday (0=Mon, 6=Sun) at 8:30 AM
    scheduler.add_job(
        execute_weekly_career_workflow, 
        'cron', 
        day_of_week='sun', 
        hour=8, 
        minute=30, 
        id='weekly_career_advice'
    )
    
    # FOR TESTING PURPOSES ONLY: Uncomment to run jobs 10 seconds after start
    # from datetime import datetime, timedelta
    # run_time = datetime.now() + timedelta(seconds=10)
    # scheduler.add_job(execute_daily_news_workflow, 'date', run_date=run_time)
    # scheduler.add_job(execute_weekly_career_workflow, 'date', run_date=run_time + timedelta(seconds=20))

    try:
        print("Scheduler is active. Waiting for jobs...")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")
