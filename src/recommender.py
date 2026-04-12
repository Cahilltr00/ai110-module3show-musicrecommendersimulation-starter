from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs.csv and return a list of dicts with numeric fields cast to float."""
    import csv
    row_count = 0
    
    
    
    numeric_fields = {"id", "energy", "tempo_bpm", "valence", "danceability", "acousticness"}
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for field in numeric_fields:
                row[field] = float(row[field])
            songs.append(row)
            
        row_count = sum(1 for row in songs)
        
    print(f"Loading songs: {row_count}...")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return (score, list of reasons)."""
    score = 0.0
    reasons = []

    # Genre match — 4.0 pts (binary)
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 4.0
        reasons.append("genre match (+4.0)")

    # Mood match — 3.0 pts (binary)
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 3.0
        reasons.append("mood match (+3.0)")

    # Energy proximity — up to 2.0 pts (continuous)
    energy_points = 2.0 * (1 - abs(song["energy"] - user_prefs["target_energy"]))
    score += energy_points
    reasons.append(f"energy proximity (+{energy_points:.2f})")

    # Acoustic preference — up to 1.0 pts (continuous)
    if user_prefs["likes_acoustic"]:
        acoustic_points = 1.0 * song["acousticness"]
    else:
        acoustic_points = 1.0 * (1 - song["acousticness"])
    score += acoustic_points
    reasons.append(f"acoustic preference (+{acoustic_points:.2f})")

    return score, reasons
    

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs, sort by score descending, and return the top k as (song, score, explanation)."""
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    ranked = sorted(scored, key=lambda x: x[1], reverse=True)
    return [
        (song, score, ", ".join(reasons))
        for song, score, reasons in ranked[:k]
    ]
