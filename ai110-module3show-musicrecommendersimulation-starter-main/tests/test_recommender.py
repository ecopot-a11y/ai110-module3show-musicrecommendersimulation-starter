from src.recommender import Song, UserProfile, Recommender, recommend_songs

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_recommend_songs_ranks_highest_score_first():
    # Create a sample user profile
    user = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.90
    }

    # Put the lower-scoring song FIRST to test sorting
    songs = [
        {
            "title": "Chill Track",
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.40
        },
        {
            "title": "Rock Track",
            "genre": "rock",
            "mood": "intense",
            "energy": 0.91
        }
    ]

    # Request only the highest-scoring song
    results = recommend_songs(user, songs, k=1)

    # Verify that only one recommendation is returned
    assert len(results) == 1

    # Verify that the highest-scoring song is selected
    assert results[0][0]["title"] == "Rock Track"

    # Verify the numeric score: 2 + 1 + 0.99 = 3.99
    assert abs(results[0][1] - 3.99) < 0.0001

    # Verify that an explanation is included
    assert "genre match" in results[0][2]
