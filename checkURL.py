import streamlit as st
import re
import requests
from langchain_community.document_loaders import WebBaseLoader

st.title("Web Loader")
url = st.text_input("Enter a URL:", "")
if st.button("Load!"):
    if url:
        session = requests.Session()
        st.write(f"Loading from web URL {url}")
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
    else:
        st.warning("Please enter a valid URL.")