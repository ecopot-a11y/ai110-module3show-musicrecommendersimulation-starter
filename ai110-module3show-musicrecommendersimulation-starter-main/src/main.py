"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    # Load the song catalog
    songs = load_songs("data/songs.csv")

    # Default listener profile
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8
    }

    # Generate the top five recommendations
    recommendations = recommend_songs(
        user_prefs, songs, k=5
    )

    print("\n" + "=" * 55)
    print("          MUSIC RECOMMENDER SIMULATION")
    print("=" * 55)

    print(f"Songs in catalog: {len(songs)}")
    print("Favorite genre: pop")
    print("Favorite mood: happy")
    print("Target energy: 0.80")

    print("\nTOP 5 RECOMMENDATIONS")
    print("-" * 55)

    for rank, (song, score, explanation) in enumerate(
        recommendations, start=1
    ):
        print(f"\n{rank}. {song['title']}")
        print(f"   Final Score: {score:.2f} / 4.00")
        print(f"   Reasons: {explanation}")

    print("\n" + "=" * 55)


if __name__ == "__main__":
    main()