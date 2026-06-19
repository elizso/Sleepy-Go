import streamlit as st 

corners = {


"3-4 approach":

[
"Enclose",
"Pincer",
"Attach"
],


"4-4 approach":

[
"Extend",
"Approach",
"Ignore"
]

}

selected = st.selectbox(
    "Select a corner move", 
    list(corners.keys())
)

for i in corners[selected]:
    st.write(i)

