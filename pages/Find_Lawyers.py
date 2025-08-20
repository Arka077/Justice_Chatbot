import streamlit as st
import urllib.parse
from utils.lawyers import get_current_location, find_lawyers_nearby
import modules.video_chat as video_chat  # ✅ Import the module

st.title("📍 Locate Nearby Lawyers and Start Video Chat")

# Sidebar (if any)
# render_sidebar()

# Create two columns for location methods
st.markdown("### 🌍 Choose Your Location Method:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**🌐 Auto-Detect (IP-based)**")
    if st.button("📡 Auto-Detect Location", use_container_width=True):
        with st.spinner("🌐 Detecting your location..."):
            location = get_current_location()
            if location:
                st.success(f"📍 Detected: {location}")
                st.session_state['detected_location'] = location
            else:
                st.error("❌ Could not detect location")

with col2:
    st.markdown("**✏️ Manual Entry**")
    manual_location = st.text_input("Enter location:", placeholder="e.g., Delhi, India", label_visibility="collapsed")
    if st.button("🔍 Search Here", use_container_width=True) and manual_location.strip():
        st.session_state['detected_location'] = manual_location.strip()

# Initialize session state
if "lawyer_results" not in st.session_state:
    st.session_state.lawyer_results = None

if "detected_location" not in st.session_state:
    st.session_state.detected_location = None

if "show_video_chat" not in st.session_state:
    st.session_state.show_video_chat = False

# Show video chat page if flagged
if st.session_state.show_video_chat:
    st.markdown("---")
    video_chat.run()
    st.stop()  # Prevents rest of page from rendering

# Search for lawyers when location is set
if st.session_state.detected_location:
    st.markdown("---")
    location = st.session_state.detected_location

    st.info(f"📍 **Selected Location:** {location}")

    if st.button("🔍 **Find Lawyers Near Me**", type="primary", use_container_width=True):
        lawyers = find_lawyers_nearby(location)
        if lawyers:
            st.session_state.lawyer_results = lawyers
            st.success(f"✅ Found {len(lawyers)} lawyers nearby!")
        else:
            st.warning("⚠️ No lawyers found in this area. Try a different location.")
            st.session_state.lawyer_results = []

# Display results
if st.session_state.lawyer_results:
    st.markdown("---")
    st.subheader(f"👨‍⚖️ Found {len(st.session_state.lawyer_results)} Lawyers")

    for i, lawyer in enumerate(st.session_state.lawyer_results[:10], 1):  # Show top 10
        name = lawyer["name"]
        address = lawyer["address"]
        phone = lawyer.get("phone", "N/A")
        rating = lawyer.get("rating", "N/A")
        reviews = lawyer.get("reviews", "N/A")
        website = lawyer.get("website", "N/A")
        category = lawyer.get("category", "Legal Services")
        opening_hours = lawyer.get("opening_hours", "Hours not available")
        maps_url = lawyer.get("url", "")

        with st.expander(f"🏛️ {i}. {name} ⭐ {rating}", expanded=(i <= 3)):
            col1, col2 = st.columns([4, 1])

            with col1:
                st.markdown(f"""
                **📋 Category:** {category}  
                **📍 Address:** {address}  
                **📞 Phone:** {phone}  
                **⭐ Rating:** {rating} ({reviews} reviews)  
                **🕐 Hours:** {opening_hours}
                """)
                if website != "N/A" and website:
                    st.markdown(f"**🌐 Website:** [Visit Website]({website})")
                if maps_url:
                    st.markdown(f"**🗺️ [View on Google Maps]({maps_url})**")

            with col2:
                st.markdown("### Actions")
                if st.button(f"📹 Start Video Chat", key=f"chat_{i}"):
                    st.session_state['selected_lawyer'] = {
                        'name': name,
                        'address': address,
                        'phone': phone,
                        'rating': rating,
                        'category': category
                    }
                    st.session_state['show_video_chat'] = True
                    st.rerun()
                if phone != "N/A":
                    st.markdown(f"**📞 [Call Now](tel:{phone})**")
                st.button(f"✉️ Send Email", key=f"email_{i}", help="Email feature coming soon")

        st.markdown("---")
