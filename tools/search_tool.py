from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_ai_news(query="latest AI agent news", max_results=7):

    response = client.search(
        query=query,
        max_results=max_results
    )

    return response["results"]

