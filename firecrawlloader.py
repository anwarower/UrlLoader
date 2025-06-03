# Install with pip install firecrawl-py
import asyncio
from firecrawl import AsyncFirecrawlApp
import os 

class Firecrawl:
    def __init__(self):
        self.app = AsyncFirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    async def scrape_url(self, url):
        response = await self.app.scrape_url(
            url=url,    
            formats= [ 'markdown' ],
            only_main_content= True
        )
        return response

