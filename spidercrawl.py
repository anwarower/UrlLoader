import os
import requests

class SpiderCrawl:
    def __init__(self):
        self.api_key = os.getenv("SPIDER_API_KEY")
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }

    def crawl(self, url, limit=5, return_format="markdown"):
        json_data = {"limit":limit,"return_format":return_format,"url":url}

        response = requests.post('https://api.spider.cloud/crawl', 
        headers=self.headers, json=json_data)
        return response.json()

    

