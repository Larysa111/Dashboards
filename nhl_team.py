import streamlit as st
import pandas as pd
df = pd.read_csv("teams.csv")


team_names = sorted(df["Team"].unique())
selected_teams = st.sidebar.multiselect(
    "Wähle Teamnamen",
    options=team_names,
    default=team_names  
)

df_filtered = df[df["Team"].isin(selected_teams)]


year_min = int(df["Jahr"].min())
year_max = int(df["Jahr"].max())
year_range = st.sidebar.slider(
    "Wähle Jahresbereich",
    min_value=year_min,
    max_value=year_max,
    value=(year_min, year_max)
)

df_filtered = df[
    (df["Team"].isin(selected_teams)) &
    (df["Jahr"].between(year_range[0], year_range[1]))
]
