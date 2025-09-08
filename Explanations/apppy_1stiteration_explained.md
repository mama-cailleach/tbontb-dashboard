
# What does `app.py` do? (First Iteration, Technical Overview)

This file is a Streamlit app for exploring TBONTB cricket stats. Here’s how it works, step by step:

## 1. Importing Modules
- `import streamlit as st` — The main library for building the web app interface.
- `import pandas as pd` — Used for loading and working with data tables (like spreadsheets).
- `import plotly.express as px` — Used for making charts and graphs.

## 2. Page Setup
- `st.set_page_config(...)` — Sets the app’s title, icon, and layout for a better user experience.

## 3. Data Loading Functions
- The app defines functions like `load_matches()`, `load_players()`, etc., each using `@st.cache_data` to speed up repeated loading.
- Each function uses `pd.read_csv()` to read a sample CSV file (matches, players, venues, etc.) into a DataFrame (a table of data).

## 4. Sidebar Navigation
- The sidebar uses `st.sidebar.radio()` to let you pick which page to view (Home, Matches, Players, Venues, About).
- The selected page controls which part of the app runs next.

## 5. Home Page Functions
- Shows team summary stats by using pandas functions like `.sum()` and `.value_counts()`.
- Finds top performers by sorting DataFrames with `.sort_values()`.
- Shows the last 5 match results using `.tail(5)`.
- Uses Streamlit widgets (`st.metric`, `st.dataframe`) to display numbers and tables.

## 6. Matches Page Functions
- Loads all matches into a DataFrame.
- Lets you filter matches by season, venue, or result using Streamlit widgets (`st.selectbox`, `st.multiselect`).
- Combines columns (like runs and wickets) using pandas string formatting.
- Displays the filtered table with `st.dataframe()`.

## 7. Players Page Functions
- Loads player stats and shows leaderboards using pandas sorting and filtering.
- Uses Plotly (`px.bar`) to make bar charts for top players.
- Lets you filter by player name or minimum matches played.
- Shows a summary table and, if a player is selected, their detailed stats.

## 8. Venues Page Functions
- Loads venue data and counts matches per venue.
- Uses Plotly (`px.pie`) to make a pie chart of matches by venue.
- Lets you filter venues and shows a table of stats.

## 9. About Page
- Placeholder for info (just text for now).

## Summary
- The app is organized into functions for each page and for loading data.
- It uses Streamlit for the interface, pandas for data, and Plotly for charts.
- You can explore and filter cricket stats using simple controls—no coding needed!
