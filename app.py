import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TBONTB Batting Records Test",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 TBONTB Batting Records (Test)")
st.markdown("*Quick test app for viewing all batting records*")

# Load batting data
@st.cache_data
def load_batting_data():
    return pd.read_csv("csv/TBONTB_all_batting.csv")

data = load_batting_data()

# Show dataframe
st.subheader("All Batting Records")
st.dataframe(data, width='stretch')

# Simple player filter
players = data["player_name"].unique().tolist()
selected_player = st.selectbox("Select Player", ["All"] + players)

if selected_player != "All":
    filtered = data[data["player_name"] == selected_player]
    st.write(f"Showing records for: {selected_player}")
    st.dataframe(filtered, width='stretch')
else:
    st.write("Showing all records.")
