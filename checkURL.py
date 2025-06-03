import streamlit as st
import re
import os 
import requests
from dotenv import load_dotenv
load_dotenv()
from spidercrawl import SpiderCrawl
from firecrawlloader import Firecrawl
from langchain_community.document_loaders import WebBaseLoader
import asyncio
def load_web_base_url(url):
    try:
        loader = WebBaseLoader(url, session=session)
        web_doc_list = loader.load()

        for doc in web_doc_list:
            st.write(f"Loading document from {doc.metadata.get('source')}")
            tmp = doc.page_content.replace('\n', ' ')
            doc.page_content = re.sub(r'[‘”’“]', '', tmp)
            st.write("Processed content:")
            st.write(doc.page_content)  
    except Exception as e:
        st.error(f"Error processing web page '{url}': {e}")

def load_spider_url(url):
    spider = SpiderCrawl()
    json_response = spider.crawl(url)
    st.write(json_response)

def load_firecrawl_url(url):
    firecrawl = Firecrawl()
    response = asyncio.run(firecrawl.scrape_url(url))
    st.write(response)

url = st.text_input("Enter a URL:", "")
chosen_option = st.radio("Load from web or spider?", ("Web", "Spider", "Firecrawl"))
if st.button("Load!"):
    if url:
        session = requests.Session()
        st.write(f"Loading from web URL {url}")
        if(chosen_option == "Web"):
            load_web_base_url(url)
        elif(chosen_option == "Spider"):
            load_spider_url(url)
        elif(chosen_option == "Firecrawl"):
            load_firecrawl_url(url)
    else:
        st.warning("Please enter a valid URL.")