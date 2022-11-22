import streamlit
import pandas
streamlit.title('My Parents Healthy New Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Blueberry Oats')
streamlit.text('🥬Kale Spinach Smoothis')
streamlit.text('Hard Boiled Free Range Eggs')
streamlit.text('Avocado Toast')
streamlit.header('Build your own fruit smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
