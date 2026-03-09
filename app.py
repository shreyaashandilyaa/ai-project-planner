import streamlit as st
from planner import generate_project_plan

st.set_page_config(page_title="AI Project Planner", layout="wide")

st.title("AI Project Planner")
st.write("Convert feature requests into structured project plans.")

feature_request = st.text_area(
    "Paste your feature request or PRD",
    height=250
)

if st.button("Generate Project Plan"):

    if feature_request.strip() == "":
        st.warning("Please enter a feature request.")
    else:

        with st.spinner("Generating project plan..."):
            plan = generate_project_plan(feature_request)

        st.subheader("Generated Project Plan")
        st.markdown(plan)
