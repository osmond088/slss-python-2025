# Intro to Sort
# Author: Osmond
# 4 December
import csv

import helper_spotify

# Sorting Algorithms
# We'll implement selection sort in two ways
#     * implement basic version using the example from yesterday
#     * implement sort with songs based on YouTube views in descending order


def selection_sort(l: list[int], ascending=True) -> list[int]:
    """Sorts a given list using selection sort
    Params:
        l - list of numbers to sort
        ascending - True if sorting in ascending order
    Returns:
        a sorted list
    """
    num_items = len(l)
    # starting at the beginning of the list
    for i in range(num_items):
        candidate_num = l[i]
        candidate_index = i
        # check the rest of the list
        for j in range(i + 1, num_items):
            if ascending:
                if l[j] < candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
            else:
                if l[j] > candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
        # swap the current number with the number at the
        # lowest index
        l[i], l[candidate_index] = l[candidate_index], l[i]
    return l


def sort_songs(songs: list[list[str]], col: int, ascending=True) -> list[list[str]]:
    """Sort a list of spotify songs in place

    Params:
        songs - list of songs
        col - column to sort
        ascending - will sort ascending by default

    Returns: sorted list"""
    # Use Selection Sort to sort songs
    num_songs = len(songs)

    for i in range(num_songs):
        # This value is the candidate
        # Handle empty strings by treating them as 0
        candidate_str = songs[i][col]
        candidate_val = (
            helper_spotify.string_to_num(candidate_str) if candidate_str.strip() else 0
        )
        candidate_idx = i

        # Check the rest of the list
        for j in range(i + 1, num_songs):
            this_song_str = songs[j][col]
            this_songs_val = (
                helper_spotify.string_to_num(this_song_str)
                if this_song_str.strip()
                else 0
            )
            if ascending:
                if this_songs_val < candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j
            else:
                if this_songs_val > candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j

        # Swap the candidate with the current index
        songs[i], songs[candidate_idx] = songs[candidate_idx], songs[i]

    return songs


if __name__ == "__main__":
    # Test basic selection sort
    sorted_list = selection_sort([1, 43, 55, -11, 100, 34])
    print(sorted_list)
    sorted_list = selection_sort([1, 43, 55, -11, 100, 34], False)
    print(sorted_list)
    print()

    # Task 1: Find songs by Ed Sheeran and print name and YouTube Views
    print("Task 1: Ed Sheeran Songs")
    print("-" * 50)
    ed_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")
    for song in ed_songs:
        print(f"{song[0]}\t{song[11]}")
    print()

    # Task 2: Sort Ed Sheeran songs by YouTube Views in ascending order
    print("Task 2: Ed Sheeran Songs Sorted by YouTube Views (Ascending)")
    print("-" * 50)
    sorted_ed_songs = sort_songs(ed_songs, 11, ascending=True)
    for song in sorted_ed_songs:
        print(f"{song[0]}\t{song[11]}")
    print()

    # Task 3: Sort Ed Sheeran songs by TikTok Views in descending order
    print("Task 3: Ed Sheeran Songs Sorted by TikTok Views (Descending)")
    print("-" * 50)
    # Column 13 is TikTok Views
    sorted_tiktok_songs = sort_songs(ed_songs, 13, ascending=False)
    for song in sorted_tiktok_songs:
        print(f"{song[0]}\t{song[13]}")
    print()

    # Task 4: Find all songs with "the" in the track name
    print("Task 4: Songs with 'the' in track name")
    print("-" * 50)
    songs_with_the = helper_spotify.songs_by_track_name("data/spotify2024.csv", "the")
    for song in songs_with_the:
        print(f"{song[0]}")
    print(f"Total songs with 'the': {len(songs_with_the)}")
    print()

    # Task 5: Sort songs with "the" by TikTok views
    print("Task 5: Songs with 'the' Sorted by TikTok Views")
    print("-" * 50)
    sorted_the_songs = sort_songs(songs_with_the, 13, ascending=False)
    for song in sorted_the_songs:
        print(f"{song[0]}\t{song[13]}")
