import streamlit as st
import pandas as pd


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


st.title("My Brothers New Healthy Dinner")

st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)


st.header("Fruityvice Fruit Advice!")
import requests


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
st.text(fruityvice_response)


# take the json version of the response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it as a table
st.dataframe(fruityvice_normalized)
