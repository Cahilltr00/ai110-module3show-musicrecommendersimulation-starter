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
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    user_prefs = {"favorite_genre": "hip-hop", "favorite_mood": "chill", "target_energy": 0.6, "likes_acoustic": True}
    # The proposed user preference profile tests the recommender with:

    # - **favorite_genre**: "hip-hop" - tests genre-based filtering
    # - **favorite_mood**: "chill" - tests mood matching
    # - **target_energy**: 0.6 - tests medium energy level preference
    # - **likes_acoustic**: True - tests acoustic instrumentation preference

    # This creates a balanced test case for a user who wants relaxed hip-hop with acoustic elements, which should help validate that the recommender correctly weighs multiple preference attributes when scoring and ranking songs.

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
