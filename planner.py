from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_project_plan(feature_request):

    prompt = f"""
You are a senior technical project manager.

Convert the following feature request into a PROFESSIONAL project plan.

Feature Request:
{feature_request}

Generate the plan using clear markdown headings and bullet points.

The output MUST contain the following sections:

# 1. Project Overview
- Goal
- Key user value
- Short description of the feature

# 2. Key Milestones
List the major phases of the project.

Example:
- Requirements & Planning
- Design
- Development
- Testing
- Launch

# 3. Work Breakdown Structure (WBS)

For EACH milestone, create a detailed WBS.

Format example:

### Milestone: Design

Product
- Finalize product requirements
- Define success metrics

Design
- Create wireframes
- Create high-fidelity UI mockups
- Conduct usability review

Engineering
- Define architecture
- Define API contracts

QA
- Define testing strategy

Each milestone should contain multiple tasks.

# 4. Resource Requirements

Estimate the team needed to deliver this project.

Example format:

- Product Manager: 1
- UI/UX Designer: 1
- Frontend Engineers: 2
- Backend Engineers: 2
- QA Engineers: 1
- DevOps Engineer: 1

Explain briefly what each role will handle.

# 5. Dependencies

List external or internal dependencies.

Examples:
- Third-party APIs
- Payment gateway integration
- Data availability
- Infrastructure setup

# 6. Risks and Mitigation

Provide a list like:

Risk:
Mitigation:

# 7. Suggested Timeline

Provide milestone durations.

Example:

- Planning: 1 week
- Design: 2 weeks
- Development: 4 weeks
- Testing: 2 weeks
- Launch: 1 week

Make the output structured, readable, and suitable for a real project plan document.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
