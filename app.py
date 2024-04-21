import os
import spotipy
import argparse
from dotenv import load_dotenv

import AIPlaylistGenerator

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

    def generate_spotify_playlist(self, prompt, num_of_songs, playlist_title):
        playlist = self.ai_playlist_generator.generate_playlist(prompt, num_of_songs)
        track_ids=[]
        for item in playlist:
            artist, song = item["artist"], item["song"]
            query = f"{song} {artist}"
            search_result = self.sp.search(q=query, type="track", limit=10)
            track_ids.append(search_result["tracks"]["items"][0]["id"])
            
        created_playlist = self.sp.user_playlist_create(
            self.current_user["id"],
            public=False,
            name=playlist_title
        )
        self.sp.user_playlist_add_tracks(self.current_user["id"], created_playlist["id"], track_ids)

def main():
    parser = argparse.ArgumentParser(description="Simple command line song utility")
    parser.add_argument("-p", type=str, help="The prompt to describe the playlist")
    parser.add_argument("-n", type=int, default=5, help="The number of songs to add to the playlist")
    parser.add_argument("-t", type=str, default="TESTING PLAYLIST FUN", help="Generated playlist title")
    args = parser.parse_args()

    spotify = SpotfiyAPI()
    spotify.generate_spotify_playlist(args.p, args.n, args.t)

if __name__ == "__main__":
    main()
