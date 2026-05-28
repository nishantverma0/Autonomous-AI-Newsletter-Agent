from agent.graph import build_graph


def run_newsletter_agent(
    goal,
    human_mode=False
):

    app = build_graph()

    state = {
        "goal": goal,
        "articles": [],
        "summaries": [],
        "critique": "",
        "final_newsletter": "",
        "logs": []
    }

    result = app.invoke(state)

    return result
