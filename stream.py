import datetime

import streamlit as st

from marsEmail import *

st.set_page_config(layout="wide")

st.title("Exploring Space")

with st.sidebar:
    st.title('NASA\'s Astronomy Picture of the Day')
    st.write('One of the most popular websites at NASA is the Astronomy Picture of the Day. In fact, this website is '
             'one of the most popular websites across all federal agencies. On June 16, 1995, two gamma-ray astronomers '
             'at NASA\'s Goddard Space Flight Center launched a website with a simple aim – to post a daily astronomical'
             ' image to raise awareness of astronomy and space science.')

    #today = datetime.datetime.now()

    date = st.date_input('Select a Date', value=datetime.date(2023, 12, 12), min_value=datetime.date(1995, 6, 16),
                         max_value=datetime.datetime.now(), format="YYYY-MM-DD", label_visibility='visible')

    st.title('Interested in exploring closer to home?')
    st.write('Send an email to "mars@calleighwinberg.courses" to receive back a random photo from NASA\'s Mars Curiosity '
             'Rover. Include a \'sol\' date (0-4000) in the body of your email to receive a photo taken on the specifc Martian '
             'sol after Curiosity landed.')

with st.container():
    #date = st.date_input('Select a Date', value=datetime.date(2023, 12, 12), min_value=datetime.date(1995, 6, 16),
                         #max_value=None, format="YYYY-MM-DD", label_visibility='visible')

    try:
        apodHTTP, title, explanation = getPhotoOfDay(date)
        st.subheader(title + " - " + str(date), divider='blue')
        # st.write(date)

        # col1, col2 = st.columns(2, gap='small')

        # with col1:
        st.image(apodHTTP, width=None, use_column_width='always')

        # with col2:
        st.write(explanation)
    except:
        st.write("oh no! There's no picture for the day selected!")




photoHTML = getMarsPhoto(1000)

#st.image(photoHTML, width = 400)

st.button("New Mars Photo", type="primary")

if st.button:
    st.image(photoHTML, width = 400)