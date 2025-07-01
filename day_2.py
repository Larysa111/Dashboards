import streamlit as st
# print("Code wird erneut ausgefurt")
# st.title("Tag 2 wird interaktiv")

# is_adult = st.checkbox(label="Volljahrig")

# # print(is_adult)

# if is_adult:
#     st.write("Benutzer ist Volljahrig")
# # else:
# #     st.write("Benutzer ist nicht Volljahrig")


# klickbox = st.button("Klick hier")
# print(klickbox)

# if klickbox:
#     st.write("Dutton wurde geklickt")
# else:
#     st.write("Button verfehlt")

# farbe = st.radio("Wahle eine Farbe", ["rot", "grun", "orang"])
# st.write(f"Die ausgewelt Farbe ist: {farbe}")

print("a") 

def button_was_clicked():
    print("Ein Button wurde geklickt")

print("b")    

klickbox = st.button("Klick hier", on_click= button_was_clicked)

print("----")



