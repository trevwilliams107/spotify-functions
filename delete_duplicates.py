from __future__ import print_function
import random

#client id/secrets
from config import client

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
        print("usage (copy this and replace 'your_username' with your spotify username and 'playlist_name' with the exact name of the playlist you want to clean): python3 delete_duplicates.py your_username playlist_name")
        sys.exit()

    if len(sys.argv) > 1:
        playlist_name = sys.argv[2]
    else:
        print("please enter the name of the playlist you want duplicate songs deleted from")
        print("usage (copy this and replace 'playlist_name' with the name of the playlist you want to clean): python3 user_playlists.py username playlist_name")
        sys.exit()

scopes = 'playlist-modify-private,playlist-modify-public,playlist-read-private,playlist-read-collaborative,user-read-private,user-library-modify,user-library-read'
token = util.prompt_for_user_token(username,
                           scope=scopes,
                           client_id=client['spotipy']['client_id'],
                           client_secret=client['spotipy']['client_secret'],
                           redirect_uri='https://localhost:8000')

song_dic = {}
count = 1

def add_tracks(tracks, count):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        uri = track['uri']
        if uri in song_dic:
            song_dic[uri][0] += 1
            song_dic[uri][1].append(count)
        else:
            song_dic[uri] = [1, []]

        count += 1
    return count

if token:
    sp = spotipy.Spotify(auth=token)
    user = sp.current_user()
    playlists = sp.current_user_playlists()
    playlist_dic = {}
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            playlist_dic[playlist['name']] = playlist['id']
    if playlist_name not in playlist_dic:
        print('This playlist could not be found.')
        print('Make sure you enter the playlist exactly how it is spelled on your spotify account (case sensitive) and that you entered a playlist that you own.')
        sys.exit()
    playlist_id = playlist_dic[playlist_name]

    results = sp.playlist(playlist_id)
    tracks = results['tracks']
    count = add_tracks(tracks, 0)
    while tracks['next']:
        tracks = sp.next(tracks)
        count = add_tracks(tracks, count)
    remove = []

    for uri in song_dic:
        num = song_dic[uri][0]
        if num == 1:
            continue
        dic = {'uri' : uri, 'positions' : song_dic[uri][1]}
        remove.append(dic)
    sp.user_playlist_remove_specific_occurrences_of_tracks(username, playlist_id, remove, snapshot_id=None)
