import streamlit as st
# import sys
import os

"""
# Welcome to Streamlit v38!!!!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""
st.title("Test App 55577")

value = st.slider("Pick a number", 0, 10, 3)
st.write(os.getcwd())

f = open("text", "a")
f.write("something")
f.close()
#os.system("echo test >> text")

# st.write(value)
# sys.stdout.write(str(value) + "\n")
# sys.stdout.flush()
