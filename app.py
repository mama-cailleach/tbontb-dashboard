import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TBONTB Dashboard",
    page_icon="🏏",
    layout="wide"
)

# --- Data loading functions (using sample data for now) ---
@st.cache_data
def load_matches():
    # To use full data, change to: "csv/TBONTB_all_matches.csv"
    return pd.read_csv("csv/samples/sample_TBONTB_all_matches.csv")

@st.cache_data
def load_players_summary():
    # To use full data, change to: "csv/TBONTB_players_summary.csv"
    return pd.read_csv("csv/samples/sample_TBONTB_players_summary.csv")

# --- Sidebar navigation ---
st.sidebar.title("Menu")
page = st.sidebar.radio(
    "Go to page:",
    ["Home", "Matches", "Players", "Venues", "About"]
)

matches = load_matches()
players = load_players_summary()

if page == "Home":
    st.title("🏏 TBONTB Dashboard Home")
    st.markdown("*Team summary and quick stats*")

    # --- Team summary stats ---
    total_matches = len(matches)
    wins = (matches["Result"].str.lower() == "win").sum()
    losses = (matches["Result"].str.lower() == "loss").sum()
    ties = (matches["Result"].str.lower() == "tie").sum()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Matches", total_matches)
    col2.metric("Wins", wins)
    col3.metric("Losses", losses)
    col4.metric("Ties", ties)

    # --- Top performers ---
    st.subheader("Top Performers")
    top_run = players.sort_values("runs", ascending=False).iloc[0]
    top_wicket = players.sort_values("wickets", ascending=False).iloc[0]
    best_avg = players[players["bat_avg"] > 0].sort_values("bat_avg", ascending=False).iloc[0]

    st.write(f"**Top Run-Scorer:** {top_run['player_name']} ({top_run['runs']} runs)")
    st.write(f"**Top Wicket-Taker:** {top_wicket['player_name']} ({top_wicket['wickets']} wickets)")
    st.write(f"**Best Batting Average:** {best_avg['player_name']} ({best_avg['bat_avg']:.2f})")

    # --- Recent results ---
    st.subheader("Recent Results")

    # Create a "Score" column for display
    recent = matches.sort_values("Date", ascending=False).head(5).copy()
    recent["Score"] = ( "TBONTB " + 
    recent["Team Runs"].astype(str) + "/" +
    recent["Team Wickets Fallen"].astype(str) + " x " +
    recent["Opposition Runs"].astype(str) + "/" +
    recent["Opposition Wickets Fallen"].astype(str)
    )
    st.dataframe(recent[["Date", "Score", "Opposition Name", "Result", "Result Info"]], width='stretch')

    # --- Quick links ---
    st.subheader("Quick Links")
    st.markdown("[Go to Matches](#)")
    st.markdown("[Go to Players](#)")
    st.markdown("[Go to Venues](#)")
    st.markdown("[About](#)")


elif page == "Matches":
    st.title("All Matches")
    st.markdown("View all matches with filters and full details. Columns used in the Score are replaced by the Score column.")

    # Prepare data
    matches_display = matches.copy()
    matches_display["Score"] = (
        matches_display["Team Runs"].astype(str) + "/" +
        matches_display["Team Wickets Fallen"].astype(str) + " (" +
        matches_display["Team Overs"].astype(str) + " ov) " +
        " x " +
        matches_display["Opposition Runs"].astype(str) + "/" +
        matches_display["Opposition Wickets Fallen"].astype(str) + " (" +
        matches_display["Opposition Overs"].astype(str) + " ov)"
    )

    # Columns 
    cols = ["Match ID", "Date", "Venue", "Result", "Score", "Opposition Name", "Result Info", "Player of the Match"]

    # --- Filtering ---
    with st.expander("Filters", expanded=True):
        seasons = sorted(matches_display["Season"].unique())
        selected_season = st.selectbox("Season", ["All"] + [str(s) for s in seasons])
        venues = sorted(matches_display["Venue"].unique())
        selected_venue = st.selectbox("Venue", ["All"] + venues)
        results = sorted(matches_display["Result"].dropna().unique())
        selected_result = st.selectbox("Result", ["All"] + results)

    filtered = matches_display.copy()
    if selected_season != "All":
        filtered = filtered[filtered["Season"].astype(str) == selected_season]
    if selected_venue != "All":
        filtered = filtered[filtered["Venue"] == selected_venue]
    if selected_result != "All":
        filtered = filtered[filtered["Result"] == selected_result]

    st.dataframe(filtered[cols], width='stretch')

    # --- Future: Scorecard button for each match ---
    # for idx, row in filtered.iterrows():
    #     st.button("Scorecard", key=row["Match ID"])
    #     # Would link to a match detail page/section


elif page == "Players":
    st.title("Players")
    st.markdown("Explore player stats. Use filters and leaderboards to explore top performers.")

    # Load sample players summary data
    @st.cache_data
    def load_players_summary():
        # To use full data, change to: "csv/TBONTB_players_summary.csv"
        return pd.read_csv("csv/samples/sample_TBONTB_players_summary.csv")
    players_df = load_players_summary()


    # --- All-Time Leaderboard (not affected by filters) ---
    st.subheader("All-Time Leaderboard")
    leaderboard_type = st.selectbox("Leaderboard by:", ["Runs", "Wickets", "Batting Average"])
    if leaderboard_type == "Runs":
        top = players_df.sort_values("runs", ascending=False).head(5)
        chart_col = "runs"
        chart_title = "Top 5 by Runs"
    elif leaderboard_type == "Wickets":
        top = players_df.sort_values("wickets", ascending=False).head(5)
        chart_col = "wickets"
        chart_title = "Top 5 by Wickets"
    else:
        top = players_df[players_df["bat_avg"] > 0].sort_values("bat_avg", ascending=False).head(5)
        chart_col = "bat_avg"
        chart_title = "Top 5 by Batting Average"

    import plotly.express as px
    fig = px.bar(top, x="player_name", y=chart_col, title=chart_title, text=chart_col)
    st.plotly_chart(fig, width='stretch')
    #st.dataframe(top[["player_name", "matches", "runs", "wickets", "bat_avg"]], width='stretch')

    # --- Filters ---
    with st.expander("Filters for Players Stats", expanded=True):
        min_matches = int(players_df["matches"].min())
        max_matches = int(players_df["matches"].max())
        matches_played = st.slider("Minimum Matches Played", min_matches, max_matches, min_matches)
        player_names = sorted(players_df["player_name"].unique())
        selected_player = st.selectbox("Player Name (optional)", ["All"] + player_names)

    filtered = players_df[players_df["matches"] >= matches_played].copy()
    if selected_player != "All":
        filtered = filtered[filtered["player_name"] == selected_player]
    st.write(f"Players: {len(filtered)}")

    # --- Player Table ---
    st.subheader("Player Summary Table")
    summary_cols = ["player_name", "matches", "runs", "wickets", "bat_avg"]
    st.dataframe(filtered[summary_cols], width='stretch')

    # --- If a single player is selected, show full stats ---
    if selected_player != "All" and not filtered.empty:
        st.subheader(f"Full Stats for {selected_player}")
        st.dataframe(filtered.T, width='stretch')

elif page == "Venues":
    st.title("Venues")
    st.markdown("Explore all venues. All columns are shown for now. Use filters to explore.")

    # Load sample venues data
    @st.cache_data
    def load_venues():
        # To use full data, change to: "csv/TBONTB_venues.csv"
        return pd.read_csv("csv/samples/sample_TBONTB_venues.csv")
    venues_df = load_venues()

    # Pie chart: matches played per venue
    st.subheader("Matches Played per Venue")
    import plotly.express as px
    fig = px.pie(
        venues_df,
        names="Venue",
        values="Total Matches",
        title="Distribution of Matches Played by Venue",
        hole=0.3
    )
    st.plotly_chart(fig, width='stretch')

    # --- Filtering ---
    with st.expander("Filters", expanded=True):
        venue_names = sorted(venues_df["Venue"].unique())
        selected_venue = st.selectbox("Venue", ["All"] + venue_names)
        min_matches = int(venues_df["Total Matches"].min())
        max_matches = int(venues_df["Total Matches"].max())
        matches_played = st.slider("Minimum Matches Played", min_matches, max_matches, min_matches)

    filtered = venues_df.copy()
    if selected_venue != "All":
        filtered = filtered[filtered["Venue"] == selected_venue]
    filtered = filtered[filtered["Total Matches"] >= matches_played]

    st.dataframe(filtered, width='stretch')

elif page == "About":
    st.title("About This App")
    st.write("Hullo! This is a web app dashboard for interactive visualization of TBONTB cricket stats.")
    st.write("This app ties in with the blog [Double Double Stats and Trouble](https://mama-cailleach.github.io/double-double-stats-and-trouble/).")
    st.write("Explore a bit of our team history in numbers and graphs.")
    st.write("This is a first iteration, mostly for testing and tinkering. More features and polish to come...")
    st.write("Feedback always welcome! What do you want to see next?")
    st.write("Made by [mama](https://github.com/mama-cailleach) | marcelo.terreiro@gmail.com")
