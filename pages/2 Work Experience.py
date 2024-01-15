import streamlit as st

st.set_page_config(page_title="My Work Experience", layout='wide', page_icon="👤")

Cert_Employment = " "
Cert_OJT = " "
OJT_manuscript = " "

st.markdown("<hr style='border: 20px solid #292929;'>", unsafe_allow_html=True)
st.markdown("<h1 style='color: #030303; text-align: center'>Work Experience</h1>", unsafe_allow_html=True)

with st.container(border=True):
    space1, col1, space2 = st.columns([5, 1, 5])
    with col1:
        st.image("images/VSU logo.png")
    st.markdown("<h3 style='color: #030303; text-align: center'>Visayas State University</h3>",
                unsafe_allow_html=True)
    st.divider()
    col2, col3 = st.columns(2)
    with col2:
        st.image("images/w1.png")
    with col3:
        st.markdown("<h4 style='color: #030303; text-align: center'>Instructor (2020 - present)</h4>",
                    unsafe_allow_html=True)
        content = ("Conducts research, instruction, and extension activities related to the "
                   "field of mechanical engineering at Visayas State University, Visca, Baybay City, "
                   "Leyte, Philippines 6541.")
        st.markdown(f"<p style='color: #030303' align='justify'>{content}</p>",
                    unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<p style='color: #030303' align='justify'>Link to my Credential:</p>",
                        unsafe_allow_html=True)
            st.link_button("My Certificate of Employment", Cert_Employment)

with st.container(border=True):
    space3, col1, space4 = st.columns([0.5, 3, 0.5])
    with col1:
        st.markdown("<h3 style='color: #030303; text-align: center'>Tsuneishi Heavy Industries (Cebu) Inc.</h3>",
                    unsafe_allow_html=True)
    st.divider()
    col2, col3 = st.columns(2)
    with col2:
        st.image("images/w2.png")
    with col3:
        content1 = "On-the-job Training Intern (2018)"
        st.markdown(f"<h4 style='color: #030303; text-align: center'>{content1}</h4>",
                    unsafe_allow_html=True)
        content2 = ("Immersed in ship hull repairs, ship docking, engine overhauling, propeller inspection, "
                    " and quality control. This internship took place at West Cebu Industrial Park-SEZ, Buanoy,"
                    " Balamban, Cebu, Philippines 6041.")
        st.markdown(f"<p style='color: #030303' align='justify'>{content2}</p>",
                    unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<p style='color: #030303' align='justify'>Links to my Credentials:</p>",
                        unsafe_allow_html=True)
            st.link_button("My Certificate of Internship", Cert_OJT)
            st.link_button("My Internship Manuscript", OJT_manuscript)

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
