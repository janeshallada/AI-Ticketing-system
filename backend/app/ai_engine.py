from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_ticket(text):
    prompt = f"""
Analyze the ticket and return STRICT JSON:

Ticket: {text}

{{
  "category": "",
  "summary": "",
  "severity": "",
  "resolution_type": "",
  "sentiment": "",
  "department": "",
  "confidence": "",
  "estimated_time": ""
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"error": content}
