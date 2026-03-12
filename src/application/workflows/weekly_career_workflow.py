from datetime import datetime
import os
import json
from src.domain.entities.career import CareerGoal
from src.infrastructure.whatsapp.meta_client import MetaWhatsAppClient
from src.application.agents.mentor_agent import MentorAgent
from src.application.agents.coordinator_agent import CoordinatorAgent

# Simple file-based memory simulation for the mentor agent
MEMORY_FILE = "mentor_memory.json"

def get_past_advice():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_past_advice(advice):
    past = get_past_advice()
    past.append(advice)
    # keep only last 5
    with open(MEMORY_FILE, "w") as f:
        json.dump(past[-5:], f)

def execute_weekly_career_workflow():
    target_number = os.getenv("WHATSAPP_TARGET_NUMBER")
    if not target_number:
        print("WHATSAPP_TARGET_NUMBER is missing. Cannot send messages.")
        return

    print("Starting Weekly Career Advice Workflow...")
    
    goal = CareerGoal()
    today_str = datetime.now().strftime("%B %d, %Y")
    past_advice = get_past_advice()

    # 1. Generate Advice using AI Mentor Agent
    mentor_agent = MentorAgent()
    advice = mentor_agent.generate_weekly_advice(goal, today_str, past_advice)

    # 2. Format and Dispatch
    whatsapp_client = MetaWhatsAppClient()
    coordinator = CoordinatorAgent(whatsapp_client)
    
    success = coordinator.dispatch_weekly_advice(advice, target_number)
    
    if success:
        # 3. Update memory
        save_past_advice(advice.system_design_concept)
        print("Weekly Career Workflow Completed Successfully.")
