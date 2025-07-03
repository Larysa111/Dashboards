import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime
import pytz

# функция для получения данных о землетрясениях
@st.cache_data(ttl=120)
def fetch_earthquake_data(url):
    response = requests.get(url)
    data = response.json()
    
    # анализируем данные
    features = data['features']
    earthquakes = []
    for feature in features:
        properties = feature['properties']
        geometry = feature['geometry']
        utc_time = pd.to_datetime(properties['time'], unit='ms')
        local_time = utc_time.tz_localize('UTC').tz_convert(pytz.timezone('America/Los_Angeles'))  # конвертируем в локальную зону
        earthquakes.append({
            "place": properties['place'],
            "magnitude": properties['mag'],
            "time_utc": utc_time,
            "time_local": local_time,
            "latitude": geometry['coordinates'][1],
            "longitude": geometry['coordinates'][0]
        })
    
    return pd.DataFrame(earthquakes)

# получение данных в реальном времени
realtime_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
df = fetch_earthquake_data(realtime_url)

# realtime_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
# df = fetch_earthquake_data(realtime_url)


st.title("Erdbeben Visualisierung")

count_of_earthquakes = df.shape[0]
st.text(f"In den letzten 30 Tagen gabe es insgesamt {count_of_earthquakes} Erdbeben.")

col1, col2 = st.columns(2)

earliest_date = df.time_utc.min().date()

from_date = col1.date_input(label="Von", value=earliest_date, min_value=earliest_date, max_value='today')
end_date = col2.date_input(label="Bis", value='today', min_value=earliest_date, max_value='today')

if end_date < from_date:
    st.error("Startdatum darf nicht vor Enddatum liegen.")

df_zeitraum = df[(df.time_utc.dt.date >= from_date) & (df.time_utc.dt.date <= end_date)]


st.metric("Erdbeben im Zeitraum", df_zeitraum.shape[0])

anzahl_df = df_zeitraum.groupby(df_zeitraum.time_utc.dt.date).size()

fig_bar = px.bar(anzahl_df, title="Einträge pro Tag",)
fig_bar.update(layout_showlegend=False)

st.plotly_chart(fig_bar, theme="streamlit")

fig_earth = px.scatter_map(
    df_zeitraum.query("magnitude > 0"),
    lat="latitude",
    lon="longitude",
    color="magnitude",
    color_continuous_scale="YlOrRd",
    hover_name="place",
    hover_data={"time_utc": True, "time_local": True, "magnitude": True},
    zoom=1,
    height=600,
    title="Geomap"
)

st.plotly_chart(fig_earth)

with st.expander("Daten im Zeitraum anzeigen"):
    st.dataframe(df_zeitraum)

# st.subheader("Tektonische Platten")
# st.image("https://getech.com/wp-content/uploads/2020/09/tectonic-plates-map-world.png")


st.subheader("Tektonische Platten")
st.image("https://earthhow.com/wp-content/uploads/2019/01/plate_tectonics_labels-1350x798.png")