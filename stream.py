import streamlit as st

from app import *

st.write("hello world")

photoHTML = getMarsPhoto(1000)

st.image(photoHTML, width = 400)