import json



num_files = 18
artist_dic = {}
song_dic = {}
red_velvet_dic = {}
total_time = 0
total_time_filtered = 0

for i in range(num_files):
    file_string = f'AllTimeData/endsong_{i}.json'
    f = open(file_string)
    song_list = json.load(f)

    for song in song_list:
        total_time += song['ms_played']
        if song['ms_played'] < 60000:
            continue
        total_time_filtered += song['ms_played']
        artist_name = song['master_metadata_album_artist_name']
        song_name = song['master_metadata_track_name']

        if artist_name is None or song_name is None:
            continue

        combination_name = song_name + ", " + artist_name

        if artist_name not in artist_dic:
            artist_dic[artist_name] = 1
        else:
            artist_dic[artist_name] += 1

        if combination_name not in song_dic:
            song_dic[combination_name] = 1
        else:
            song_dic[combination_name] += 1

        if artist_name == "Red Velvet":
            if song_name not in red_velvet_dic:
                red_velvet_dic[song_name] = 1
            else:
                red_velvet_dic[song_name] += 1

sorted_artists_by_plays = sorted(artist_dic.items(), key=lambda x:x[1], reverse=True)
sorted_songs_by_plays = sorted(song_dic.items(), key=lambda x:x[1], reverse=True)
sorted_songs_by_plays_rv = sorted(red_velvet_dic.items(), key=lambda x:x[1], reverse=True)

song_file = open("song_stats_all_time.txt", "a")
song_file.write("song, artist         num_plays\n")
for combination in sorted_songs_by_plays:
    song_file.write(combination[0] + "          " +  str(combination[1]) + "\n")


song_file = open("rv_song_stats_all_time.txt", "a")
song_file.write("song, artist         num_plays\n")
for song_name in sorted_songs_by_plays_rv:
    song_file.write(song_name[0] + "          " +  str(song_name[1]) + "\n")


artist_file = open("artist_stats_all_time.txt", "a")
artist_file.write("artist         num_plays\n")
for artist in sorted_artists_by_plays:
    artist_file.write(artist[0] + "          " +  str(artist[1]) + "\n")

time_file = open("time_listened_stats_all_time.txt", "a")
time_file.write("Total time listened (minutes)\n")
time_file.write(str(total_time/60000) + '\n')
time_file.write("Time listened where listen time >= 1 min (minutes)\n")
time_file.write(str(total_time_filtered/60000) + '\n')
