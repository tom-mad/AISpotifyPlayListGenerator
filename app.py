import os
import pprint
import spotipy
from dotenv import load_dotenv

import AIPlaylistGenerator

# load_dotenv()

# sp = spotipy.Spotify(
#     auth_manager=spotipy.SpotifyOAuth(
#         client_id=os.getenv("SPOTIFY_CLIENT_ID"),
#         client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
#         redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
#         scope="playlist-modify-private"
#     )
# )

# current_user = sp.current_user()
# assert current_user is not None

# search_result = sp.search(q="Uptown Funk", type="track", limit=10)
# pprint.pprint(search_result["tracks"]["items"][0]["id"])

# tracks = [search_result["tracks"]["items"][0]["id"]]

# created_playlist = sp.user_playlist_create(
#     current_user["id"],
#     public=False,
#     name="TESTING PLAYLIST FUN"
# )

# sp.user_playlist_add_tracks(current_user["id"], created_playlist["id"], tracks)
class SpotfiyAPI:
    def __init__(self) -> None:
        self.ai_playlist_generator = AIPlaylistGenerator.AIPlaylistGenerator()

        load_dotenv()

        self.sp = spotipy.Spotify(
            auth_manager=spotipy.SpotifyOAuth(
                client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
                scope="playlist-modify-private"
            )
        )
        self.current_user = self.sp.current_user()

        assert self.current_user is not None
        playlist = self.ai_playlist_generator.generate_playlist("epic songs", 4)
        track_ids=[]
        for item in playlist:
            artist, song = item["artist"], item["song"]
            query = f"{song} {artist}"
            search_result = self.sp.search(q="Uptown Funk", type="track", limit=10)
            track_ids.append(tracks = [search_result["tracks"]["items"][0]["id"]])
            
        self.sp.user_playlist_add_tracks(self.current_user["id"], created_playlist["id"], track_ids)

if __name__ == "__main__":
    spotify = SpotfiyAPI()
