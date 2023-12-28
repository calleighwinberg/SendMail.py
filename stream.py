import streamlit as st

from marsEmail import *

st.write("hello world")

photoHTML = getMarsPhoto(1000)

#st.image(photoHTML, width = 400)

st.button("New Mars Photo", type="primary")

if st.button:
    st.image(photoHTML, width = 400)