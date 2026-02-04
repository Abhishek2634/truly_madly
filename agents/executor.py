from tools.weather_tool import get_weather
from tools.github_tool import search_repos

class ExecutorAgent:
    def __init__(self):
        self.tool_map = {
            "get_weather": get_weather,
            "search_repos": search_repos
        }

    def execute_plan(self, plan):
        results = {}
        logs = []

        for step in plan:
            tool_name = step.get("tool")
            args = step.get("arguments", {})
            step_id = step.get("step_id")

            if tool_name in self.tool_map:
                try:
                    if tool_name == "get_weather":
                        output = self.tool_map[tool_name](args.get("city"))
                    elif tool_name == "search_repos":
                        output = self.tool_map[tool_name](args.get("query"))
                    else:
                        output = "Unknown argument mapping"
                    
                    results[step_id] = output
                    logs.append({
                        "step": step_id, 
                        "tool": tool_name, 
                        "status": "success", 
                        "output": output
                    })
                except Exception as e:
                    logs.append({"step": step_id, "status": "error", "error": str(e)})
            else:
                logs.append({"step": step_id, "status": "error", "error": "Tool not found"})
        
        return results, logs