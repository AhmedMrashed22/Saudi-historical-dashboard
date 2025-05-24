import streamlit as st
import pandas as pd
import geopandas as gpd
import streamlit.components.v1 as components
import altair as alt

st.set_page_config(layout="wide", page_title="Saudi Historical Dashboard")

st.title("🕌 Saudi Arabia Historical Places Dashboard")

# Sidebar
st.sidebar.header("Filter Options")
show_map = st.sidebar.checkbox("Show Map", True)
show_table = st.sidebar.checkbox("Show Table", True)

# Load data
gdf = gpd.read_file("historical_sites.geojson")
df = pd.DataFrame(gdf.drop(columns='geometry'))

# Visitors Summary
st.metric("📊 Total Visitors (All Sites)", f"{df['visitors'].sum():,}")

# Visitors Bar Chart
st.subheader("📈 Visitors per Historical Site")

chart = alt.Chart(df).mark_bar().encode(
    x=alt.X("name:N", title="Historical Site"),
    y=alt.Y("visitors:Q", title="Number of Visitors"),
    tooltip=["name", "visitors"]
).properties(
    width=700,
    height=400
)

st.altair_chart(chart, use_container_width=True)

# Map
if show_map:
    st.subheader("🗺️ Interactive Map")
    components.html(open("map.html").read(), height=600)

# Table
if show_table:
    st.subheader("📋 Site Information Table")
    st.dataframe(df)
