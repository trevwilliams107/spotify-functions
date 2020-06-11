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
        print("usage (copy this): python3 user_playlists.py your_username artist")
        sys.exit()

    if len(sys.argv) > 1:
        artist = sys.argv[2]
    else:
        print("please enter the artist you would like to make a playlist for")
        print("usage (copy this): python3 user_playlists.py your_username artist")
        sys.exit()

scopes = 'playlist-modify-private,playlist-modify-public,playlist-read-private,playlist-read-collaborative,user-read-private,user-library-modify,user-library-read'
token = util.prompt_for_user_token('trevwilliams107',
                           scope=scopes,
                           client_id='20624df21d7c41288ee2b990bcd14050',
                           client_secret='c3e9c3e71deb4d09ba2ef2441c305cc8',
                           redirect_uri='https://localhost:8000')

if token:
    sp = spotipy.Spotify(auth=token)
    user = sp.current_user()
    name = 'All ' + artist + ' Songs'
    artist_id = sp.search(q='artist:' + artist, type='artist', limit=1)['artists']['items'][0]['id']
    results = sp.artist_albums(artist_id, limit=20)
    albums = results['items']
    sp.user_playlist_create(user['id'], name, public=True, description='')

    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    count = 1
    big_list = []
    song_list = []
    for album in albums:
        album_id = album['id']
        songs = sp.album_tracks(album_id, limit=40)['items']
        for song in songs:
            song_list.append(song['uri'])
            count += 1
            if count >= 100:
                big_list.append(song_list)
                song_list = []
                count = 1

    playlist_id = sp.current_user_playlists(limit=1, offset=0)['items'][0]['id']
    for lst in big_list:
        sp.user_playlist_add_tracks(username, playlist_id, lst, position=None)

        # print()
        # print()
        # print(songs)

        # for song in songs:
        #     print(song)


















    #
