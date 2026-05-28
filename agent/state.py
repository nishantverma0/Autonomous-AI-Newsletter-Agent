from typing import TypedDict, List


class AgentState(TypedDict):
    goal: str
    articles: List
    summaries: List
    critique: str
    final_newsletter: str
    logs: List[str]
