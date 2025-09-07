# What does `app.py` do?

This file is a simple Streamlit app for viewing TBONTB cricket batting records. Here’s what each part does, explained for beginners:

## 1. Importing Libraries
- `import streamlit as st` — Lets us build web apps easily in Python.
- `import pandas as pd` — Helps us work with data tables (like Excel in Python).

## 2. Page Setup
- `st.set_page_config(...)` — Sets the app’s title, icon, and layout.
- `st.title(...)` and `st.markdown(...)` — Show a big title and a short description at the top of the page.

## 3. Loading the Data
- `@st.cache_data` — Makes loading faster by remembering the data after the first time.
- `def load_batting_data(): ...` — Reads the CSV file with all the batting records.
- `data = load_batting_data()` — Actually loads the data so we can use it.

## 4. Showing the Data
- `st.subheader(...)` — Adds a smaller heading.
- `st.dataframe(data, ...)` — Shows the whole table of batting records so you can scroll and look at it.

## 5. Filtering by Player
- Gets a list of all player names from the data.
- `st.selectbox(...)` — Lets you pick a player from a dropdown menu (or choose "All").
- If you pick a player, it shows only their records. If you pick "All", it shows everyone.

## Summary
- This app lets you look at all batting records, or just one player’s, in a simple web page.
- You don’t need to know much Python to use it—just run the app and use the dropdown to explore the data!
