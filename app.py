import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff


st.set_page_config(page_title="Olympic Data Analysis", page_icon=":bar_chart:",layout="wide")
st.title(" :bar_chart: Olympic Data Analyzer")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

df = pd.read_csv('data/athlete_events.csv')
region_df = pd.read_csv('data/noc_regions.csv')

df = preprocessor.preprocess(df, region_df)

user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete wise Analysis')
)

st.dataframe(df, use_container_width=True)