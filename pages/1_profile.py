import streamlit as st

st.title("📝 Profile Page")

# Initialize session state for user profile if not already set
if "name" not in st.session_state:
    st.session_state.name = "Enter Name"
if "email" not in st.session_state:
    st.session_state.email = ""
if "age" not in st.session_state:
    st.session_state.age = 18
   
# User Information Form
with st.form("profile_form"):
    name = st.text_input("Full Name", value=st.session_state.name)
    email = st.text_input("Email", value=st.session_state.email)
    age = st.number_input("Age", min_value=18, max_value=100, value=st.session_state.age)
    submit = st.form_submit_button("Save Changes")

if submit:
    st.session_state.name = name
    st.session_state.email = email
    st.session_state.age = age
    st.success(f"Profile updated! ✅\n\n**Name:** {name}\n**Email:** {email}\n**Age:** {age}")
