from llm.wrapper import query_llm

VERIFIER_SYSTEM_PROMPT = """
You are the Verifier Agent. 
Your job is to take the "Tool Execution Logs" and generate a beautiful, human-readable response for the user.

Rules:
1. Return a JSON object with a single key: "final_response".
2. The value of "final_response" MUST be a string formatted in Markdown.
3. Use Bullet points, **Bold** text, and Headers (###) to organize the information.
4. Do NOT simply dump the raw JSON data. Summarize it naturally.
5. If the weather is provided, state the city, temperature, and wind speed clearly.
6. If GitHub repos are provided, list them with their star counts and links.

Example Output JSON:
{
  "final_response": "### 🌤️ Weather in Mumbai\n- **Temperature:** 28°C\n- **Wind:** 10 km/h\n\n### 🐙 Top GitHub Repos\n1. **LangChain** (⭐ 80k) - [Link](...)\n   *Framework for LLMs.*"
}
"""

class VerifierAgent:
    def verify_and_summarize(self, user_task, execution_logs):
        prompt = f"""
        User Task: {user_task}
        Tool Execution Logs: {execution_logs}
        """
        response = query_llm(VERIFIER_SYSTEM_PROMPT, prompt)
        return response.get("final_response", "Error generating summary.")