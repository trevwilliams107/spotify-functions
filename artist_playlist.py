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
        print("usage (copy this and replace 'your_username' with your spotify username and 'artist' with the artist you want to make an album for. Please put the artist name in quotes): python3 user_playlists.py your_username artist")
        sys.exit()

    if len(sys.argv) > 1:
        artist = sys.argv[2]
    else:
        print("please enter the artist you would like to make a playlist for")
        print("usage (copy this and replace 'artist' with the artist you want to make a playlist for. Please put the artist name in quotes): python3 user_playlists.py username artist")
        sys.exit()

scopes = 'playlist-modify-private,playlist-modify-public,playlist-read-private,playlist-read-collaborative,user-read-private,user-library-modify,user-library-read'
token = util.prompt_for_user_token(username,
                           scope=scopes,
                           client_id=client['spotipy']['client_id'],
                           client_secret=client['spotipy']['client_secret'],
                           redirect_uri='https://localhost:8000')

if token:
    sp = spotipy.Spotify(auth=token)
    user = sp.current_user()
    artist_id = sp.search(q='artist:' + artist, type='artist', limit=1)['artists']['items'][0]['id']
    results = sp.artist_albums(artist_id, limit=50)
    artist_name = sp.artist(artist_id)['name']
    name = 'All ' + artist_name + ' Songs'
    albums = results['items']

    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
        
    count = 1
    big_list = []
    song_list = []
    name_list = []
    for album in albums:
        album_id = album['id']
        songs = sp.album_tracks(album_id, limit=40)['items']
        for song in songs:
            artists = song['artists']
            all_artists_ids = set()
            for artist in artists:
                all_artists_ids.add(artist['id'])
            if artist_id in all_artists_ids:
                name_list.append(song['name'])
                song_list.append(song['uri'])
                count += 1
                if count >= 100:
                    big_list.append(song_list)
                    song_list = []
                    count = 1
    big_list.append(song_list)
    sp.user_playlist_create(user['id'], name, public=True, description='')
    playlist_id = sp.current_user_playlists(limit=1, offset=0)['items'][0]['id']
    for lst in big_list:
        sp.user_playlist_add_tracks(username, playlist_id, lst, position=None)
