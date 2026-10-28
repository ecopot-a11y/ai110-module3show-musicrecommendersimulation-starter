"""
Run the music recommender with diverse user profiles.
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    # Load the existing song catalog
    songs = load_songs("data/songs.csv")

    # Normal and adversarial test profiles
    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.90
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95
        },
        "Conflicting Preferences": {
            "genre": "pop",
            "mood": "sad",
            "energy": 0.90
        },
        "Unfamiliar Genre": {
            "genre": "classical",
            "mood": "mysterious",
            "energy": 0.50
        }
    }

    print("=" * 55)
    print("       MUSIC RECOMMENDER - SYSTEM EVALUATION")
    print("=" * 55)
    print(f"Songs in catalog: {len(songs)}")

    # Evaluate each user profile
    for profile_name, user_prefs in profiles.items():

        print("\n" + "=" * 55)
        print(f"PROFILE: {profile_name}")
        print("=" * 55)

        print(f"Favorite genre: {user_prefs['genre']}")
        print(f"Favorite mood: {user_prefs['mood']}")
        print(f"Target energy: {user_prefs['energy']:.2f}")

        recommendations = recommend_songs(
            user_prefs, songs, k=5
        )

        print("\nTOP 5 RECOMMENDATIONS")
        print("-" * 55)

        for rank, (song, score, explanation) in enumerate(
            recommendations, start=1
        ):
            print(f"\n{rank}. {song['title']}")
            print(f"   Final Score: {score:.2f} / 4.00")
            print(f"   Reasons: {explanation}")

    print("\n" + "=" * 55)
    print("             EVALUATION COMPLETE")
    print("=" * 55)


if __name__ == "__main__":
    main()