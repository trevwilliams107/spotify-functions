from __future__ import print_function
import sys
import spotipy
import spotipy.util as util

scope = 'user-top-read'
username = 'trevwilliams107'

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks(limit=50, offset=0, time_range='long_term')
    for item in results['items']:
        print(item['name'])
        
else:
    print("Can't get token for", username)