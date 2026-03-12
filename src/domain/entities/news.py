from pydantic import BaseModel, Field
from typing import List

class NewsArticle(BaseModel):
    title: str = Field(..., description="The headline of the news article")
    summary: str = Field(..., description="A short summary of the article")
    url: str = Field(..., description="Link to the full article")
    source: str = Field(..., description="The source of the news, e.g., TechCrunch, The Verge")

class DailyNewsCurated(BaseModel):
    date: str
    articles: List[NewsArticle]
    intro_message: str = Field("", description="A greeting or intro from the agent")
