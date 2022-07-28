import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.markdown(
"""
This web app is maintained by ACE,  
Remote sensing and Geographic Information Science (GIS) researchers group from Geomatics Engineering, Institute Technology of Sepuluh Nopember. 
"""
)

col1, col2, col3= st.columns(3)

with col2:
    st.header("About Us")
    #st.image("https://static.streamlit.io/examples/cat.jpg")

st.markdown(
""" 
"""
)

coll1, coll2, coll3= st.columns(3)

with coll1:
    st.subheader("Member 1")
    #st.image("https://static.streamlit.io/examples/cat.jpg")

with coll3:
    st.subheader("Member 2")
    st.markdown(
        """
        Megivareza Putri Hanansyah
        03311940000041
        """
    )
    st.text('varezamegi@gmail.com')
    st.text('[LinkedIn](https://www.linkedin.com/in/megivareza-putri-hanansyah-b6b4b720a/)')
    st.text('[Instagram](https://instagram.com/megivareza?igshid=YmMyMTA2M2Y=)')
    st.image("https://i.postimg.cc/CLDfTLFr/Jurnalistik-Megivareza-Putri-Hanansyah-03311940000041.jpg")


st.header("batas bawah")
