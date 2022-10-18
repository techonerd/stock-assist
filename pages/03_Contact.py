import streamlit as st


with st.form("my_form"):
    st.title("Contact us :email:")
    sender_name = st.text_input("Full Name", placeholder="Enter your name")
    sender_email = st.text_input("Email", placeholder="Enter your email")
    sender_message = st.text_area("Meessage", placeholder="Enter your message")
    if submitted := st.form_submit_button("Submit"):
        st.write("name", sender_name, "email", sender_email, "message", sender_message)

