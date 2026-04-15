"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    """
    Main function that loads songs and generates personalized music recommendations.
    Loads a collection of songs from a CSV file and creates recommendations based on
    a user preference profile. The user preferences include favorite genre (hip-hop),
    favorite mood (chill), target energy level (0.6), and acoustic preference (True).
    Retrieves the top 5 song recommendations that match the user profile and displays
    each recommendation with its score and explanation for why it was recommended.
    Returns:
        None
    """
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.8, "likes_acoustic": True}
    
    user_prefs_2 = {"favorite_genre": "hip-hop", "favorite_mood": "chill", "target_energy": 0.6, "likes_acoustic": False}
    
    # Hip-hop users were served more low-energy songs on a consistent basis. This user was more driven by the target_energy I believe than the actual genre.
    
    user_prefs_3 = {"favorite_genre": "blues", "favorite_mood": "relaxed", "target_energy": 0.5, "likes_acoustic": True}
    
    # With the blues genre being more niche, a user with the blues preference will be recommended things more surrouding their mood preference.
    
    user_prefs_4 = {"favorite_genre": "indie pop", "favorite_mood": "nostalgic", "target_energy": 0.7, "likes_acoustic": True}
    
    # The indie-pop user was served 5 songs all with a differet genre. An indie-pop user will prefer songs that more match their energy and acoustic preferences.
    
    user_prefs_5 = {"favorite_genre": "country", "favorite_mood": "happy", "target_energy": 0.6, "likes_acoustic": False}
    
    # Country users are going to be more emerged in the music with feelings of nostalgia, happy, relaxed and even romantic!

    # Adversarial / edge case profiles — designed to expose potential weaknesses in the recommender.

    # Case mismatch: "Pop"/"Happy" won't match stored "pop"/"happy" — genre+mood score silently = 0
    user_prefs_6 = {"favorite_genre": "Pop", "favorite_mood": "Happy", "target_energy": 0.8, "likes_acoustic": True}

    # Energy above valid range: energy proximity formula produces negative contributions for all songs
    user_prefs_7 = {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 2.5, "likes_acoustic": False}

    # Nonexistent genre + mood: 0 pts for both — energy alone decides ranking, no warning shown
    user_prefs_8 = {"favorite_genre": "reggae", "favorite_mood": "furious", "target_energy": 0.5, "likes_acoustic": False}

    # Contradictory preferences: metal genre match (+4) but likes_acoustic=True penalizes low-acoustic metal songs
    user_prefs_9 = {"favorite_genre": "metal", "favorite_mood": "intense", "target_energy": 0.95, "likes_acoustic": True}

    # Negative energy: abs(song_energy - (-1.0)) always > 1.0, so energy always subtracts from score
    user_prefs_10 = {"favorite_genre": "lofi", "favorite_mood": "chill", "target_energy": -1.0, "likes_acoustic": True}

    # Whitespace in strings: " pop" != "pop" — silent mismatch, genre score = 0
    user_prefs_11 = {"favorite_genre": " pop", "favorite_mood": "happy ", "target_energy": 0.8, "likes_acoustic": True}

    # Integer instead of bool for likes_acoustic: Python duck-typing may handle 0/1, but no validation exists
    user_prefs_12 = {"favorite_genre": "jazz", "favorite_mood": "chill", "target_energy": 0.4, "likes_acoustic": 0}

    # No genre/mood match + energy=0.5: many songs cluster near 0.5, ranking decided by sort stability
    user_prefs_13 = {"favorite_genre": "zzz_unknown", "favorite_moodfavorite_mood": "zzz_unknown", "target_energy": 0.5, "likes_acoustic": False}

    # The proposed user preference profile tests the recommender with:

    # - **favorite_genre**: "hip-hop" - tests genre-based filtering
    # - **favorite_mood**: "chill" - tests mood matching
    # - **target_energy**: 0.6 - tests medium energy level preference
    # - **likes_acoustic**: True - tests acoustic instrumentation preference

    # This creates a balanced test case for a user who wants relaxed hip-hop with acoustic elements, which should help validate that the recommender correctly weighs multiple preference attributes when scoring and ranking songs.

    recommendations = recommend_songs(user_prefs_5, songs, k=5)

    print("\n" + "=" * 44)
    print("   TOP MUSIC RECOMMENDATIONS")
    print("=" * 44)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} — {song['artist']}")
        print(f"    Score : {score:.2f} / 10.00")
        print(f"    Genre : {song['genre']}  |  Mood: {song['mood']}")
        print("    Why   :")
        for reason in explanation.split(", "):
            print(f"            • {reason}")
        print("-" * 44)


if __name__ == "__main__":
    main()
