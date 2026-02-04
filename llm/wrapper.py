import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_llm(system_prompt: str, user_prompt: str, model="gpt-4o-mini", json_mode=True):
    """
    Generic wrapper for LLM calls. 
    Supports JSON mode for structured output.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"} if json_mode else None,
            temperature=0.0
        )
        content = response.choices[0].message.content
        if json_mode:
            return json.loads(content)
        return content
    except Exception as e:
        return {"error": str(e)}