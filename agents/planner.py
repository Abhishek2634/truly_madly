from llm.wrapper import query_llm

PLANNER_SYSTEM_PROMPT = """
You are the Planner Agent. Your job is to break down a user request into a sequence of tool calls.
Available Tools:
1. get_weather(city: str) - Get current weather.
2. search_repos(query: str) - Search GitHub repositories.

Return a JSON object with a "plan" key containing a list of steps.
Each step must have:
- "step_id": integer
- "tool": "get_weather" or "search_repos"
- "arguments": object containing the arguments (e.g., {"city": "Delhi"})
- "description": Brief explanation of the step.
"""

class PlannerAgent:
    def create_plan(self, user_input):
        response = query_llm(PLANNER_SYSTEM_PROMPT, f"Task: {user_input}")
        return response.get("plan", [])