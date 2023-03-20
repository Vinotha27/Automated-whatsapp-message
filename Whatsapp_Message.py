import streamlit as st
pip install pywhatkit
import pywhatkit
wm=pywhatkit.sendwhatmsg("+917010683112","This is a automate whatsapp Message,Your pending payment of Rs.17,000,If you already paid the due ignore this message",11,8)
st.write(wm)
