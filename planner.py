from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_project_plan(feature_request):

    prompt = f"""
You are an experienced technical project manager.

Convert the following feature request into a structured and detailed project plan.

Feature Request:
{feature_request}

Create the following sections:

1. Project Overview
   - Goal
   - Key user value
   - High-level feature description

2. Key Milestones
   Identify the major phases of the project.

3. Work Breakdown Structure (WBS)
   Break each milestone into detailed tasks.

   Organize tasks under categories:
   - Product
   - Design
   - Engineering
   - QA

   Ensure tasks are actionable and realistic.

4. Resource Requirements
   List the required team roles and how many people are needed.

   Example:
   - Product Manager (1)
   - Frontend Engineers (2)
   - Backend Engineers (2)
   - UI/UX Designer (1)
   - QA Engineer (1)
   - DevOps Engineer (1)

5. Dependencies
   Mention external systems, integrations, approvals, or infrastructure required.

6. Risks
   List key project risks and mitigation strategies.

7. Suggested Timeline
   Estimate duration for each milestone.

Format the output clearly using headings and bullet points so it reads like a professional project plan.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
