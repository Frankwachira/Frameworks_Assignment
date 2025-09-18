import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('metadata.csv', low_memory=False)
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))
filtered = df[df['year'].between(year_range[0], year_range[1])]

st.write(f"Papers published between {year_range[0]} and {year_range[1]}: {len(filtered)}")
st.bar_chart(filtered['journal'].value_counts().head(10))
st.dataframe(filtered[['title', 'journal', 'publish_time']].head(10))