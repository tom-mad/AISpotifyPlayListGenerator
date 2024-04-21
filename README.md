# AISpotifyPlaylistGenerator

## Overview
AISpotifyPlaylistGenerator is a project aimed at generating Spotify playlists using AI technology. It utilizes the OpenAI API along with Spotify API to create personalized playlists based on user prompts.

## Dependencies
To use AISpotifyPlaylistGenerator, you need to have a `.env` file in the project directory with the following data:
- `OPENAI_API_KEY`: Your OpenAI API key
- `SPOTIFY_CLIENT_ID`: Your Spotify Client ID
- `SPOTIFY_CLIENT_SECRET`: Your Spotify Client Secret
- `SPOTIFY_REDIRECT_URI`: Your Spotify Redirect URI

## Usage
To use AISpotifyPlaylistGenerator, execute the `app.py` Python file. It's a command-line utility with the following options:

        python app.py [-h] [-p PROMPT] [-n NUM_SONGS] [-t PLAYLIST_TITLE]

- `-p PROMPT`: The prompt to describe the playlist.
- `-n NUM_SONGS`: The number of songs to add to the playlist (default is 5).
- `-t PLAYLIST_TITLE`: Generated playlist title (default is "TESTING PLAYLIST FUN").

Example usage:

        python app.py -p "Relaxing evening" -n 10 -t "Chill Vibes"

This will generate a playlist titled "Chill Vibes" with 10 songs based on the prompt "Relaxing evening".
