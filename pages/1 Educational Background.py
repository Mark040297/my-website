import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Educational Background", layout='wide', page_icon="👤")

VSU_diploma = " "
VSU_TOR = " "
VSU_ProofEnglish = " "
TUAT_diploma = " "
TUAT_TOR = " "
st.markdown("<hr style='border: 20px solid #292929;'>", unsafe_allow_html=True)
st.markdown("<h1 style='color: #030303; text-align: center'>Educational Background</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #030303'>School Attended</h2>", unsafe_allow_html=True)

with st.container(border=True):
    space1, col1, space2 = st.columns([5, 1, 5])
    with col1:
        st.image("images/VSU logo.png")
    st.markdown("<h3 style='color: #030303; text-align: center'>Visayas State University</h3>",
                unsafe_allow_html=True)
    st.divider()
    col2, col3 = st.columns(2)
    with col2:
        st.image("images/VSU1.png")
    with col3:
        st.markdown("<h4 style='color: #030303; text-align: center'>BS in Mechanical Engineering</h4>",
                    unsafe_allow_html=True)
        content = ("Completed the bachelors degree in 2020 being the Magna Cum Laude and Class Valedictorian. "
                   "The projects being delved were focused on automation, mechatronics, and robotics applied in "
                   "agriculture.")
        st.markdown(f"<p style='color: #030303' align='justify'>{content}</p>",
                    unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<p style='color: #030303' align='justify'>Links to my Credentials:</p>",
                        unsafe_allow_html=True)
            st.link_button("My Diploma", VSU_diploma)
            st.link_button("My Transcript", VSU_TOR)
            st.link_button("My English Certificate", VSU_ProofEnglish)

with st.container(border=True):
    space3, col1, space4 = st.columns([1, 0.5, 1])
    with col1:
        st.image("images/TUAT logo.png")
    st.markdown("<h3 style='color: #030303; text-align: center'>Tokyo University of Agriculture and Technology</h3>",
                unsafe_allow_html=True)
    st.divider()
    col2, col3 = st.columns(2)
    with col2:
        st.image("images/TUAT1.png")
    with col3:
        content1 = "Short-term Exchange Program in Science and Engineering"
        st.markdown(f"<h4 style='color: #030303; text-align: center'>{content1}</h4>",
                    unsafe_allow_html=True)
        content2 = ("This six-month foreign exchange program was held at Tokyo, Japan in 2018-2019. "
                    "I have the opportunity to interact and collaborate with foreign students and "
                    "to immerse in different Japanese technologies and researches.")
        st.markdown(f"<p style='color: #030303' align='justify'>{content2}</p>",
                    unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<p style='color: #030303' align='justify'>Links to my Credentials:</p>",
                        unsafe_allow_html=True)
            st.link_button("My Diploma", TUAT_diploma)
            st.link_button("My Transcript", TUAT_TOR)

st.markdown("<h2 style='color: #030303'>Awards</h2>", unsafe_allow_html=True)

with st.container(border=True):
    df = pd.read_csv("data_educ.csv", sep=";")  # the default value of sep is comma
    col4, col5 = st.columns(2)
    with col4:
        for index, row in df[:2].iterrows():
            st.image(f"images/{row['image']}", caption=row['photo credit'])
            st.markdown(f"<h4 style='color: #030303; text-align: center'>{row['award']}</h4>",
                        unsafe_allow_html=True)
            st.markdown(f"<p style='color: #030303' align='justify'>{row['description']}</p>",
                        unsafe_allow_html=True)
            st.link_button("Read more", row['link'])
    with col5:
        for index, row in df[2:].iterrows():
            st.image(f"images/{row['image']}", caption=row['photo credit'])
            st.markdown(f"<h4 style='color: #030303; text-align: center'>{row['award']}</h4>",
                        unsafe_allow_html=True)
            st.markdown(f"<p style='color: #030303' align='justify'>{row['description']}</p>",
                        unsafe_allow_html=True)
            st.link_button("Read more", row['link'])


# footer
st.container(height=100, border=False)
st.markdown("<hr style='border: 20px solid #292929;'>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #030303'>© All rights reserved 2024</p>", unsafe_allow_html=True)

col5, col6, spaceA, col7, col8, spaceB, col9, col10 = st.columns([0.25, 1, 0.5, 0.25, 1, 0.5, 0.25, 1])
with col5:
    st.image("images/icon1.png")
with col6:
    st.write("www.facebook.com/markanthony.arcayan")
with col7:
    st.image("images/icon2.png")
with col8:
    st.write("www.youtube.com/@youngarcchannel6333")
with col9:
    st.image("images/icon3.png")
with col10:
    st.write("mark112arcayan@gmail.com")
