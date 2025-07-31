import streamlit as st
import pandas as pd
from datetime import datetime
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_hostory

if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False
    
