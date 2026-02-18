"""
Currently:
- can search and play a song 
- can pause/resume playback
- can skip to next or previous song
- can add a song to the queue 
- can show what's currently playing

Later:
- add volume control
- add show queue
- add more search options (like search by artist, album, playlist, etc.)
- add 3 results for each search instead of just 1 for more accurate searching
- add lyrics display using a lyrics API
- add recommendations based on user's listening history
- add analysis to suggest songs based on user's mood or time of day
"""

# Import necessary libraries
import os 
import spotipy                          # Spotify API client
from spotipy.oauth2 import SpotifyOAuth # Handles Spotify authentication
from dotenv import load_dotenv          # Loads environment variables from .env file

# Load environment variables from .env file
load_dotenv()

# Creates spotify client
# Note: requires SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI env variables set
def spotify_client():
    # Check for required .env variables before attempting authentication
    if not os.getenv("SPOTIPY_CLIENT_ID"):
        print("Error: SPOTIPY_CLIENT_ID not found in environment variables.")
        return None
    if not os.getenv("SPOTIPY_CLIENT_SECRET"):
        print("Error: SPOTIPY_CLIENT_SECRET not found in environment variables.")
        return None
    if not os.getenv("SPOTIPY_REDIRECT_URI"):
        print("Error: SPOTIPY_REDIRECT_URI not found in environment variables.")
        return None

    # Define the scope of permissions we need
    scope = "user-modify-playback-state user-read-playback-state" 
    
    # Attempt to create the Spotify client with authentication
    try:
        # SpotifyOAuth automatically looks for the env variables
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope)) 
        return sp 
    except Exception as e: # Catch any exceptions during authentication
        print(f"Connection Error: {e}")
        return None

# Returns unique device id for spotify playback
def get_device_id(sp): # sp is the spotify client instance
    # Check for devices
    try:
        devices = sp.devices()
        if not devices['devices']: # No devices found
            return None
        
        # Return the first active device (priority 1), otherwise return the first available device
        for d in devices['devices']:
            if d['is_active']: # If this device is active, return its ID immediately
                return d['id']
        
        # Return the first device if no active devices are found
        return devices['devices'][0]['id']
    except Exception as e:
        print(f"Error finding device: {e}") 
        return None

# Functions to handle music commands
# Function to search and play a song based on user input 
def play_song(sp, device_id):
    # Prompt user for song or artist name
    query = input("What song or artist do you want to play? ")
    if not query: return

    print(f"Searching for '{query}'...")
    try:
        # Search based on track or artist for 1 result (track type)
        results = sp.search(q=query, limit=1, type='track')
        
        # If we found a track, play it on the specified device
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            track_uri = track['uri']
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            
            print(f"Playing: {track_name} by {artist_name}")
            sp.start_playback(device_id=device_id, uris=[track_uri])
        else:
            print("Song not found") # If no tracks were found matching the query
    except Exception as e:
        print(f"Error playing song: {e}")

# Function to add a song to the queue based on user input
def add_queue(sp, device_id):
    # Prompt user for song or artist name to add to queue
    query = input("What song to add to queue? ")
    if not query: return
    
    # Search for the track 
    print(f"Searching for '{query}'...")
    results = sp.search(q=query, limit=1, type='track')
    
    # If we found a track, add it to the queue on the specified device
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        print(f"Added to queue: {track['name']}")
        sp.add_to_queue(uri=track['uri'], device_id=device_id)
    else:
        print("Song not found")

# Plays music from spotify
def music ():
    # Try to connect to Spotify
    print("\nConnecting to Spotify...")
    sp = spotify_client()
    if not sp:
        print("Failed to connect. Exiting music mode.")
        return

    # Get the device ID once at the start
    device_id = get_device_id(sp)
    if not device_id:
        print("No active Spotify device found")
        print("Please open Spotify and try again")
        return

    print("Spotify Connected & Device Found!") # Connection success

    # Music Menu Loop
    while True:
        print("\nSpotify Menu:")
        print("1. Play a song")
        print("2. Pause / Resume")
        print("3. Next Song")
        print("4. Previous Song")
        print("5. Add to Queue")
        print("6. What's Playing Now?")
        print("7. Exit Music Mode")
        
        choice = input("Select an option: ").strip()

        try:
            # Handle user choices for music commands
            if choice == '1':
                play_song(sp, device_id)
            
            elif choice == '2':
                # Check current status to toggle
                current = sp.current_playback() 
                if current and current['is_playing']: # means music is currently playing, so we pause it
                    sp.pause_playback(device_id=device_id)
                    print("Paused")
                else:
                    sp.start_playback(device_id=device_id)
                    print("Resumed")
            
            elif choice == '3':
                sp.next_track(device_id=device_id) # Skip to next track
                print("Skipped")
            
            elif choice == '4':
                sp.previous_track(device_id=device_id) # Play previous track
                sp.start_playback(device_id=device_id) # Previous tracks needs to be started manually
                print("Previous track")
            
            elif choice == '5':
                add_queue(sp, device_id)
                
            elif choice == '6':
                current = sp.current_playback() 
                # Check if something is currently playing and print the track info
                if current and current['item']:
                    print(f"Now Playing: {current['item']['name']} by {current['item']['artists'][0]['name']}")
                else:
                    print("Nothing is playing right now")
            
            elif choice == '7':
                print("Exiting Music Menu...")
                break
                
            else:
                print("Invalid choice")
                
        # Debugging
        except spotipy.exceptions.SpotifyException as e:
            print(f"Spotify Error: {e}")
            # Sometimes devices go to sleep, so we try to refresh the ID if an error occurs
            device_id = get_device_id(sp)

# For testing this file directly
if __name__ == "__main__":
    music()