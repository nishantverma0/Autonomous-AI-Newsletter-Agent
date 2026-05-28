import os

from tools.search_tool import search_ai_news
from tools.summarize_tool import summarize_article
from tools.review_tool import critique_newsletter
from tools.html_generator import generate_html


def planner_node(state):

    state["logs"].append(
        "🧠 Planning newsletter workflow..."
    )

    return state


def research_node(state):

    state["logs"].append(
        "🔍 Researching latest AI news..."
    )

    articles = search_ai_news()

    state["articles"] = articles

    return state


def summarize_node(state):

    state["logs"].append(
        "✍️ Summarizing articles..."
    )

    summaries = []

    for article in state["articles"]:

        title = article.get("title", "No Title")

        url = article.get("url", "")

        content = article.get("content")

        if not content:
            content = article.get("snippet", "")

        if not content:
            content = title

        try:

            summary = summarize_article(content)

        except Exception as e:

            summary = f"""
            Summary generation failed.

            Error:
            {str(e)}
            """

        summaries.append({
            "title": title,
            "url": url,
            "summary": summary
        })

    state["summaries"] = summaries

    state["logs"].append(
        f"✅ Generated {len(summaries)} summaries"
    )

    return state



def review_node(state):

    state["logs"].append(
        "🪞 Reviewing newsletter quality..."
    )

    combined_text = ""

    for s in state["summaries"]:
        combined_text += s["summary"]

    critique = critique_newsletter(
        combined_text
    )

    state["critique"] = critique

    state["logs"].append(
        "✅ Review Completed"
    )

    return state


def generate_node(state):

    state["logs"].append(
        "📰 Generating newsletter..."
    )

    if not state["summaries"]:

        state["final_newsletter"] = """
        <h1>No summaries generated.</h1>
        """

        return state

    html = generate_html(
        state["summaries"]
    )

    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/newsletter.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    markdown = "# Weekly AI Newsletter\n\n"

    for s in state["summaries"]:

        markdown += f"""
## {s['title']}

{s['summary']}

Read More:
{s['url']}

---
"""

    with open(
        "outputs/newsletter.md",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(markdown)

    state["final_newsletter"] = html

    state["logs"].append(
        "✅ Newsletter generated successfully"
    )

    return state
