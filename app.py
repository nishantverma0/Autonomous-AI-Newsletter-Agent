import streamlit as st
import traceback

from main import run_newsletter_agent


st.set_page_config(
    page_title="Autonomous AI Newsletter Agent",
    layout="wide"
)

st.title("🤖 Autonomous AI Newsletter Agent")

st.markdown("""
AI Agent that researches, summarizes,
reviews and generates newsletters autonomously.
""")


goal = st.text_area(
    "Enter Goal",
    value="""
Create a weekly newsletter
on latest AI agent news
and send it to subscribers.
""",
    height=150
)

human_mode = st.toggle(
    "Human-in-the-Loop Mode"
)


if st.button("Run Autonomous Agent"):

    try:

        with st.spinner(
            "Running autonomous workflow..."
        ):

            result = run_newsletter_agent(
                goal,
                human_mode
            )

        st.success(
            "Newsletter Generated Successfully!"
        )

        col1, col2 = st.columns(2)

        # LEFT SIDE
        with col1:

            st.subheader("🧠 Agent Logs")

            for log in result["logs"]:
                st.write(log)

            st.subheader("🪞 Critique")

            st.write(result["critique"])

        # RIGHT SIDE
        with col2:

            st.subheader(
                "📰 Newsletter Preview"
            )

            st.components.v1.html(
                result["final_newsletter"],
                height=800,
                scrolling=True
            )

        st.download_button(
            "Download HTML",
            result["final_newsletter"],
            file_name="newsletter.html"
        )

    except Exception as e:

        st.error("Agent Failed ❌")

        st.code(str(e))

        st.code(
            traceback.format_exc()
        )
