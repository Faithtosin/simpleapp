import streamlit as st
# import sys
import os

"""
# Welcome to Streamlit v19!!!! :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""
st.title("Test App 55577")

value_1 = st.slider("Pick a number", 0, 10, 3)
value_2 = st.slider("Pick a number", 30, 100, 32)
addition = value_1 + value_2
st.write(os.getcwd())
st.write("The sum of your numbers is", addition)

#os.system("echo test >> text")

# st.write(value)
# sys.stdout.write(str(value) + "\n")
# sys.stdout.flush()
