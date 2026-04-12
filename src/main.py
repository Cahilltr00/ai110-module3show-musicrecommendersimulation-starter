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
    user_prefs_2 = {"favorite_genre": "hip-hop", "favorite_mood": "chill", "target_energy": 0.6, "likes_acoustic": True}
    # The proposed user preference profile tests the recommender with:

    # - **favorite_genre**: "hip-hop" - tests genre-based filtering
    # - **favorite_mood**: "chill" - tests mood matching
    # - **target_energy**: 0.6 - tests medium energy level preference
    # - **likes_acoustic**: True - tests acoustic instrumentation preference

    # This creates a balanced test case for a user who wants relaxed hip-hop with acoustic elements, which should help validate that the recommender correctly weighs multiple preference attributes when scoring and ranking songs.

    recommendations = recommend_songs(user_prefs, songs, k=5)

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
