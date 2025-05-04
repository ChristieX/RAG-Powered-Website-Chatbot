from scraper import scrape_website
from langchain_text_splitters import CharacterTextSplitter

def chunk_text(text, chunk_size=1000, chunk_overlap=100):
    text_splitter=CharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    chunks=text_splitter.create_documents(text)
    return chunks

texts = scrape_website("https://pypi.org/project/langchain/")
print("Scrapped text:")
scrap_text = chunk_text(texts) 





