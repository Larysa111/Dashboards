import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Klassifizierung von Lieblingsobst")

df = pd.DataFrame({
    "Obst": ["Apfel", "Banane", "Erdbeere", "Orange", "Traube"],
    "Stimmen": [8, 5, 6, 4, 3],
    "Farbe": ["Rot", "Gelb", "Rot", "Orange", "Violett"],
    "Vitamin C (mg)": [12, 9, 60, 50, 4],
    "Herkunft": ["Deutschland", "Ecuador", "Spanien", "Italien", "Griechenland"],
    "Icon": ["🍎", "🍌", "🍓", "🍊", "🍇"],
})

col1, col2 = st.columns([2,1])

fig = px.bar(
    df,
    x="Obst",
    y="Stimmen",
    hover_data = ["Farbe", "Vitamin C (mg)", "Herkunft"],
    title="Stimmen fur Lieblingsobst"
)

selected = col1.plotly_chart(fig, on_select="rerun")
indices = selected["selection"]["point_indices"]

with col2:
    if not indices:
        st.info("👉 Klicke auf eine Obstsorte im Diagramm, um mehr zu erfahren.")
    else:
        obst = df.iloc[indices[0]]
        st.subheader(f"Details zu {obst.Icon}{obst.Obst}")
        st.markdown(f"""
        - **Farbe**: {obst.Farbe}  
        - **Vitamin C**: {obst['Vitamin C (mg)']}  
        - **Typische Herkunft**: {obst.Herkunft}
        """)