def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    result = []
    space_required = 0
    if (songs[0][2] > max_size):
        return result
    else:
        space_required += songs[0][2]
        result += songs[0][0],

    sorted_songs = sorted([item for item in songs[1:]], key= lambda song_size: song_size[2])

    while sorted_songs:
        if sorted_songs[0][2] <= max_size - space_required:
            space_required += sorted_songs[0][2]
            result += sorted_songs.pop(0)[0],
        else:
            break
    return result

print(song_playlist([('z', 0.1, 0.1), ('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 1))


