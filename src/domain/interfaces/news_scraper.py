from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.news import NewsArticle

class INewsScraper(ABC):
    @abstractmethod
    def fetch_top_news(self, limit: int = 10) -> List[NewsArticle]:
        """Fetches the top tech news articles."""
        pass
