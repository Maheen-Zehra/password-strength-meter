# Project 02: Password Strength Meter

# 🔹 Requirements
# 1. Password Strength Criteria
# A strong password should:
# ✅ Be at least 8 characters long
# ✅ Contain uppercase & lowercase letters
# ✅ Include at least one digit (0-9)
# ✅ Have one special character (!@#$%^&*)

# 2. Scoring System
# Weak (Score: 1-2) → Short, missing key elements
# Moderate (Score: 3-4) → Good but missing some security features
# Strong (Score: 5) → Meets all criteria
# 3. Feedback System
# If the password is weak, suggest improvements.
# If the password is strong, display a success message.

import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker By Maheen Zehra", page_icon="🔑", layout="centered")

#custom css
st.markdown("""
<style>
    .main {text-align: center; }
    .stTextInput {width: 60% !important; margin: auto; text-align: center;}
    .stButton button {width: 50%; background-color: #cacfd2; color: black; font-size: 18px;  display: block; margin: 0 auto; }
    .stButton button:hover { background-color: #145a32; color: white;}
            </style>
            """,unsafe_allow_html=True)

#page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter your password below to check its security level.🔍")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌ Password should be **at least 8 character long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1 
    else:
        feedback.append("❌ Password should include **both upper case (A-Z) and lower case (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌Password should include **at least one number (0-9)**.")

    #special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌Include **at least one special character (!@#$%^&*)**.")
    
    #display password strength results
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3 :
        st.info("⚠️**Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌**Week Password** - Follow the suggestion below to strength it.")

    #feedback
    if feedback:
        with st.expander("🔍**Improcve your password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐.")

#Button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")#show warning if password is empty

