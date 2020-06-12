from __future__ import print_function
import random

#spotipy imports
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

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


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage (copy this and replace 'your_username' with your spotify username and 'playlist_uri' with the URI of the playlist you want to clean): python3 delete_duplicates.py your_username playlist_uri")
        sys.exit()

    if len(sys.argv) > 1:
        playlist_name = sys.argv[2]
    else:
        print("please enter the uri of the playlist you want duplicate songs deleted from")
        print("usage (copy this and replace 'playlist_uri' with the uri of the playlist you want to clean): python3 user_playlists.py username playlist_uri")
        sys.exit()

scopes = 'playlist-modify-private,playlist-modify-public,playlist-read-private,playlist-read-collaborative,user-read-private,user-library-modify,user-library-read'
token = util.prompt_for_user_token(username,
                           scope=scopes,
                           client_id='20624df21d7c41288ee2b990bcd14050',
                           client_secret='c3e9c3e71deb4d09ba2ef2441c305cc8',
                           redirect_uri='https://localhost:8000')

song_dic = {}

if token:
    sp = spotipy.Spotify(auth=token)
    user = sp.current_user()
    print()
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








    print()
