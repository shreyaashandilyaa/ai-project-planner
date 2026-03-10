from openai import OpenAI
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Read API key from either local .env or Streamlit Cloud secrets
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)


def generate_project_plan(feature_request):

    prompt = f"""
Create a COMPLETE software project plan for the following feature request.

Feature Request:
{feature_request}

Use the following structure EXACTLY.

# Project Overview

# Key Milestones

# Work Breakdown Structure (WBS)

For each milestone, break work into:

Product
Design
Engineering
QA

Include detailed tasks.

# Resource Requirements

List team roles and number of people required.

Example:
Product Manager: 1
UI/UX Designer: 1
Frontend Engineers: 2
Backend Engineers: 2
QA Engineer: 1
DevOps Engineer: 1

# Dependencies

# Risks and Mitigation

# Suggested Timeline
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content

