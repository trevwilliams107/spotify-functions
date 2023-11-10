import json

artist_dic = {}
song_dic = {}
total_time = 0
total_time_filtered = 0
for i in range(7):
    file_string = f'MyData/StreamingHistory{i}.json'
    f = open(file_string)
    song_list = json.load(f)
    # for song in song_json:
    for song in song_list:
        total_time += song['msPlayed']
        if song['msPlayed'] < 60000:
            continue
        total_time_filtered += song['msPlayed']
        artist_name = song['artistName']
        song_name = song['trackName']
        combination_name = song_name + ", " + artist_name
        if artist_name not in artist_dic:
            artist_dic[artist_name] = 1
        else:
            artist_dic[artist_name] += 1

        if combination_name not in song_dic:
            song_dic[combination_name] = 1
        else:
            song_dic[combination_name] += 1

sorted_artists_by_plays = sorted(artist_dic.items(), key=lambda x:x[1], reverse=True)
sorted_songs_by_plays = sorted(song_dic.items(), key=lambda x:x[1], reverse=True)

song_file = open("song_stats_2022.txt", "a")
song_file.write("song, artist         num_plays\n")

for combination in sorted_songs_by_plays:
    song_file.write(combination[0] + "          " +  str(combination[1]) + "\n")


artist_file = open("artist_stats_2022.txt", "a")
artist_file.write("artist         num_plays\n")
for artist in sorted_artists_by_plays:
    artist_file.write(artist[0] + "          " +  str(artist[1]) + "\n")

time_file = open("time_listened_stats_2022.txt", "a")
time_file.write("Total time listened (minutes)\n")
time_file.write(str(total_time/60000))
time_file.write("Time listened where listen time >= 1 min (minutes)\n")
time_file.write(str(total_time_filtered/60000))




