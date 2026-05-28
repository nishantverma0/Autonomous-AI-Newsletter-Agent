import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from agent.prompts import SUMMARY_PROMPT

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3
)


def summarize_article(content):

    prompt = f"""
    {SUMMARY_PROMPT}

    ARTICLE:
    {content}
    """

    response = llm.invoke(prompt)

    return response.content