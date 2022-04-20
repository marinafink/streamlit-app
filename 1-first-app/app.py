# SETUP

import streamlit as st
import pandas as pd
import datetime


#-------------------
# CREATE DATA

# Simple dataframe
df = pd.DataFrame({
    'A': [1, 4, 3, 2],
    'B': [10, 20, 30, 40]
    })

#-------------------
# START OF APP

#-------------------
# HEADER

# Title of our app

st.title('Meine erste App')
# Add header
st.header('Mein header')
# Add a gif from https://giphy.com/
st.markdown("![alt text](https://media.giphy.com/media/Yw0ZpX6d3sQnxsjaQx/giphy.gif)")

st.title("Meine erste App")
# Add header
st.header("Mein Header")
# Add a gif from https://giphy.com/
#st.markdown("![Katze](https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif)")

#st.image('hdm-logo.jpg')
#>>>>>>> a70e5471c04b44eff4ca69dd654f091c702a28c8

#st.image('hdm-logo.jpg')
#-------------------
# BODY


#-------------------
# Show static DataFrame
st.dataframe(df)

#-------------------
# Bar chart
st.bar_chart(df)
#<<<<<<< HEAD

#-------------------
# SIDEBAR
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

#-------------------
# WIDGETS
age = st.sidebar.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

d = st.date_input(
    "When is your birthday?",
    datetime.date(2019, 7, 6))
st.write('Your Birthday is:',d)

#-------------------

# SIDEBAR

st.sidebar.radio(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

#-------------------

# WIDGET

age = st.sidebar.slider('How old are you?', 0, 130, 25)
st.sidebar.write("I'm ", age, 'years old')


d = st.sidebar.date_input(
     "When's your birthday",
     datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
#>>>>>>> a70e5471c04b44eff4ca69dd654f091c702a28c8
