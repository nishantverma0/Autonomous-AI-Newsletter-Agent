import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from agent.prompts import CRITIQUE_PROMPT

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2
)


def critique_newsletter(newsletter):

    prompt = f"""
    {CRITIQUE_PROMPT}

    NEWSLETTER:
    {newsletter}
    """

    response = llm.invoke(prompt)

    return response.content