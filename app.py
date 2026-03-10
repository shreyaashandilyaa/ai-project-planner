import streamlit as st
from planner import generate_project_plan

st.set_page_config(page_title="AI Project Planner", layout="wide")

st.title("AI Project Planner")
st.write("Convert feature requests into structured project plans.")

# Initialize history
if "history" not in st.session_state:
    st.session_state.history = []

feature_request = st.text_area(
    "Paste your feature request or PRD",
    height=250
)

generate = st.button("Generate Project Plan")

if generate:

    if feature_request.strip() == "":
        st.warning("Please enter a feature request.")
    else:

        with st.spinner("Generating project plan..."):
            plan = generate_project_plan(feature_request)

        # Save to history
        st.session_state.history.insert(0, {
            "request": feature_request,
            "plan": plan
        })

        st.subheader("Generated Project Plan")

        st.markdown(plan)

        # Download buttons
        st.download_button(
            label="Download Plan (Markdown)",
            data=plan,
            file_name="project_plan.md",
            mime="text/markdown"
        )

        st.download_button(
            label="Download Plan (Text)",
            data=plan,
            file_name="project_plan.txt",
            mime="text/plain"
        )

# Show history
if st.session_state.history:

    st.divider()
    st.header("Generated Plan History")

    for i, item in enumerate(st.session_state.history):

        with st.expander(f"Plan {i+1}"):

            st.markdown("### Feature Request")
            st.write(item["request"])

            st.markdown("### Project Plan")
            st.markdown(item["plan"])

            st.download_button(
                label="Download This Plan",
                data=item["plan"],
                file_name=f"project_plan_{i+1}.md",
                mime="text/markdown",
                key=f"download_{i}"
            )
