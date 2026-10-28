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
    popularity: int = 50
    release_decade: int = 2020
    detailed_mood_tags: str = ""
    instrumentalness: float = 0.0
    is_live: bool = False
    listening_context: str = ""

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
        prefs = vars(user).copy()
        return sorted(self.songs, key=lambda song: score_song(prefs, vars(song))[0], reverse=True)[:max(0, k)]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = score_song(vars(user), vars(song))
        return ", ".join(reasons)


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

            # Advanced fields are optional for compatibility with older CSV files.
            row["popularity"] = int(row.get("popularity") or 50)
            row["release_decade"] = int(row.get("release_decade") or 2020)
            row["instrumentalness"] = float(row.get("instrumentalness") or 0)
            row["is_live"] = str(row.get("is_live", "no")).lower() in ("yes", "true", "1")
            row["detailed_mood_tags"] = row.get("detailed_mood_tags", "")
            row["listening_context"] = row.get("listening_context", "")
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

    # Optional advanced preferences: each is independently scored.
    # Without these preferences, the original 0–4 score is unchanged.
    if user_prefs.get("target_popularity") is not None:
        target = max(0, min(100, float(user_prefs["target_popularity"])))
        points = max(0.0, 0.5 * (1 - abs(float(song.get("popularity", 50)) - target) / 100))
        score += points
        reasons.append(f"popularity similarity (+{points:.2f})")

    if user_prefs.get("preferred_decade") is not None:
        if int(song.get("release_decade", 2020)) == int(user_prefs["preferred_decade"]):
            score += 0.5
            reasons.append("release decade match (+0.50)")

    if user_prefs.get("detailed_mood_tag"):
        tags = {tag.strip().lower() for tag in str(song.get("detailed_mood_tags", "")).split("|")}
        if str(user_prefs["detailed_mood_tag"]).strip().lower() in tags:
            score += 0.5
            reasons.append("detailed mood match (+0.50)")

    if user_prefs.get("target_instrumentalness") is not None:
        target = max(0.0, min(1.0, float(user_prefs["target_instrumentalness"])))
        actual = float(song.get("instrumentalness", 0))
        points = max(0.0, 0.5 * (1 - abs(actual - target)))
        score += points
        reasons.append(f"instrumentalness similarity (+{points:.2f})")

    if user_prefs.get("prefers_live") is not None:
        live = song.get("is_live", False)
        if isinstance(live, str):
            live = live.strip().lower() in ("yes", "true", "1")
        if bool(live) == bool(user_prefs["prefers_live"]):
            score += 0.5
            reasons.append("live recording preference match (+0.50)")

    if user_prefs.get("listening_context"):
        if str(song.get("listening_context", "")).lower() == str(user_prefs["listening_context"]).lower():
            score += 0.5
            reasons.append("listening context match (+0.50)")

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

