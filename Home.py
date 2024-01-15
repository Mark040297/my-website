import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Credentials", layout='wide', page_icon="👤")

st.markdown("<hr style='border: 20px solid #292929;'>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.image("images/my_photo.png", channels="BGR")

with col2:
    my_CV = "[My Curriculum Vitae](https://drive.google.com/file/d/16lRKfZ9Z0zc8GEHZVpya9Qvu4Y2FYlwa/view?usp=sharing)"
    CV_link = "https://drive.google.com/file/d/16lRKfZ9Z0zc8GEHZVpya9Qvu4Y2FYlwa/view?usp=sharing"
    st.markdown("<h1 style='color: #030303'>Mark Anthony S. Arcayan</h1>", unsafe_allow_html=True)
    content1 = """
        Hi, I'm Mark Anthony S. Arcayan! As a registered mechanical engineer and dedicated instructor,
        I possess expertise in computer programming, mechatronics, and robotics. I am passionate about designing 
        innovative solutions to address real-life problems, combining technical proficiency with a 
        commitment to practical applications.
    """
    content2 = """
        Curious to learn more about me in a short span of time? 
        Please feel free to explore my CV by following the link below. 
    """
    st.markdown(
        f"""
        <div style='color: #030303' align='justify'>
            <p>{content1}</p>
        </div>
        """, unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(
            f"""
                <div style='color: #030303 ' font-style='italic' align='justify'>
                    <p>{content2}</p>
                </div>
                """, unsafe_allow_html=True)
        st.link_button("My Curriculum Vitae", CV_link)

st.markdown("<hr style='border: 1px solid #292929;'>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("<h3 style='text-align: center; color: #030303'>My related projects to the IFROS</h3>",
                unsafe_allow_html=True)
    video_link2 = "https://youtu.be/d4LtE8lvCkk"
    st.video(data=video_link2, format="video/mp4", start_time=0)
with st.container(border=True):
    st.markdown("<h3 style='text-align: center; color: #030303'>Why I want to join IFROS?</h3>", unsafe_allow_html=True)
    video_link1 = "https://youtu.be/igLgakcYkQo"
    st.video(data=video_link1, format="video/mp4", start_time=0)

st.markdown("<hr style='border: 1px solid #292929;'>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #030303'>Contents</h1>", unsafe_allow_html=True)

df = pd.read_csv("data_Home.csv", sep=";")  # the default value of sep is comma

for index, row in df.iterrows():
    with st.container(border=True):
        col3, col4 = st.columns(2)
        with col3:
            st.image(f"images/{row['image']}", caption=row['image source'])
        with col4:
            st.markdown(
                f"""
                <div style="padding: 20px; background-color: #dbdbdb; border-radius: 10px;">
                    <h3>{row['title']}</h3>
                    <p>{row['description']}</p>                    
                </div>
                """,
                unsafe_allow_html=True
            )
        st.write(" ")

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

col5, col6, space1, col7, col8, space2, col9, col10 = st.columns([0.25, 1, 0.5, 0.25, 1, 0.5, 0.25, 1])
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
