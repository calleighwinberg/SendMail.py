import datetime

import streamlit as st

from mars_email import *

st.set_page_config(layout="wide")

st.title("Exploring Space")

with st.sidebar:
    st.title('NASA\'s Astronomy Picture of the Day')
    st.write('One of the most popular websites at NASA is the Astronomy Picture of the Day. In fact, this website is '
             'one of the most popular websites across all federal agencies. On June 16, 1995, two gamma-ray astronomers '
             'at NASA\'s Goddard Space Flight Center launched a website with a simple aim – to post a daily astronomical'
             ' image to raise awareness of astronomy and space science.')


    date = st.date_input('Select a Date', value=datetime.date(2023, 12, 12), min_value=datetime.date(1995, 6, 16),
                         max_value=datetime.datetime.now(), format="YYYY-MM-DD", label_visibility='visible')

    st.title('Interested in exploring closer to home?')
    st.write('Send an email to "mars@calleighwinberg.courses" to receive back a random photo from NASA\'s Mars Curiosity '
             'Rover. Include a \'sol\' date (0-4000) in the body of your email to receive a photo taken on the specific Martian '
             'sol counting from when Curiosity landed.')


with st.container():
    try:
        lst = get_photo_of_day(date)
        st.subheader(lst[1] + " - " + str(date), divider='blue')

        if lst[3] == 'image':
            st.image(lst[0], width=None, use_column_width='always')
        else:
            st.video(lst[0])

        st.write(lst[2])
    except:
        st.write("oh no! There's no picture for the day selected!")
