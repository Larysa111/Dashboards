import streamlit as st
import pandas as pd
import io
import plotly.express as px

st.set_page_config(page_title='BMI Tracker', layout="centered", initial_sidebar_state="expanded")


# Функция для определения категории ИМТ
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Untergewicht"
    elif 18.5 <= bmi < 25:
        return "Normalgewicht"
    elif 25 <= bmi < 30:
        return "Übergewicht"
    else:
        return "Fettleibigkeit" 


if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame({
        "Name": ["Alice", "Bob", "Clara"],
        "Height (cm)": [172.5, 165.0, 180.3],
        "Weight (kg)": [60.0, 70.0, 55.5] # Добавляем колонку для веса
    })   
        
# Рассчитываем BMI для начальных данных
    # BMI = вес (кг) / (рост (м) * рост (м))
    st.session_state.data["BMI"] = st.session_state.data.apply(
        lambda row: round(row["Weight (kg)"] / ((row["Height (cm)"] / 100)**2), 1) if row["Height (cm)"] > 0 else 0, axis=1
    )
    # Добавляем колонку для статуса ИМТ
    st.session_state.data["BMI Status"] = st.session_state.data["BMI"].apply(get_bmi_category)


st.title("📏 BMI Tracker")    

with st.sidebar:
    st.header("Add a new person")
    name = st.text_input("Name", key="name_input")
    height = st.number_input("Height (cm)", min_value=0.0, step=0.1, key="height_input")
    weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1, key="weight_input") 
    
    if st.button("Save"):
        if name and height and weight: # Проверяем все три поля
            # Рассчитываем BMI для нового человека
            bmi = round(weight / ((height / 100)**2), 1) if height > 0 else 0
            # Определяем статус ИМТ
            bmi_status = get_bmi_category(bmi)

            new_data_row = pd.DataFrame({
                "Name": [name],
                "Height (cm)": [height],
                "Weight (kg)": [weight], # Добавляем вес
                "BMI": [bmi], # Добавляем BMI
                "BMI Status": [bmi_status] # Добавляем статус ИМТ
            })

            st.session_state.data = pd.concat(
                [st.session_state.data, new_data_row], # Используем напрямую st.session_state.data
                ignore_index=True,
            )
            st.toast(f"Gespeichert: {name} - {height:.1f} cm, {weight:.1f} kg, BMI: {bmi:.1f} ({bmi_status})", icon="✅")
        else:
            st.toast("Bitte Name, Größe und Gewicht eingeben!", icon="⚠️") # Обновляем сообщение


    st.markdown("---")
    st.header("Datenoptionen")  


    uploaded_file = st.file_uploader("CSV-Datei hochladen", type="csv")
    if uploaded_file is not None:
       try:
           df_upload = pd.read_csv(uploaded_file)
           # Проверяем наличие всех трех базовых колонок
           required_cols = {"Name", "Height (cm)", "Weight (kg)"}
           if required_cols.issubset(df_upload.columns):
                # Если BMI нет в загруженном файле, рассчитаем его
                if "BMI" not in df_upload.columns:
                   df_upload["BMI"] = df_upload.apply(
                       lambda row: round(row["Weight (kg)"] / ((row["Height (cm)"] / 100)**2), 1) if row["Height (cm)"] > 0 else 0, axis=1
                   )
                # Добавляем статус ИМТ, если его нет
                if "BMI Status" not in df_upload.columns:
                    df_upload["BMI Status"] = df_upload["BMI"].apply(get_bmi_category)
   
                st.session_state.data = df_upload
                st.toast("Datei erfolgreich geladen!", icon="📄")
           else:
               st.warning(f"Die Datei muss die Spalten {', '.join(required_cols)} enthalten.") # Обновляем сообщение
       except Exception as e:
           st.error(f"Fehler beim Laden der Datei: {e}")


    if st.button("🗑️ Datensatz leeren"):
           # Очистка теперь включает и вес, и BMI
           st.session_state.data = pd.DataFrame({"Name": [], "Height (cm)": [], "Weight (kg)": [], "BMI": [], "BMI Status": []})
           st.toast("Daten wurden zurückgesetzt.", icon="🗑️")

    st.download_button(
        label="📥 CSV herunterladen",
        data=st.session_state.data.to_csv(index=False).encode("utf-8"),
        file_name="BMI_data.csv", # Обновляем имя файла
        mime="text/csv"
)          


st.subheader("Datensatz (bearbeitbar)")
# Теперь разрешаем редактирование всех колонок, включая BMI
edited_df = st.data_editor(
    st.session_state.data,
    num_rows="dynamic",
    use_container_width=True,
    key="data_editor",
    # Опционально можно сделать BMI нередактируемым, если он всегда должен быть рассчитанным
    column_config={
        "BMI": st.column_config.NumberColumn("BMI", help="Body-Mass-Index", format="%.1f", disabled=True),
        "BMI Status": st.column_config.TextColumn("BMI Status", help="Body-Mass-Index-Kategorie", disabled=True),
        "Weight (kg)": st.column_config.NumberColumn("Weight (kg)", help="Gewicht in Kilogramm", format="%.1f kg"),
        "Height (cm)": st.column_config.NumberColumn("Height (cm)", help="Wachstum in Zentimetern", format="%.1f cm")
    }
) 

# Пересчитываем BMI, если изменился рост или вес в таблице
# так как BMI должен зависеть от других значений
if not edited_df.equals(st.session_state.data): # Проверяем, были ли изменения
    # Убедимся, что мы работаем с копией, чтобы избежать SettingWithCopyWarning
    temp_df = edited_df.copy()
    temp_df["BMI"] = temp_df.apply(
        lambda row: round(row["Weight (kg)"] / ((row["Height (cm)"] / 100)**2), 1) if row["Height (cm)"] > 0 else 0, axis=1
    )
    temp_df["BMI Status"] = temp_df["BMI"].apply(get_bmi_category)
    st.session_state.data = temp_df
    st.toast("Daten aktualisiert, BMI und Status neu berechnet!", icon="🔄")


# Используем после всех потенциальных изменений в data_editor
current_data = st.session_state.data

if not current_data.empty:
    max_height = current_data["Height (cm)"].max()
    min_height = current_data["Height (cm)"].min()
    avg_height = current_data["Height (cm)"].mean()

    max_weight = current_data["Weight (kg)"].max() # Максимальный вес
    min_weight = current_data["Weight (kg)"].min() # Минимальный вес
    avg_weight = current_data["Weight (kg)"].mean() # Средний вес

    max_bmi = current_data["BMI"].max() # Максимальный BMI
    min_bmi = current_data["BMI"].min() # Минимальный BMI
    avg_bmi = current_data["BMI"].mean() # Средний BMI


    tallest_name = current_data.loc[current_data["Height (cm)"] == max_height, "Name"].values[0]
    shortest_name = current_data.loc[current_data["Height (cm)"] == min_height, "Name"].values[0]

    # Имена для максимального/минимального веса и BMI
    heaviest_name = current_data.loc[current_data["Weight (kg)"] == max_weight, "Name"].values[0]
    lightest_name = current_data.loc[current_data["Weight (kg)"] == min_weight, "Name"].values[0]

    highest_bmi_name = current_data.loc[current_data["BMI"] == max_bmi, "Name"].values[0]
    lowest_bmi_name = current_data.loc[current_data["BMI"] == min_bmi, "Name"].values[0]

    st.divider()
    st.subheader("Kennzahlen")
    # Три колонки для метрик роста, веса и BMI
    col_h1, col_h2, col_h3 = st.columns(3)
    col_w1, col_w2, col_w3 = st.columns(3)
    col_b1, col_b2, col_b3 = st.columns(3)

    # Метрики роста (как раньше)
    col_h1.metric("Größte Größe", f"{max_height:.1f} cm", f"von {tallest_name}")
    col_h2.metric("Kleinste Größe", f"{min_height:.1f} cm", f"von {shortest_name}")
    col_h3.metric("Durchschnitt (Größe)", f"{avg_height:.1f} cm") # Изменяем, чтобы было понятно, что это средний рост

    st.markdown("---") # Разделитель для ясности

    # Метрики веса
    col_w1.metric("Höchstes Gewicht", f"{max_weight:.1f} kg", f"von {heaviest_name}")
    col_w2.metric("Niedrigstes Gewicht", f"{min_weight:.1f} kg", f"von {lightest_name}")
    col_w3.metric("Durchschnitt (Gewicht)", f"{avg_weight:.1f} kg")

    st.markdown("---") # Разделитель для ясности

    # Метрики BMI
    col_b1.metric("Höchster BMI", f"{max_bmi:.1f}", f"von {highest_bmi_name}")
    col_b2.metric("Niedrigster BMI", f"{min_bmi:.1f}", f"von {lowest_bmi_name}")
    col_b3.metric("Durchschnitt (BMI)", f"{avg_bmi:.1f}") 

    st.divider()
    st.subheader("BMI-Verteilung")
    # Подготовка данных для Altair
    bmi_distribution_df = current_data["BMI Status"].value_counts().reset_index()
    bmi_distribution_df.columns = ["BMI Status", "Count"]

    # Подготовка данных для Plotly
    bmi_distribution_df = current_data["BMI Status"].value_counts().reset_index()
    bmi_distribution_df.columns = ["BMI Status", "Count"]

    # Определяем порядок категорий и соответствующие цвета
    category_order = ["Untergewicht", "Normalgewicht", "Übergewicht", "Fettleibigkeit"]
    color_map = {
        "Untergewicht": "blue",
        "Normalgewicht": "green",
        "Übergewicht": "yellow",
        "Fettleibigkeit": "red"
    }

    # Создаем Plotly диаграмму
    fig = px.bar(
        bmi_distribution_df,
        x="BMI Status",
        y="Count",
        title="Verteilung des BMI nach Kategorien",
        color="BMI Status", # Указываем столбец для раскрашивания
        color_discrete_map=color_map, # Применяем нашу карту цветов
        category_orders={"BMI Status": category_order} # Устанавливаем порядок категорий
    )

    # Обновляем макет для лучшего отображения
    fig.update_layout(xaxis_title="BMI Status", yaxis_title="Anzahl der Personen")
    
    st.plotly_chart(fig, use_container_width=True) # Отображаем диаграмму Plotly
else:
    st.info("Füge Daten hinzu, um Kennzahlen zu sehen.")
   