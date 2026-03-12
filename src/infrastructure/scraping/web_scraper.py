import requests
from bs4 import BeautifulSoup
from typing import List
from src.domain.interfaces.news_scraper import INewsScraper
from src.domain.entities.news import NewsArticle

class WebScraper(INewsScraper):
    def fetch_top_news(self, limit: int = 10) -> List[NewsArticle]:
        # Using Google News RSS feed for tech news
        url = "https://news.google.com/rss/search?q=technology+startups+AI&hl=en-US&gl=US&ceid=US:en"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, features="xml")
            
            articles = []
            items = soup.findAll("item")
            
            for item in items[:limit]:
                title = item.title.text if item.title else "No Title"
                link = item.link.text if item.link else "No Link"
                # Strip HTML from description if necessary
                description = item.description.text if item.description else "No Description"
                source = item.source.text if item.source else "Google News"
                
                # Removing heavy HTML tags from description using a secondary soup
                clean_desc = BeautifulSoup(description, "html.parser").get_text(strip=True)[:200]
                
                articles.append(NewsArticle(
                    title=title,
                    summary=clean_desc,
                    url=link,
                    source=source
                ))
                
            return articles
            
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch news: {e}")
            return []
