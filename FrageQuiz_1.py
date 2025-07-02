import streamlit as st
import pandas as pd

df = pd.read_csv("fragen.csv")

st.title("🧪 CSV-Quiz")
antworten = {}
with st.form("quiz_form"):
    for i, row in df.iterrows():
        frage = row["Frage"]
        options = [row[f"Option{j}"] for j in range(4)]  

        antwort = st.radio(f"{i+1}. {frage}", options, key=i)
        antworten[i] = antwort

    submitted = st.form_submit_button("Quiz abschicken")

if submitted:
    st.subheader("🔍 Auswertung")
    punkte = 0

    for i, row in df.iterrows():
        options = [row[f"Option{j}"] for j in range(4)]
        richtige_antwort = options[int(row["richtige_option"])]
        nutzer_antwort = antworten[i]

        if nutzer_antwort == richtige_antwort:
            st.success(f"✅ {i+1}. {row['Frage']}")
            punkte += 1
        else:
            st.error(f"❌ {i+1}. {row['Frage']}")
            st.markdown(f"Richtige Antwort: **{richtige_antwort}**")

    st.metric("Dein Ergebnis", f"{punkte}/{len(df)}")
    if punkte == len(df):
        st.balloons()