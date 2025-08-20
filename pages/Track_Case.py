import streamlit as st
from utils.ecourt_api import get_case_status
#from shared_sidebar import render_sidebar

st.title("🧾 Track Your Legal Case")

case_number = st.text_input("🔎 Enter Case Number (e.g., SC/1234/2022)")

if st.button("Track Case"):
    case_info = get_case_status(case_number)
    
    if case_info:
        st.subheader("📋 Case Details")
        st.markdown(f"**Case Number:** {case_info.get('Case Number', 'N/A')}")
        st.markdown(f"**Status:** {case_info.get('Status', 'N/A')}")
        st.markdown(f"**Court:** {case_info.get('Court', 'N/A')}")
        st.markdown(f"**Parties Involved:** {case_info.get('Parties', 'N/A')}")
        st.markdown(f"**Latest Update:** {case_info.get('Latest Update', 'N/A')}")
    else:
        st.warning("No details found for the given case number.")

