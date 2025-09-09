# tbontb-dashboard

This repository contains the Streamlit dashboard for the "Two Bats or Not To Bat" (TBONTB) cricket team stats project.

## What is this?

A work-in-progress web app to explore and visualize TBONTB cricket data (2013–2025) interactively. The dashboard lets you view team results, player stats, venue records, and more, with filtering and charts.

## How does it work?

- **Built with:** [Streamlit](https://streamlit.io/) (Python), using pandas for data and plotly for charts.
- **Main file:** `app.py` (run this to launch the dashboard).
- **Data:** CSV files for matches, players, venues, batting, and bowling stats.
- **Navigation:** Use the sidebar to switch between Home, Matches, Players, Venues, and About pages.
- **Filtering:** Each page has filters for seasons, venues, player names, etc.
- **Deployment:** The app is deployed on Streamlit Community Cloud and updates automatically from this GitHub repo.

## Current Status

- First iteration deployed and live for testing (as of September 2025)
- Home, Matches, Players, Venues, and About pages implemented
- Filtering, summary stats, and leaderboards available
- Feedback form included on the About page
- See [Planing and Updates/phase4_progress_log.md](Planing%20and%20Updates/phase4_progress_log.md) for the latest progress and next steps

## Want more details?

- See [Planing and Updates/phase4_consolidated_plan.md](Planing%20and%20Updates/phase4_consolidated_plan.md) for the full project plan and technical roadmap.
- See [Explanations/data_dictionary.md](Explanations/data_dictionary.md) for a description of all data columns.
- See [Explanations/apppy_1stiteration_explained.md](Explanations/apppy_1stiteration_explained.md) for a beginner-friendly technical overview of the app.

---

_This project is still in active development. Feedback and suggestions are welcome!_