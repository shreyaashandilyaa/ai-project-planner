from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_project_plan(feature_request):

    prompt = f"""
You are a senior technical project manager.

Create a COMPLETE project plan from the following feature request.

Feature Request:
{feature_request}

The response MUST contain ALL of the following sections.

Use clear markdown headers exactly as written.

---

# Project Overview
Explain the goal of the feature and the value to users.

---

# Key Milestones
List the major phases of the project.

Example:
- Planning
- Design
- Development
- Testing
- Launch

---

# Work Breakdown Structure (WBS)

For EACH milestone, break the work into detailed tasks.

Format example:

### Milestone: Design

Product
- Define requirements
- Finalize PRD

Design
- Create wireframes
- Create high-fidelity UI
- Conduct usability review

Engineering
- Define architecture
- Define APIs

QA
- Define test strategy

Repeat this structure for multiple milestones.

---

# Resource Requirements

List the team needed and how many of each role.

Example format:

- Product Manager: 1
- UI/UX Designer: 1
- Frontend Engineers: 2
- Backend Engineers: 2
- QA Engineer: 1
- DevOps Engineer: 1

Explain briefly what each role will do.

---

# Dependencies

List external dependencies such as:
- APIs
- Data sources
- Integrations
- Infrastructure

---

# Risks and Mitigation

List major risks and how they will be mitigated.

---

# Suggested Timeline

Provide estimated duration for each milestone.

Example:

- Planning: 1 week
- Design: 2 weeks
- Development: 4 weeks
- Testing: 2 weeks
- Launch: 1 week

---

IMPORTANT:
Do NOT skip any section.
Ensure the sections "Work Breakdown Structure (WBS)" and "Resource Requirements" are always included.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
