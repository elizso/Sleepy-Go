import streamlit as st
from utils.recommendations import recommendation 

st.header("Mood")

brain = st.selectbox(
    "Brain Battery", 
    ["Dead", "Sleepy", "Human", "Super Saiyan"]
)

rec = recommendation(brain)

st.write(rec) 