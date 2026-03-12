import os
from google import genai
from google.genai import types
from typing import List
from src.domain.entities.news import DailyNewsCurated, NewsArticle

class NewsAgent:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key)

    def process_news(self, raw_articles: List[NewsArticle], date: str) -> DailyNewsCurated:
        """Takes raw scraped articles and uses Gemini to curate and summarize the top tech news."""
        
        prompt = f"""
        You are an expert tech news curator. I will provide you with a list of raw tech news headlines and descriptions scraped from the web today ({date}).
        Please curate them, rewrite the summaries to be engaging, and return a JSON object that matches the DailyNewsCurated schema.
        Exclude any non-tech or generic news. Keep the top 5-10 most relevant to a software engineering audience.
        Ensure you add a nice `intro_message` greeting for the morning.
        
        Raw Articles:
        {[art.model_dump() for art in raw_articles]}
        """

        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=DailyNewsCurated,
                    temperature=0.3
                ),
            )
            
            # The SDK automatically handles the Pydantic parsing if configured correctly, 
            # or we can manually parse the JSON string response
            return DailyNewsCurated.model_validate_json(response.text)
        except Exception as e:
            print(f"Error processing news with Gemini: {e}")
            # Fallback
            return DailyNewsCurated(
                date=date,
                articles=raw_articles[:5],
                intro_message="Here are your raw tech news highlights for today."
            )
