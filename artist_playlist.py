from __future__ import print_function
import random

#spotipy imports
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials




if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage (copy this): python3 user_playlists.py [username]")
        sys.exit()

util.prompt_for_user_token('trevwilliams107',
                           scope='playlist-modify-private,playlist-modify-public',
                           client_id='20624df21d7c41288ee2b990bcd14050',
                           client_secret='c3e9c3e71deb4d09ba2ef2441c305cc8',
                           redirect_uri='https://localhost:8000')

if token:
    sp = spotipy.Spotify(auth=token)
    user_playlist_create(user, name, public=True, description='')
