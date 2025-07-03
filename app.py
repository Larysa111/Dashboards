# import streamlit as st

# if "counter" not in st.session_state:
#     st.session_state.counter=0

# if st.button("Klick mich"):
#     st.session_state.counter+=1

# st.metric("Button geklickt", value=st.session_state.counter)

# if st.session_state.counter == 5:
#     st.balloons()
   
# print(st.session_state)

# import streamlit as st

# st.write("something I want to see in my app")
# if "step" not in st.session_state:
#     st.session_state.step = 1
    
# if "info" not in st.session_state:
#     st.session_state.info = {}
    
# def go_to_step2(name):
#     st.session_state.info["name"] = name
#     st.session_state.step = 2
    
# def go_to_step1():
#     st.session_state.step = 1

# if st.session_state.step == 1:
#     st.header("Part 1: Info")
#     name = st.text_input("Name", value=st.session_state.info.get("name", ""))
#     st.button("Next", on_click=go_to_step2, args=(name,))

 
# elif st.session_state.step == 2:
#     st.header("Part 2: Review")
#     st.subheader("Please review this:")
#     st.write(f"**Name**: {st.session_state.info.get('name', '')}")
    
#     if st.button("Submit"):
#         st.success("Great!")
#         st.balloons()
#         st.session_state.info = {}
#         st.button("Back", on_click=go_to_step1)

# import streamlit as st
# import pandas as pd

# DATA = pd.DataFrame({
#     "Stadt": ["Berlin", "München", "Hamburg", "Köln", "Frankfurt", "Stuttgart", "Dresden"],
#     "Einwohner": [3_700_000, 1_500_000, 1_800_000, 1_100_000, 750_000, 600_000, 550_000]
# })

# if "filtered" not in st.session_state:
#     st.session_state.filtered = DATA.copy()

# def filter_cities():
#     term = st.session_state.search_term.strip().lower()
#     if term:
#         st.session_state.filtered = DATA[DATA["Stadt"].str.lower().str.contains(term)]
#     else:
#         st.session_state.filtered = DATA.copy()

# st.title("City-Filter")

# st.text_input(
#     label="Stadt suchen",
#     key="search_term",
#     on_change=filter_cities
# )

# st.write("### Gefundene Städte")
# st.dataframe(st.session_state.filtered, use_container_width=True)

# import streamlit as st

# if "checkbox" not in st.session_state:
#     st.session_state.checkbox = False

# def toggle_input():
#     st.session_state.checkbox = not st.session_state.checkbox
#     if not st.session_state.checkbox:
#         st.session_state.user_input = ""

# st.checkbox("Show Input Field", value=st.session_state.checkbox, on_change=toggle_input)

# if st.session_state.checkbox:
#     user_input = st.text_input("Enter something:")
#     st.session_state.user_input = user_input
# else:
#     user_input = st.session_state.get("user_input", "")

# st.write(f"User Input: {user_input}")

import streamlit as st
import time

@st.cache_data(ttl=60) # Cache diese Daten für 60 Sekunden
def fetch_data():
    # Langsame Datenabfrage simulieren:
    time.sleep(3)
    return {"data": "This is cached data!"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)