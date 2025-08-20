# utils/lawyers.py
import requests
import time
import streamlit as st

# Apify configuration
API_TOKEN = 'apify_api_hfDnQ6vMXRVKipdfz8n3Z0j7YBRB3Z3IVwkX'
ACTOR_ID = 'compass~google-maps-extractor'

def get_current_location():
    """
    Get user's current location using multiple methods
    """
    try:
        # Method 1: Try ipinfo.io (more accurate than ipapi.co)
        response = requests.get('https://ipinfo.io/json', timeout=10)
        if response.status_code == 200:
            data = response.json()
            city = data.get('city', '')
            region = data.get('region', '')
            country = data.get('country', '')
            
            if city and region:
                return f"{city}, {region}, {country}"
            elif city:
                return f"{city}, {country}"
        
        # Method 2: Fallback to ipapi.co
        response = requests.get('https://ipapi.co/json/', timeout=10)
        if response.status_code == 200:
            data = response.json()
            city = data.get('city', '')
            region = data.get('region', '')
            country = data.get('country_name', '')
            
            if city and region:
                return f"{city}, {region}, {country}"
            elif city:
                return f"{city}, {country}"
        
        # Method 3: Try another service
        response = requests.get('http://ip-api.com/json/', timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                city = data.get('city', '')
                region = data.get('regionName', '')
                country = data.get('country', '')
                
                if city and region:
                    return f"{city}, {region}, {country}"
                elif city:
                    return f"{city}, {country}"
        
        return None
    except Exception as e:
        st.error(f"Error getting location: {str(e)}")
        return None

def find_lawyers_nearby(location, max_results=10):
    """
    Find lawyers near the given location using Apify Google Maps scraper
    """
    try:
        # Start the Apify actor run
        url = f"https://api.apify.com/v2/acts/{ACTOR_ID}/runs?token={API_TOKEN}"
        
        payload = {
            "searchStringsArray": ["lawyers", "advocates", "legal services"],
            "locationQuery": location,
            "maxCrawledPlacesPerSearch": max_results,
            "language": "en"
        }
        
        with st.spinner("🔍 Searching for lawyers nearby..."):
            response = requests.post(url, json=payload)
            
            if response.status_code == 201:
                run_data = response.json()
                run_id = run_data['data']['id']
                
                # Wait for the run to complete
                status_url = f"https://api.apify.com/v2/acts/{ACTOR_ID}/runs/{run_id}?token={API_TOKEN}"
                
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                max_wait_time = 120  # 2 minutes max wait
                wait_time = 0
                
                while wait_time < max_wait_time:
                    status_response = requests.get(status_url)
                    status_data = status_response.json()
                    status = status_data['data']['status']
                    
                    status_text.text(f"Status: {status}")
                    progress_bar.progress(min(wait_time / max_wait_time, 0.9))
                    
                    if status in ['SUCCEEDED', 'FAILED', 'ABORTED', 'TIMED-OUT']:
                        break
                        
                    time.sleep(3)
                    wait_time += 3
                
                progress_bar.progress(1.0)
                status_text.empty()
                progress_bar.empty()
                
                if status == 'SUCCEEDED':
                    # Get the results
                    dataset_id = status_data['data']['defaultDatasetId']
                    results_url = f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={API_TOKEN}"
                    
                    results_response = requests.get(results_url)
                    if results_response.status_code == 200:
                        raw_results = results_response.json()
                        
                        # Process and format the results
                        lawyers = []
                        for result in raw_results:
                            lawyer = {
                                "name": result.get('title', 'Unknown Lawyer'),
                                "address": result.get('address', 'Address not available'),
                                "phone": result.get('phone', 'N/A'),
                                "rating": result.get('totalScore', 'N/A'),
                                "reviews": result.get('reviewsCount', 'N/A'),
                                "website": result.get('website', 'N/A'),
                                "category": result.get('categoryName', 'Legal Services'),
                                "url": result.get('url', ''),
                                "place_id": result.get('placeId', ''),
                                "opening_hours": format_opening_hours(result.get('openingHours', [])),
                                "neighborhood": result.get('neighborhood', 'N/A'),
                                "city": result.get('city', 'N/A'),
                                "state": result.get('state', 'N/A'),
                                "postal_code": result.get('postalCode', 'N/A'),
                                "permanently_closed": result.get('permanentlyClosed', False)
                            }
                            
                            # Skip permanently closed places
                            if not lawyer["permanently_closed"]:
                                lawyers.append(lawyer)
                        
                        return lawyers
                    else:
                        st.error("Failed to fetch results from dataset")
                        return []
                else:
                    st.error(f"Scraping failed with status: {status}")
                    return []
            else:
                st.error(f"Failed to start scraping: {response.status_code}")
                return []
                
    except Exception as e:
        st.error(f"Error finding lawyers: {str(e)}")
        return []

def format_opening_hours(hours_data):
    """
    Format opening hours data into a readable string
    """
    if not hours_data:
        return "Hours not available"
    
    try:
        formatted_hours = []
        for day_info in hours_data:
            day = day_info.get('day', '')
            hours = day_info.get('hours', '')
            if day and hours:
                formatted_hours.append(f"{day}: {hours}")
        
        return "; ".join(formatted_hours) if formatted_hours else "Hours not available"
    except:
        return "Hours not available"