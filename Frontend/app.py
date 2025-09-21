import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:5000"

def main():
    st.title("Song Translator: English → Tamil")

    # Get songs list from backend
    try:
        songs = requests.get(f"{BACKEND_URL}/songs").json()["songs"]
    except Exception as e:
        st.error("Failed to fetch songs from backend.")
        return

    song_choice = st.selectbox("Select a song", songs)

    if st.button("Translate to Tamil"):
        try:
            response = requests.post(f"{BACKEND_URL}/lyrics", json={"song": song_choice})
            data = response.json()
            tamil_lyric = data.get("tamil", "")
            
            if tamil_lyric:
                st.subheader("Tamil Lyrics:")
                st.write(tamil_lyric)
            else:
                st.warning("No lyrics found for this song.")
        except Exception as e:
            st.error("Error fetching Tamil lyrics from backend.")

if __name__ == "__main__":
    main()
