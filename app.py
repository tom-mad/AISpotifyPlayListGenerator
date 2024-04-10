import os
import spotipy

from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI")
    )
)

current_user = sp.current_user()
print(current_user)
