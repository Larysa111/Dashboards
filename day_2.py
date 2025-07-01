
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

# print("a") 

# def button_was_clicked():
#     print("Ein Button wurde geklickt")
# def button_was_clicked():
#     print("Ein 2Button wurde geklickt")


# print("b")    

# klickbox = st.button("Klick hier", on_click= button_was_clicked)
# klickbox = st.button("Klick hier 2", on_click= button_was_clicked)
# print("----")

# st.button("Klick mich", key="button1")
# st.button("Klick mich", key="button2")
# st.button("Klick mich", key="button3")
 
# if st.session_state.button1:
#     st.write("Button wurde geklickt")
 
# #st.write(f"# Über Variable: {var_richtung}")
# st.write(f"# Über Sessionstate: {st.session_state.richtung}")
 
# st.radio(
#     label="Wähle aus: ",
#     options=["links", "mitte", "rechts", "oben", "unten"],
#     key="richtung"
#     )
 
 
# st.write(st.session_state)

# bmi_form = st.form(key="bmi_form")
 
# with bmi_form:
#     col1, col2 = st.columns(2)
 
#     with col1:
#         first_name = st.text_input("Vorname")
#         age = st.number_input(
#             "Dein Alter",
#             min_value=0,
#             max_value=120,
#             value=18,
#             step=1,
#         )
 
#     with col2:
#         height_cm = st.number_input(
#             "Körpergröße in cm",
#             min_value=50.5,
#             max_value=250.0,
#             value=170.0,
#             step=0.1,
#             format="%.1f",
#         )
 
#         weight = st.number_input(
#             "Dein Gewicht in kg",
#             min_value=0.0,        
#             max_value=600.0,      
#             value=50.5,        
#             step=0.1,          
#             format="%.1f"
#         )
 
#     subbmitted = st.form_submit_button("Absenden")
 
# if subbmitted:
#     st.write(f"Hallo {first_name}")
#     st.write(f"du bist {age} Jahre alt")
#     st.metric(
#         label="BMI",
#         value=weight/(height_cm/100)**2
#         )

# def greetings():
#     print("Willkommen volljähriger Benutzer!")
#     print(f"Status der Checkbox: {st.session_state.adult_check}")

# is_adult = st.checkbox(label="Volljährig", value=False, on_change=greetings, key="adult_check")
# if is_adult:
#     st.write("Benutzer ist volljährig")


# city = st.selectbox("Stadt auswählen:", ["Berlin", "München", "Hamburg"])
# st.write("Deine Stadt:", city)

# foods = st.multiselect("Lieblingsessen:", ["Pizza","Sushi","Salat"])
# st.write("Du magst:", foods)

# age = st.slider("Wie alt bist du?", 0, 100, 25)
# st.write("Alter:", age)

# d = st.date_input("Datum wählen")
# t = st.time_input("Uhrzeit wählen")
# st.write("Ausgewählt:", d, t)
import streamlit as st



st.title("BMI Rechner")

with st.form(key="first_form"):
    first_name = st.text_input("Vorname")
    second_name = st.text_input("Nachname")
    age = st.number_input(
        "Dein Alter",
        min_value=0,        
        max_value=120,      
        value=18,        
        step=1,           
        format="%d"
    )
    mail = st.text_input("E-Mail")
    submitted = st.form_submit_button("Absenden")


with st.form(key="first_form"):
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("Vorname")
        age = st.number_input(
            "Dein Alter",
            min_value=0,        
            max_value=120,      
            value=18,        
            step=1,           
            format="%d"
        )
        height_cm = st.number_input(
            "Deine Körpergröße in cm",
            min_value=50.0,
            max_value=250.0,
            value=170.0,
            step=0.5,
            format="%.1f"
            )
    with col2:
        second_name = st.text_input("Nachname")
        weight = st.number_input(
            "Dein Gewicht in kg",
            min_value=0.0,        
            max_value=600.0,      
            value=50.5,        
            step=0.1,           
            format="%.1f"
        )

    mail = st.text_input("E-Mail")
    submitted = st.form_submit_button("Absenden")

if submitted:
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Untergewicht"
    elif bmi < 25:
        category = "Normalgewicht"
    elif bmi < 30:
        category = "Übergewicht"
    elif bmi < 35:
        category = "Adipositas Grad I"
    elif bmi < 40:
        category = "Adipositas Grad II"
    else:
        category = "Adipositas Grad III"

    st.success(f"Hallo {first_name} {second_name}!")
    st.write(f"- **Alter:** {age} Jahre")  
    st.write(f"- **Größe:** {height_cm:.1f} cm")  
    st.write(f"- **Gewicht:** {weight:.1f} kg")  
    st.metric(label="Dein BMI", value=f"{bmi:.1f}", delta=f"{category}")
    
    st.markdown("**Gewichtsklassifikation bei Erwachsenen:**")
    st.markdown("""
    - BMI < 18,5: Untergewicht  
    - BMI 18,5 - 24,9: Normalgewicht  
    - BMI 25 - 29,9: Übergewicht  
    - BMI 30 - 34,9: Adipositas Grad I  
    - BMI 35 - 39,9: Adipositas Grad II  
    - BMI ≥ 40: Adipositas Grad III  
    """)
    st.write("Bei Fragen kann dir dein Arzt weiterhelfen.")