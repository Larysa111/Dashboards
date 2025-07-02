import streamlit as st
import pandas as pd
import plotly.express as px

#загрузка csv файла
df = pd.read_csv("teams_1.csv")
st.title("NHL Teams")

#установка типа переменной для год
df["Jahr"] = df["Jahr"].astype(int)

#боковая панель, делаем множественный выбор
team_names = sorted(df["Team"].unique())
selected_teams = st.multiselect(
    "Waehle Teamnamen",
    options=team_names,
    default=team_names[:3]
)

#боковая панель, делаем слайдер для года
min_year = df["Jahr"].min()
max_year = df["Jahr"].max()
year_range = st.slider(
    "Jahresbereich filtern",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1
)
#применяем фильтр
df_filtered = df[
    (df["Team"].isin(selected_teams)) &
    (df["Jahr"].between(year_range[0], year_range[1]))
]

#показываем таблицу
st.expander("Datensatz anzeigen").dataframe(df_filtered, use_container_width=True)

#выпадающий список выбора метрики
st.markdown("## Trendanalyse als Liniediagramm")
metric_options = ["GF", "AF", "Siege", "Niederlagen"]
selected_metric = st.selectbox(
    "Waehle die Metrik fur das Liniendiagramm",
    options=metric_options,
)


if df_filtered.empty:
    st.info("Keine Daten fur gewaelten Filter")
else:
    fig = px.line(
        df_filtered,
        x="Jahr",
        y=selected_metric,
        color="Team",
        markers=True,
        title=f"Verlauf von {selected_metric}"
    )

    fig.update_layout(legend_title_text='Tram')
    st.plotly_chart(fig, use_container_width=True)      