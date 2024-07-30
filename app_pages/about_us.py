import base64
import os.path

import streamlit as st


def icons_read(icon_name):
    directory = "icons/"
    file_path = os.path.join(directory, icon_name)
    # Read the icon image files
    with open(file_path, "r") as f:
        icon = f.read()
    return icon


# Read the icon files using the function
icon1_data = icons_read("efficacy.png")
# icon2_data = icons_read("icon2.png")
# icon3_data = icons_read("icon3.png")
# icon4_data = icons_read("icon4.png")

# Encode the icon images as base64
icon1_base64 = base64.urlsafe_b64encode(icon1_data).decode("utf-8")
# icon2_base64 = base64.b64encode(icon2_data).decode("utf-8")
# icon3_base64 = base64.b64encode(icon3_data).decode("utf-8")
# icon4_base64 = base64.b64encode(icon4_data).decode("utf-8")

# Set the page configuration
def render_about_us():
    st.markdown("""
     <div class="header-container"><h1 class="header-title">GEN AI - Voice of Customer</h1></div>""", unsafe_allow_html=True)
    st.markdown("""
        <div style='border: 1px solid #ddd; padding: 10px;'>
            <div class="info-text">Welcome, how can I help you?</div>
            <p>Welcome to GENAI Voice of Customer, where we transform customer interactions into actionable insights and exceptional experiences using advanced generative AI.</p>
            <div class="info-text">What We Do</div>
            <div class="section-1">
               <div style="margin-right: 20px;">
                <div>Support Automation</div>
                <div>Our AI model offers immediate, accurate responses to customer inquiries, reducing response times and improving the overall support experience</div>
              </div>
               <div style="margin-right: 20px;">
                <div>Customer Feedback Analysis</div>
                <div>We collect and analyze feedback from multiple channels, identifying key trends, sentiments, and actionable insights to help businesses make informed decisions</div>
              </div>
            </div>
        </div>
        <div style='border: 1px solid #ddd; padding: 10px; border-left: none; border-right: none;'>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div style='border: 1px solid #ddd; padding: 20px; width: 100%; '>
            <h2>Why Choose GENAI?</h2>
            <div style="display: flex; justify-content: space-between;">
              <div style="margin-right: 20px;">
                <div><img src="data:image/png;base64,{icon1_base64}" alt="Icon 1" width="30" height="30"> Efficiency</div>
                <div>Automate and streamline your customer support operations, reducing costs and improving response times</div>
              </div>
              <div style="margin-right: 20px;">
                <div>Insight</div>
                <div>Gain deep, data-driven insights into customer behaviors, preferences, and pain points</div>
              </div>
              <div style="margin-right: 20px;">
                <div>Satisfaction</div>
                <div>Enhance customer satisfaction by delivering timely and effective support tailored to individual needs.</div>
              </div>
              <div style="margin-right: 20px;">
                <div>Innovation</div>
                <div>Stay ahead of the competition by leveraging cutting-edge AI technology to continually improve customer engagement</div>
              </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<h3>Contact Us</h3>', unsafe_allow_html=True)
    st.markdown(
        '<p>If you have any inquiries or would like to learn more about our services, please feel free to reach out to us:</p>',
        unsafe_allow_html=True)
    st.markdown('<ul><li>Email: info@genai.com</li><li>Phone: +1 123-456-7890</li></ul>', unsafe_allow_html=True)


