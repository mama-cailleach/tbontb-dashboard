# Phase 4 - Streamlit Dashboard Consolidated Plan

## 🎯 Project Overview

**Goal**: Create a Python-based Streamlit dashboard for TBONTB cricket team statistics (2013-2025)  
**Purpose**: Team engagement, easy data visualization, and portfolio showcase  
**Timeline**: 6-8 weeks for MVP deployment

---

## 📋 Platform Decision

### Streamlit - Selected ✅

| Aspect | Pros | Cons |
|--------|------|------|
| **Learning Curve** | Python-based, easy to learn | Less interactive than dedicated BI tools |
| **Cost** | Free hosting on Streamlit Cloud | Some layout limitations |
| **Portfolio Value** | Great for showcasing technical skills | - |
| **Team Access** | Good mobile support, web-based | - |
| **Future Growth** | Can upgrade to Plotly/Dash later | - |

**Rejected Alternatives**: Power BI (cost/learning curve), Tableau (expensive/overkill), Dash (too complex for first project)

---

## 🗂️ Repository & Environment Setup

### Repository Structure
**Decision**: Create separate repository for clean deployment
- New repo: `tbontb-dashboard` 
- Keeps dashboard code separate from data processing
- Easier for Streamlit Cloud deployment
- Better portfolio showcase

```
/tbontb-dashboard (new repository)
├── /data
│   ├── README.md           # Explains data sources
│   └── .gitignore         # Ignores actual CSV files
├── /pages                 # Multi-page components
├── app.py                 # Main dashboard file
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

### Environment Setup
```bash
# 1. Navigate to project directory
cd /path/to/tbontb-dashboard

# 2. Create virtual environment
python -m venv venv

# 3. Activate (Windows)
venv\Scripts\activate

# 4. Install packages
pip install streamlit pandas plotly

# 5. Save dependencies
pip freeze > requirements.txt

# 6. Run dashboard
streamlit run app.py
```

---

## 📊 Data Architecture

### Data Source Strategy
**Approach**: Separate CSVs with helper functions for joins

**Available Data Files**:
- `TBONTB_all_batting.csv` - Individual batting performances
- `TBONTB_all_bowling.csv` - Individual bowling performances  
- `TBONTB_match_info.csv` - Match details and outcomes
- `TBONTB_venues.csv` - Venue-specific statistics

**Data Loading Pattern**:
```python
@st.cache_data
def load_and_process_data():
    # Load separate files
    batting_df = pd.read_csv("data/TBONTB_all_batting.csv")
    bowling_df = pd.read_csv("data/TBONTB_all_bowling.csv")
    matches_df = pd.read_csv("data/TBONTB_match_info.csv")
    
    # Create derived views as needed
    player_combined = pd.merge(
        batting_df.groupby(['player_name', 'Season'])['runs'].sum().reset_index(),
        bowling_df.groupby(['player_name', 'Season'])['wickets'].sum().reset_index(),
        on=['player_name', 'Season'], how='outer'
    ).fillna(0)
    
    return {
        "batting": batting_df,
        "bowling": bowling_df,
        "matches": matches_df,
        "player_combined": player_combined
    }
```

**Benefits**:
- Clean data organization
- Efficient caching (joins happen once per session)
- Flexible for future requirements
- Maintains data integrity

---

## 🏗️ Development Roadmap

### Phase 1: MVP Foundation (Week 1-2)
**Core Infrastructure**
- Environment setup and repository creation
- Basic Streamlit app structure
- Data loading and caching implementation
- Simple navigation framework

**MVP Features**:
- Player search and basic statistics
- Season filtering
- Simple visualizations (bar charts, line graphs)

### Phase 2: Core Features (Week 3-4)
**Multi-page Navigation**:
- Home: Team overview and recent performance
- Player Stats: Individual player deep-dive
- Team Records: Milestones and achievements

**Key Functionality**:
- Player dropdown with autocomplete
- Games played threshold filter
- Basic career statistics display
- Performance trend visualizations

### Phase 3: Enhanced Features (Week 5-6)
**Advanced Filtering**:
- Season multi-select
- Venue performance breakdown
- Opposition analysis
- Multi-dimensional filtering combinations

**Improved Visualizations**:
- Interactive Plotly charts
- Mobile-responsive design
- Performance comparison tools

### Phase 4: Deployment & Feedback (Week 7-8)
**Production Deployment**:
- Streamlit Cloud hosting setup
- Team sharing and feedback collection
- Performance optimization
- Bug fixes and iterations

---

## 🎨 User Interface Design

### Sidebar Configuration
```python
# Global filters (apply across all pages)
st.sidebar.title("Filters")

# Minimum games filter
min_games = st.sidebar.slider("Minimum Games Played", 1, 50, 3)

# Season selection
all_seasons = data["batting"]["Season"].unique().tolist()
selected_seasons = st.sidebar.multiselect("Select Seasons", all_seasons, default=all_seasons)

# Main navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page", [
    "Team Overview", 
    "Player Statistics", 
    "Venue Analysis", 
    "Submit Feedback"
])
```

### Page Structure
**Consistent Layout**:
- Header with team branding
- Sidebar for navigation and global filters
- Main content area with responsive columns
- Footer with data update information

**Mobile Responsiveness**:
- Streamlit's built-in responsive design
- Appropriate chart sizing for mobile screens
- Touch-friendly interface elements

---

## 🔧 Technical Implementation

### Starter Application Template
```python
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="TBONTB Cricket Dashboard", 
    page_icon="🏏", 
    layout="wide"
)

# Data loading function
@st.cache_data
def load_data():
    # Implementation from data architecture section
    pass

# Main application logic
def main():
    # Load data
    data = load_data()
    
    # Header
    st.title("🏏 TBONTB Cricket Dashboard")
    st.markdown("*Team statistics from 2013-2025 seasons*")
    
    # Sidebar filters and navigation
    # Implementation from UI design section
    
    # Page routing
    if page == "Team Overview":
        show_team_overview(data)
    elif page == "Player Statistics":
        show_player_stats(data)
    elif page == "Venue Analysis":
        show_venue_analysis(data)
    elif page == "Submit Feedback":
        show_feedback_form()

if __name__ == "__main__":
    main()
```

### Key Features Implementation

**Player Statistics Page**:
```python
def show_player_stats(data):
    st.header("Player Statistics")
    
    # Player selection with filtering
    filtered_players = get_filtered_players(data, min_games, selected_seasons)
    selected_player = st.selectbox("Select Player", filtered_players)
    
    # Display statistics
    player_data = data["batting"][data["batting"]["player_name"] == selected_player]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Runs", player_data["runs"].sum())
    with col2:
        st.metric("Innings", len(player_data))
    with col3:
        st.metric("Average", round(player_data["runs"].mean(), 2))
    
    # Visualization
    fig = px.bar(player_data, x="Season", y="runs", 
                title=f"{selected_player}'s Runs by Season")
    st.plotly_chart(fig, use_container_width=True)
```

**Feedback Collection System**:
```python
def show_feedback_form():
    st.header("Team Feedback")
    
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        feedback_type = st.selectbox("Type", 
            ["Bug Report", "Feature Request", "General Feedback"])
        message = st.text_area("Your Message")
        
        submitted = st.form_submit_button("Submit Feedback")
        
        if submitted:
            # Save to CSV or integrate with email service
            save_feedback(name, feedback_type, message)
            st.success("Thank you for your feedback!")
```

---

## 🎯 Success Metrics

### Technical Milestones
- [ ] MVP deployed and accessible to team
- [ ] Player search functionality working
- [ ] Mobile-responsive design confirmed
- [ ] Data loading under 3 seconds
- [ ] Zero critical bugs in core features

### Team Engagement
- [ ] All team members can access their statistics
- [ ] Positive feedback from team members
- [ ] Regular usage by 50%+ of team
- [ ] Feature requests indicating engagement

### Portfolio Value
- [ ] Clean, professional presentation
- [ ] Documented development process
- [ ] Deployed and publicly accessible
- [ ] Technical skills clearly demonstrated

---

## 🔄 Maintenance & Updates

### Data Update Process
**Current**: Annual updates (seasons complete)  
**Future**: Could expand to match-by-match updates during active seasons

### Version Control
- GitHub repository with clear commit history
- Documentation of major feature additions
- Backup procedures for data and configuration

### Performance Monitoring
- Streamlit Cloud analytics
- User feedback integration
- Load time optimization

---

## 📝 Next Immediate Actions

1. **Environment Setup** (This Week)
   - Create new GitHub repository
   - Set up virtual environment
   - Install required packages

2. **Data Preparation** (Week 1)
   - Export clean CSV files from Excel workbooks
   - Document data dictionary
   - Create sample datasets for testing

3. **MVP Development** (Week 2)
   - Build basic app structure
   - Implement player search feature
   - Create first visualizations

4. **Testing & Iteration** (Week 3)
   - Team feedback collection
   - Mobile testing
   - Performance optimization

This consolidated plan provides a clear roadmap from initial setup through deployment, with specific technical implementations and measurable success criteria.
