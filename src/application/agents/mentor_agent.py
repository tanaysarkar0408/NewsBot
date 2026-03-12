import os
from google import genai
from google.genai import types
from src.domain.entities.career import CareerGoal, WeeklyCareerAdvice

class MentorAgent:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key)

    def generate_weekly_advice(self, goal: CareerGoal, date: str, past_advice: list[str]) -> WeeklyCareerAdvice:
        """Generates weekly career advice for a MAANG SDE-1 aspirant."""
        
        prompt = f"""
        You are an elite Career Mentor helping a candidate prepare for an {goal.target_role} role at {", ".join(goal.target_companies)}.
        Today is {date}. 
        The candidate is currently focusing on: {goal.focus_areas if goal.focus_areas else 'general software engineering'}.
        
        Here are the topics you've suggested in the past weeks so you DON'T repeat them:
        {past_advice}

        Provide a structured plan for this week. It MUST include:
        1. A specific topic or tech stack to learn.
        2. A small, impressive project idea that MAANG recruiters love.
        3. A specific system design concept to understand deep dive.
        4. A motivational quote.
        
        Return the response strictly matching the requested JSON schema.
        """

        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=WeeklyCareerAdvice,
                    temperature=0.7
                ),
            )
            
            return WeeklyCareerAdvice.model_validate_json(response.text)
        except Exception as e:
            print(f"Error generating mentor advice: {e}")
            return WeeklyCareerAdvice(
                date=date,
                learning_suggestion="Focus on fundamental data structures and algorithms.",
                project_idea="Build a simple key-value store.",
                system_design_concept="Understand the concept of a Load Balancer.",
                motivational_quote="Keep grinding."
            )
