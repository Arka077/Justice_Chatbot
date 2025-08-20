import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

def run():
    # --- Get selected lawyer from session ---
    lawyer = st.session_state.get("selected_lawyer", None)

    if not lawyer:
        st.error("🚫 **Access Denied**: This page can only be accessed through the lawyer finder.")
        st.markdown("### Please use the proper navigation:")
        st.info("👆 Go to **Find Lawyers** page and click the **'📹 Start Video Chat'** button next to a lawyer's profile.")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔍 **Go to Find Lawyers**", type="primary", use_container_width=True):
                st.session_state.show_video_chat = False
                st.experimental_rerun()
        return

    # --- Lawyer Info ---
    lawyer_name = lawyer['name']
    address = lawyer['address']
    phone = lawyer['phone']
    rating = lawyer['rating']
    category = lawyer['category']

    # --- Page title ---
    st.title("📹 Video Chat with Legal Professional")
    st.markdown("---")

    # --- Header Section ---
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### 👨‍⚖️ {lawyer_name}")
        st.caption("Legal Professional • Live Consultation Room")

    with col2:
        if st.button("🏠 Back to Search"):
            st.session_state.show_video_chat = False
            st.rerun()


    st.markdown("---")

    # --- Jitsi Video Chat Embed ---
    st.markdown("### 📹 Live Video Consultation")

    room_id = f"LegalCall_{urllib.parse.quote(lawyer_name)}"
    jitsi_url = f"https://meet.jit.si/{room_id}#userInfo.displayName='Client'"

    components.html(f"""
        <iframe 
            src="{jitsi_url}"
            style="height: 700px; width: 100%; border: 0px;"
            allow="camera; microphone; fullscreen; display-capture"
        ></iframe>
    """, height=700)

    st.info("✅ You are now in a live video consultation room powered by [Jitsi Meet](https://meet.jit.si/).")
