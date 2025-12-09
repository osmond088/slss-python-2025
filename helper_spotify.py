# Helper for searching through Spotify results
import csv


def songs_by_artist(file_path: str, artist: str) -> list[list[str]]:
    """Searches through given file and returns a list of songs from given artist."""
    artist_col = 2
    songs = []
    # open the file
    with open(file_path) as f:
        # get rid of the header row
        _ = f.readline()
        # create a reader object
        r = csv.reader(f)
        # go through reader line by line
        for info in r:
            # if the current artist is "Kendrick"
            if info[artist_col] == artist:
                songs.append(info)
    return songs


def songs_by_track_name(filepath: str, search_term: str) -> list[list[str]]:
    """Get all songs that contain a search term in their track name

    Params:
        filepath - path to the CSV file
        search_term - term to search for in track names

    Returns:
        list of songs with the search term in their name
    """
    track_name_col = 0
    songs = []
    # open the file
    with open(filepath) as f:
        # get rid of the header row
        _ = f.readline()
        # create a reader object
        r = csv.reader(f)
        # go through reader line by line
        for info in r:
            # if the search term is in the track name (case-insensitive)
            if search_term.lower() in info[track_name_col].lower():
                songs.append(info)
    return songs


def string_to_num(s: str) -> int:
    """Converts a string number with commas in it to an integer. (e.g. "1,223,222" -> 1223222)"""
    return int(s.replace(",", ""))
