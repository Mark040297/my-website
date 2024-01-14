import streamlit as st

# Sidebar with navigation
navigation = st.sidebar.radio("Navigation", ["Home", "Page 1", "Page 2"])

# Main content based on user selection
if navigation == "Home":
    st.title("Home Page")
    st.write("Welcome to the home page!")

elif navigation == "Page 1":
    st.title("Page 1")
    st.write("This is page 1 content.")

elif navigation == "Page 2":
    st.title("Page 2")
    st.write("This is page 2 content.")