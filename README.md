# spotify-functions

This repository currently supports 3 features: Data export to a Google Sheet, artist playlist creation and duplicate song deletion. 

For all of these make sure to install spotipy, googleapis and random



How to run the Data Export feature:

This feature will write every song in every playlist you have to a google sheet. One sheet is made for each playlist you have. It contains data such as artist popularity, release date, etc. There is also a count of how many times a certain song has appeared in all of your playlists and a count of how many times a certain artist has appeared in your playlists.

First, you must make a google sheet document to put the data. In the code, change the spreadsheet id to your own spreadsheet. There are comments to direct you to where it should go.

Then, in terminal cd into where playlist_data.py is. Then run the command:

playlist_data.py username

where username is your spotify username.
The application should direct you to confirm that you will allow the application to make changes to your spotify and google accounts. The google application is not verified, so it will give you a warning when trying to navigate to the confirmation page. The spotify confirmation process requires you to copy and paste 2 URLs, which will be opened through localhost.

Warning: If run more than once, an error will occur. You must either delete the sheets on the google sheet you were using or make a new google sheet and put it in the code.

How to run artist playlist creation:

This feature creates a new playlist for an artist of your choosing that contains all of the songs that artist has released and is available on spotify.

First, in terminal, cd into where artist_playlist.py is located. Then, run the command:

aritst_playlist.py username artist_name

username = your spotify username 
artist_name = the name of the artist you want to make a playlist for

Warning: running this function more than once using the same artist will create extra playlists with the same songs and titles.

How to run duplicate song deletion:

This feature deletes all duplicate songs in a playlist (ie if a playlist has 2 instances of a song, after running this file it will only have 1). The songs deleted are the ones closest to the end.

First, in terminal, cd into where delete_duplicates.py is located. Then, run the command:

delete_duplicates.py username playlist_name

username = your spotify username
playlist_name = name of playlist you want to clean.

Warning: playlist_name must match exactly the name of the playlist you want to clean. The changes made by this file cannot be undone. 








To do:
- Create a csv for each playlist, add each song, keeping order, create another csv which counts the appearances of each song in a playlist. Could potentially make this a google doc. This is for future data analysis
  -potential data project: examine an artist's most popular songs in different countries
- Create function that makes a playlist, given a list of artists, add all of that artist's songs into the playlist
- Given a list of artists, make a playlist with the top 5 songs of that artist 
- Delete duplicate songs from a playlist
