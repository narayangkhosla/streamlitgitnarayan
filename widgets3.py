import streamlit as st

st.title("User Registration Form")
with st.form("my_form"):
    user_input = st.text_input("Enter your username:", placeholder="Username")
    user_password = st.text_input(
        "Enter your password:", type="password", placeholder="Password"
    )
    # user_gender=st.text_input("Enter your gender:", placeholder="Male/Female")
    user_gender = st.radio("Select your gender:", ["Male", "Female"], index=0)
    user_pincode = st.text_input("Enter your pincode:", placeholder="Pincode")
    user_address = st.text_input(
        "Enter your correspondence address:", placeholder="Address"
    )
    options = ["B.Tech", "M.Tech", "Bca", "Mca", "BBA", "MBA"]
    user_courses = st.selectbox(
        "Select your course:", options, placeholder="Select Course"
    )
    submit_button = st.form_submit_button("Submit")
if (
    submit_button
    and user_input
    and user_password
    and user_pincode
    and user_address
    and user_courses
):
    st.success("Form submitted successfully!")
    st.write(f"Hello, {user_input}!")
    st.write(f"Your password is: {user_password}")
    st.write(f"Your gender is: {user_gender}")
    st.write(f"YOur pincode is: {user_pincode}")
    st.write(f"Your correspondence address is: {user_address}")
    st.write(f"You have selected the course: {user_courses}")

else:
    st.warning("Please fill out all fields before submitting.")
