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
    """Load songs from a CSV file and convert numeric fields."""

    import csv

    songs = []

    with open(csv_path, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Score one song based on genre, mood, and energy similarity.

    Returns:
        (total_score, reasons)
    """

    score = 0.0
    reasons = []

    # Get the user's preferences.
    # Support both the Phase 2 profile and the starter main.py profile.
    favorite_genre = user_prefs.get(
        "favorite_genre", user_prefs.get("genre", "")
    )
    favorite_mood = user_prefs.get(
        "favorite_mood", user_prefs.get("mood", "")
    )
    target_energy = float(
        user_prefs.get("target_energy", user_prefs.get("energy", 0.5))
    )

    # Rule 1: Genre match (+2.0)
    if song["genre"].lower() == favorite_genre.lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Rule 2: Mood match (+1.0)
    if song["mood"].lower() == favorite_mood.lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Rule 3: Energy similarity (up to +1.0)
    song_energy = float(song["energy"])

    energy_points = max(
        0.0, 1.0 - abs(song_energy - target_energy)
    )

    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    return score, reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Rank songs by preference score and return the top k with explanations."""
    
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)

        scored_songs.append(
            (song, score, ", ".join(reasons))
        )

    ranked_songs = sorted(
        scored_songs,
        key=lambda item: item[1],
        reverse=True
    )

    return ranked_songs[:max(0, k)]

