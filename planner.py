from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_project_plan(feature_request):

    prompt = f"""
You are an experienced technical project manager.

Convert the following feature request into a structured project plan.

Feature Request:
{feature_request}

Create:

1. Project Overview
2. Key Milestones
3. Task Breakdown (Product, Engineering, Design)
4. Dependencies
5. Risks
6. Suggested Timeline

Keep it structured and easy to read.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content
