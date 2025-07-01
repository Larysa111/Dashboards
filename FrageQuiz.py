import pandas as pd
import streamlit as st

data = [
    ["Welches Element hat das chemische Symbol „O“?", "Gold", "Silber", "Oxid", "Sauerstoff", 3],
    ["Was ist die Hauptstadt von Italien?", "Madrid", "Rom", "Mailand", "Florenz", 1],
    ["Wie viele Kontinente gibt es?", "5", "6", "7", "8", 2],
    ["Was ist 2 + 2?", "3", "4", "5", "6", 1],
    ["Welche Farbe hat der Himmel?", "Grün", "Blau", "Rot", "Gelb", 1]
]

# Создаём CSV-файл
df = pd.DataFrame(data, columns=["Frage", "Option0", "Option1", "Option2", "Option3", "Richtige option"])

csv_filename = "fragen.csv"
df.to_csv(csv_filename, index=False)  

csv_filename