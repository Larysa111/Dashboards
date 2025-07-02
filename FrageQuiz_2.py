import streamlit as st
import pandas as pd

st.title("🧪 CSV-Quiz mit Dateiupload")


with st.expander("ℹ️ Anleitung zur CSV-Datei anzeigen"):
    st.markdown("""
    Die CSV-Datei muss wie folgt aufgebaut sein:

    | frage | option0 | option1 | option2 | option3 | richtige_option |
    |-------|---------|---------|---------|---------|------------------|
    | Was ist 2 + 2? | 3 | 4 | 5 | 6 | 1 |

    - 'option0' bis 'option3' sind die vier Antwortmöglichkeiten.
    - 'richtige_option' gibt den Index der richtigen Antwort an (beginnend bei **0**).
    - Die Datei muss als '.csv' gespeichert sein (UTF-8 empfohlen).
    """)
    
    st.download_button(
        label="📥 Beispieldatei herunterladen",
        data=open("fragen.csv", "rb").read(),
        file_name="example_quiz.csv",
        mime="text/csv"
    )

upload = st.file_uploader("📁 Eigene CSV-Datei hochladen", type="csv")

if upload is not None:
    try:
        df = pd.read_csv(upload)
        st.success("CSV erfolgreich geladen!")
    except Exception as e:
        st.error(f"Fehler beim Einlesen der Datei: {e}")
        st.stop()
else:
    st.info("Es wurde keine CSV hochgeladen. Das Standard-Quiz wird verwendet.")
    df = pd.read_csv("fragen.csv")

antworten = {}
with st.form("quiz_form"):
    for i, row in df.iterrows():
        options = [row[f"Option{j}"] for j in range(4)]
        frage = row["Frage"]
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