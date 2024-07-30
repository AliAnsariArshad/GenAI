import streamlit as st
from openai_logic.response_generator import generate_response
from openai_logic.voc import process_feedback


def render_submit_feedback():
    st.markdown('<div class="header-container"><h1 class="header-title">GEN AI - Voice of Customer</h1></div>',
                unsafe_allow_html=True)
    st.markdown('<div class="info-text">Welcome to the Feedback page!</div>', unsafe_allow_html=True)

    form = st.form("feedback_form")
    feedback = form.text_area("Enter your feedback here:")
    submit_btn = form.form_submit_button("Submit Feedback")

    product = ""
    department = ""
    # Submit button
    if submit_btn and feedback:
        # Process the feedback here (e.g., store it in a database, send it via email, etc.)
        if isinstance(process_feedback(feedback), tuple):
            response, product, department = process_feedback(feedback)
        else:
            response = process_feedback(feedback)

        if isinstance(response, dict):
            st.markdown(f"<div class='response-container'>Suggested solution:\n\n"
                        f"{response['Suggested solution']}</div>",
                        unsafe_allow_html=True)

            with st.form(key='my_form'):
                selected_option = st.radio("Did this solution resolve your issue?", ("Yes", "No"), index=None)
                submit_button = st.form_submit_button(label='Submit')

                if submit_button:
                    if selected_option == "Yes":
                        st.markdown(
                            f"<div class='response-container'>{generate_response('Positive', product, department)}</div>",
                            unsafe_allow_html=True)

            # if selected_option is not None:
            #     st.write("You selected:", selected_option)
            # options = None
            # while options is None:
            #     options = st.radio("Did this solution resolve your issue?", ("Yes", "No"), index=None)

            # if selected_option == "Yes":
            #     st.markdown(f"<div class='response-container'>{generate_response('Positive', product, department)}</div>", unsafe_allow_html=True)
        else:
            st.success("Thank you for your feedback!")
            st.markdown(f"<div class='response-container'>{response}</div>", unsafe_allow_html=True)
    elif submit_btn:
        st.warning("Please enter your feedback before submitting.")
