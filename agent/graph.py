from langgraph.graph import StateGraph, END

from agent.state import AgentState

from agent.nodes import (
    planner_node,
    research_node,
    summarize_node,
    review_node,
    generate_node
)


def build_graph():

    workflow = StateGraph(AgentState)

    workflow.add_node(
        "planner",
        planner_node
    )

    workflow.add_node(
        "research",
        research_node
    )

    workflow.add_node(
        "summarize",
        summarize_node
    )

    workflow.add_node(
        "review",
        review_node
    )

    workflow.add_node(
        "generate",
        generate_node
    )

    workflow.set_entry_point("planner")

    workflow.add_edge(
        "planner",
        "research"
    )

    workflow.add_edge(
        "research",
        "summarize"
    )

    workflow.add_edge(
        "summarize",
        "review"
    )

    workflow.add_edge(
        "review",
        "generate"
    )

    workflow.add_edge(
        "generate",
        END
    )

    return workflow.compile()
