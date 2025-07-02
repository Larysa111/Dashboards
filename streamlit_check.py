import sys
import streamlit as st

st.title("Проверка Python среды")
st.write("Python executable:")
st.code(sys.executable)

st.write("Python version:")
st.code(sys.version)

st.write("Site-packages directory:")
st.code('\n'.join(sys.path))