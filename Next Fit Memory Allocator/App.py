import streamlit as st
import time

# Initialize session state for progress if not already initialized
if "progress" not in st.session_state:
    st.session_state.progress = 0  # Start with 0% progress

if "progress_text" not in st.session_state:
    st.session_state.progress_text = "Backtesting (0%)"

# Function to simulate progress updates
def run_backtest():
    for i in range(1, 101):  # Simulate progress from 1% to 100%
        time.sleep(0.1)  # Simulate work being done
        st.session_state.progress = i  # Update progress
        st.session_state.progress_text = f"Backtesting ({i}%)"
        progress_placeholder.progress(st.session_state.progress, text=st.session_state.progress_text)

# Main UI
st.title("Real-Time Progress Bar in Streamlit")

# Create a placeholder for the progress bar
progress_placeholder = st.empty()

# Show the progress bar with the current state
progress_placeholder.progress(
    st.session_state.progress,
    text=st.session_state.progress_text
)

# Start button
if st.button("Start Backtest"):
    run_backtest()

# Reset button
if st.button("Reset"):
    st.session_state.progress = 0
    st.session_state.progress_text = "Backtesting (0%)"
    progress_placeholder.progress(
        st.session_state.progress,
        text=st.session_state.progress_text
    )
