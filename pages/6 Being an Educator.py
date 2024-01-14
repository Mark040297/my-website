import streamlit as st

st.set_page_config(page_title="Being an Educator", layout='wide', page_icon="📚")

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
