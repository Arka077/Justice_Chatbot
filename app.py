import streamlit as st
import urllib.parse
import streamlit.components.v1 as components

st.set_page_config(page_title="DOJ Legal Portal", layout="wide")
st.title("⚖️ Department of Justice - Legal Services Portal")

query_params = st.query_params
if "video_chat" in query_params:
    lawyer_name = query_params["video_chat"]
    st.title(f"🎥 Video Chat with {lawyer_name}")
    room_name = urllib.parse.quote(f"doj_legal_{lawyer_name}")
    components.iframe(f"https://meet.jit.si/{room_name}", height=500, width=700)
    st.markdown("[🔙 Back to Home](./)")
    st.stop()

# Home Page Navigation
st.markdown("## 🏠 Welcome to the DOJ Legal Portal")
st.markdown("Choose one of the services below to proceed:")

col1, col2 = st.columns(2)
with col1:
    if st.button("📍 Find Lawyers"):
        st.switch_page("pages/find_lawyers.py")
    st.caption("Locate nearby lawyers and connect via video call.")

    if st.button("🧾 Track a Case"):
        st.switch_page("pages/track_case.py")
    st.caption("Track the status of your legal case using e-Courts API.")

with col2:
    
    #if st.button("📄 Summarize Legal Document"):
    #    st.switch_page("pages/summarize.py")
    #st.caption("Upload legal PDFs and get concise summaries.")
    

    if st.button("🤖 Legal Chatbot"):
        st.switch_page("pages/legal_chatbot.py")
    st.caption("Ask legal questions and get AI-powered responses.")
