from __future__ import print_function
import random

#spotify imports
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

#GOOGLE IMPORTS AND TOKEN STUFF

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pprint import pprint
from googleapiclient import discovery

google_cid = '709831756208-hc395jqnaeq4gmrhgdp27243v38pbe2f.apps.googleusercontent.com'
google_csec = '-W_7SzJWXQbGE1zzKhA5wsdm'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1NbsNJd2C2bJMwI8mRA0UPQVq5PNhnh-qxDtJbfYFu3E'
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T','U', 'V', 'W']



def createSheet(sheet_title):
    x = len(sheet_title)
    if 'r' in sheet_title:
        x += 3
    if 's' in sheet_title:
        x += 2
    if 'e' in sheet_title:
        x += 2
    if 'l' in sheet_title:
        x += 2
    if 't' in sheet_title:
        x += 2
    if 'n' in sheet_title:
        x += 2
    random.seed(x)

    # TODO: Change placeholder below to generate authentication credentials. See
    # https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
    #
    # Authorize using one of the following scopes:
    #     'https://www.googleapis.com/auth/drive'
    #     'https://www.googleapis.com/auth/drive.file'
    #     'https://www.googleapis.com/auth/spreadsheets'

    creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = discovery.build('sheets', 'v4', credentials=creds)



    # The spreadsheet to apply the updates to.
    spreadsheet_id = SPREADSHEET_ID  # TODO: Update placeholder value.

    batch_update_spreadsheet_request_body = {
        # A list of updates to apply to the spreadsheet.
        # Requests will be applied in the order they are specified.
        # If any request is not valid, no requests will be applied.
        "requests": [
        {
          "addSheet": {
            "properties": {
              "title": sheet_title,
              "gridProperties": {
                "rowCount": 600,
                "columnCount": 16
              },
              "tabColor": {
                "red": random.random(),
                "green": random.random(),
                "blue": random.random()
              }
            }
          }
        }
      ]  # TODO: Update placeholder value.

        # TODO: Add desired entries to the request body.
    }

    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_spreadsheet_request_body)
    response = request.execute()


def appendSong(lst, playlist_name):

    creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = discovery.build('sheets', 'v4', credentials=creds)

    spreadsheet_id = SPREADSHEET_ID  # TODO: Update placeholder value.

    # The A1 notation of a range to search for a logical table of data.
    # Values will be appended after the last row of the table.
    print(lst)
    print()
    secondLetter = ALPHABET[len(lst[0]) - 1]
    print(secondLetter)
    range_ = playlist_name + '!A1:' + secondLetter + '1'  # TODO: Update placeholder value.

    # How the input data should be interpreted.
    value_input_option = 'RAW'  # TODO: Update placeholder value.

    # How the input data should be inserted.
    insert_data_option = 'INSERT_ROWS'  # TODO: Update placeholder value.

    value_range_body = {
        # TODO: Add desired entries to the request body.
        'values' :  lst
        }

    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
    response = request.execute()





util.prompt_for_user_token('trevwilliams107',
                           scope='playlist-modify-private,playlist-modify-public',
                           client_id='20624df21d7c41288ee2b990bcd14050',
                           client_secret='c3e9c3e71deb4d09ba2ef2441c305cc8',
                           redirect_uri='https://localhost:8000')

song_artist_lst = []
playlist_dic = {}
artist_dic = {}

def show_tracks(tracks, playlist_name):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print(track['name'])

        if (track['artists'][0]['name'], track['name']) in playlist_dic:
            playlist_dic[(track['artists'][0]['name'], track['name'])] += 1
        else:
            playlist_dic[(track['artists'][0]['name'], track['name'])] = 1

        if track['artists'][0]['name'] in artist_dic:
            artist_dic[track['artists'][0]['name']] += 1
        else:
            artist_dic[track['artists'][0]['name']] = 1
        genres = ''
        for genre in sp.artist(track['artists'][0]['id'])['genres']:
            genres += genre + ', '
        song_artist_lst.append([track['artists'][0]['name'], track['name'], track['album']['name'], track['album']['release_date'], track['popularity'], convertMillisMin(track['duration_ms']), convertMillisSec(track['duration_ms']), track['album']['total_tracks'], track['album']['type'], playlist_name, track['id'], track['album']['id'], track['artists'][0]['id'], genres, track['explicit'], sp.artist(track['artists'][0]['id'])['popularity']])



def convertMillisMin(milli):
    seconds = str(round(milli//1000)%60)
    minutes = str((milli//(1000*60))%60)
    if int(seconds) < 10:
        seconds = '0' + seconds
    return minutes + ':' + seconds

def convertMillisSec(milli):
    seconds = str(round(milli//1000))
    return seconds



if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage (copy this): python3 user_playlists.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username,
                               scope='playlist-modify-private,playlist-modify-public,playlist-read-private',
                               client_id='20624df21d7c41288ee2b990bcd14050',
                               client_secret='c3e9c3e71deb4d09ba2ef2441c305cc8',
                               redirect_uri='https://localhost:8000')

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.current_user_playlists()
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print(playlist['name'])
                song_artist_lst = []
                playlist_name = playlist['name']
                pn = ''
                for i in playlist_name:
                    if i == '!':
                        pn += '1'
                    elif i == ':':
                        pn += ';'
                    else:
                        pn += i


                createSheet(pn)
                # print ('  total tracks', playlist['tracks']['total'])
                results = sp.playlist(playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks, playlist_name)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks, playlist_name)
                appendSong([['Artist', 'Song Title', 'Album', 'Release Date', 'popularity', 'duration in minutes','duration in seconds', '# of tracks on album',	'album type', 'playlist name', 'song id', 'album id', 'artist id', 'genres', 'explicit', 'artist_popularity']], pn)
                appendSong(song_artist_lst, pn)

        createSheet('Song Counts')
        appendSong([['Artist', 'Song Title', 'Number of appearances in playlists']], 'Song Counts')
        songLst = []
        for key in playlist_dic.keys():
            count = playlist_dic[(key[0], key[1])]
            songLst.append([key[0], key[1], count])
        appendSong(songLst, 'Song Counts')

        createSheet('Artist Counts')
        artistLst = []
        appendSong([['Artist', 'Number of appearances in playlists']], 'Artist Counts')
        for key in artist_dic.keys():
            count = artist_dic[key]
            artistLst.append([key, count])
        appendSong(artistLst, 'Artist Counts')


    else:
        print("Can't get token for", username)









# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
#
# for album in albums:
#     print(album['name'])
