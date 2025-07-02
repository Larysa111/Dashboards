import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "Stadt": ["Berlin", "München", "Hamburg", "Köln", "Frankfurt"],
    "Einwohner": [3_700_000, 1_500_000, 1_800_000, 1_100_000, 750_000]
})


fig = px.bar(df, x="Stadt", y="Einwohner")

selected_points = st.plotly_chart(fig, on_select="rerun")

# st.header(type(selected))

selected_points_indices = selected_points["selection"]["point_indices"]

if not selected_points_indices:
    st.write(
        "🔎 **Klicke** auf einen Balken im Diagramm, um "
        "Details anzuzeigen und den Rest der App dynamisch zu befüllen."
    )
else:
    selected_rows = df.iloc[selected_points_indices]
    st.dataframe(selected_rows, hide_index=True)