import streamlit as st
import os
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent
from dotenv import load_dotenv

# Load env variables
load_dotenv()

st.set_page_config(page_title="AI Ops Assistant", page_icon="🤖")

st.title("🤖 AI Operations Assistant (Weather and Github API)")
st.markdown("Multi-agent system: **Planner** → **Executor** → **Verifier**")
st.markdown("Enter queries like 'Find weather in Delhi and search for React libraries on GitHub' or 'Get weather in Mumbai' etc.")

# Check API Key
if not os.getenv("OPENAI_API_KEY"):
    st.error("⚠️ OPENAI_API_KEY is missing in .env file.")
    st.stop()

# Input
user_query = st.text_input("Enter your task:", placeholder="e.g. Find weather in London and search for React libraries on GitHub")

if st.button("Run Agents"):
    if not user_query:
        st.warning("Please enter a task.")
    else:
        # 1. Planner Step
        st.subheader("1. 🧠 Planner Agent")
        with st.spinner("Generating plan..."):
            planner = PlannerAgent()
            plan = planner.create_plan(user_query)
            st.json(plan)
        
        if not plan:
            st.error("Failed to generate plan.")
            st.stop()

        # 2. Executor Step
        st.subheader("2. ⚙️ Executor Agent")
        with st.spinner("Executing tools..."):
            executor = ExecutorAgent()
            results, logs = executor.execute_plan(plan)
            st.write("Execution Logs:")
            st.json(logs)

        # 3. Verifier Step
        st.subheader("3. ✅ Verifier Agent")
        with st.spinner("Verifying and summarizing..."):
            verifier = VerifierAgent()
            final_response = verifier.verify_and_summarize(user_query, logs)
            st.success("Final Output:")
            st.markdown(final_response)