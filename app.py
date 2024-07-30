import streamlit as st
from app_pages import about_us, submit_feedback


def main():

    st.set_page_config(page_title="GenAi Voice of Customer", layout="wide")

    # Define a container to hold both elements
    st.sidebar.markdown('<div class="container"><div class="genai">Gen AI</div><div class="voice">VoiceOf<span class="customer">Customer</span></div></div>', unsafe_allow_html=True)

    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    # Initialize session state dictionary
    if 'session_state' not in st.session_state:
        st.session_state['session_state'] = {}

    about_us_button = st.sidebar.button("About Us", key="button1", type="primary")
    if about_us_button:
        st.session_state['selected_page'] = "About Us"

    submit_feedback_button = st.sidebar.button("Submit Feedback", key="button2")
    if submit_feedback_button:
        st.session_state['selected_page'] = "Submit Feedback"

    # Render the selected page
    if 'selected_page' not in st.session_state:
        st.session_state['selected_page'] = "About Us"

    if st.session_state['selected_page'] == "About Us":
        about_us.render_about_us()
    elif st.session_state['selected_page'] == "Submit Feedback":
        submit_feedback.render_submit_feedback()

    with open('./static/style.css', 'r') as css_style:
        css = css_style.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
