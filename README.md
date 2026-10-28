# 🎵 Music Recommender Simulation

## Project Summary

This project demonstrates a content-based music recommendation system developed in Python. The program loads a catalog of songs from a CSV file, compares each song against a user's musical preferences, and calculates a recommendation score using genre, mood, and energy similarity. It then ranks the songs and displays the top five recommendations, including numerical scores and explanations. Automated tests help verify the scoring and ranking logic.

---

## How The System Works

Real-world music recommendation platforms use listening behavior, likes, skips, and information about songs to predict what a listener may enjoy. My simplified **content-based recommender** does not track user activity. Instead, it compares a user's stated preferences with song features, calculates a score for each song, and ranks the results. I prioritize **genre, mood, and energy similarity**, so the recommendation process is transparent and easy to test.

### Song Data and User Taste Profile

The current catalog contains 10 songs in `data/songs.csv`. Each `Song` stores `id`, `title`, `artist`, `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`. The initial scoring rule uses only **genre, mood, and energy**; the other attributes are available for later improvements.

The `UserProfile` stores `favorite_genre`, `favorite_mood`, `target_energy`, and `likes_acoustic`. For this first algorithm, `likes_acoustic` is saved but does **not** affect the score.

Example user preferences:

```python
user_prefs = {
    "favorite_genre": "rock",
    "favorite_mood": "intense",
    "target_energy": 0.90,
    "likes_acoustic": False,
}
```

### Finalized Algorithm Recipe (0–4 points)

1. **Genre match:** Add **2.0 points** if the song's genre matches `favorite_genre`, otherwise add 0.
2. **Mood match:** Add **1.0 point** if the song's mood matches `favorite_mood`, otherwise add 0.
3. **Energy similarity:** Add `1.0 - abs(song.energy - target_energy)` points. Because energy values range from 0 to 1, this rewards songs closest to the desired energy, not simply the most energetic songs.
4. **Total score:** `score = 2.0 * genre_match + 1.0 * mood_match + energy_similarity`. The maximum is **4.0 points**.
5. **Ranking rule:** Score **every** song, sort the results from highest to lowest score, and return the top `k` songs (normally `k=5`). 
6. **Explanations:** For each selected song, explain which preferences matched and how close its energy is to the user's target.

Genre gets twice the weight of mood because it represents a broad musical preference, while mood may change depending on the listener's activity. Mood still matters: two rock songs may feel very different. The **scoring rule** judges a single song; the **ranking rule** compares all songs and decides which appear first.

### Data Flow (Planning Sketch)

```text
INPUT
  UserProfile: favorite genre, favorite mood, target energy
  + data/songs.csv: song catalog
        |
        v
PROCESS — FOR EACH SONG
  Check genre match (+2.0)
  Check mood match (+1.0)
  Calculate energy similarity (up to +1.0)
  Save song + score + explanation
        |
        v
RANKING
  Sort all scored songs from highest to lowest
  Select top K (usually 5)
        |
        v
OUTPUT
  Personalized song recommendations with scores and reasons
```

### Expected Biases and Limitations

The **2-point genre weight may over-prioritize familiar genres**, overlooking great songs in other genres that match the user's mood and energy. Exact genre and mood matching also ignores relationships between similar categories. A single taste profile cannot represent changing situations such as working out versus studying. The small catalog and lack of listening history, lyrics, or feedback limit personalization. I will evaluate these weaknesses by testing different profiles and comparing the rankings.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\Activate.ps1      # Windows PowerShell
   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

The music recommendation system was tested using the default listener profile:

Favorite genre: pop

Favorite mood: happy

Target energy: 0.80

Songs in catalog: 10

The program evaluates each song based on genre matching, mood matching, and energy similarity. It then ranks the songs from highest to lowest score and returns the top five recommendations.

## System Evaluation: Diverse User Profiles

To evaluate the music recommendation system, I tested five different user profiles. Three profiles represent typical musical preferences, while two adversarial profiles test the algorithm's behavior when preferences are conflicting or unavailable in the catalog.

### Test 1: High-Energy Pop

This profile represents a listener who prefers happy pop music with high energy.

```text
====================================================
PROFILE: High-Energy Pop
====================================================
Favorite genre: pop
Favorite mood: happy
Target energy: 0.90

TOP 5 RECOMMENDATIONS
----------------------------------------------------

1. Sunrise City
   Final Score: 3.92 / 4.00
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.92)

2. Gym Hero
   Final Score: 2.97 / 4.00
   Reasons: genre match (+2.0), energy similarity (+0.97)

3. Rooftop Lights
   Final Score: 1.86 / 4.00
   Reasons: mood match (+1.0), energy similarity (+0.86)

4. Storm Runner
   Final Score: 0.99 / 4.00
   Reasons: energy similarity (+0.99)

5. Night Drive Loop
   Final Score: 0.85 / 4.00
   Reasons: energy similarity (+0.85)
```

### Test 2: Chill Lofi

This profile represents a listener who prefers relaxing lofi music with low energy.

```text
====================================================
PROFILE: Chill Lofi
====================================================
Favorite genre: lofi
Favorite mood: chill
Target energy: 0.35

TOP 5 RECOMMENDATIONS
----------------------------------------------------

1. Library Rain
   Final Score: 4.00 / 4.00
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+1.00)

2. Midnight Coding
   Final Score: 3.93 / 4.00
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.93)

3. Focus Flow
   Final Score: 2.95 / 4.00
   Reasons: genre match (+2.0), energy similarity (+0.95)

4. Spacewalk Thoughts
   Final Score: 1.93 / 4.00
   Reasons: mood match (+1.0), energy similarity (+0.93)

5. Coffee Shop Stories
   Final Score: 0.98 / 4.00
   Reasons: energy similarity (+0.98)
```

### Test 3: Deep Intense Rock

This profile represents a listener who prefers intense rock music with very high energy.

```text
====================================================
PROFILE: Deep Intense Rock
====================================================
Favorite genre: rock
Favorite mood: intense
Target energy: 0.95

TOP 5 RECOMMENDATIONS
----------------------------------------------------

1. Storm Runner
   Final Score: 3.96 / 4.00
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.96)

2. Gym Hero
   Final Score: 1.98 / 4.00
   Reasons: mood match (+1.0), energy similarity (+0.98)

3. Sunrise City
   Final Score: 0.87 / 4.00
   Reasons: energy similarity (+0.87)

4. Rooftop Lights
   Final Score: 0.81 / 4.00
   Reasons: energy similarity (+0.81)

5. Night Drive Loop
   Final Score: 0.80 / 4.00
   Reasons: energy similarity (+0.80)
```

### Test 4: Conflicting Preferences (Adversarial)

This profile requests sad pop music with very high energy. It tests whether the algorithm can accommodate unusual combinations of preferences.

```text
====================================================
PROFILE: Conflicting Preferences
====================================================
Favorite genre: pop
Favorite mood: sad
Target energy: 0.90

TOP 5 RECOMMENDATIONS
----------------------------------------------------

1. Gym Hero
   Final Score: 2.97 / 4.00
   Reasons: genre match (+2.0), energy similarity (+0.97)

2. Sunrise City
   Final Score: 2.92 / 4.00
   Reasons: genre match (+2.0), energy similarity (+0.92)

3. Storm Runner
   Final Score: 0.99 / 4.00
   Reasons: energy similarity (+0.99)

4. Rooftop Lights
   Final Score: 0.86 / 4.00
   Reasons: energy similarity (+0.86)

5. Night Drive Loop
   Final Score: 0.85 / 4.00
   Reasons: energy similarity (+0.85)
```

### Test 5: Unfamiliar Genre (Adversarial)

This profile requests classical music with a mysterious mood. It tests how the system behaves when the requested categories are missing from the catalog.

```text
====================================================
PROFILE: Unfamiliar Genre
====================================================
Favorite genre: classical
Favorite mood: mysterious
Target energy: 0.50

TOP 5 RECOMMENDATIONS
----------------------------------------------------

1. Midnight Coding
   Final Score: 0.92 / 4.00
   Reasons: energy similarity (+0.92)

2. Focus Flow
   Final Score: 0.90 / 4.00
   Reasons: energy similarity (+0.90)

3. Coffee Shop Stories
   Final Score: 0.87 / 4.00
   Reasons: energy similarity (+0.87)

4. Library Rain
   Final Score: 0.85 / 4.00
   Reasons: energy similarity (+0.85)

5. Spacewalk Thoughts
   Final Score: 0.78 / 4.00
   Reasons: energy similarity (+0.78)
```

### Evaluation Findings

I tested my music recommendation system using five different user profiles, including three normal profiles and two adversarial profiles. The purpose was to determine whether the algorithm produced reasonable recommendations and identify weaknesses in its scoring logic.

**Results from Normal Profiles**

The three normal profiles produced recommendations that closely matched the requested musical preferences.

For High-Energy Pop, "Sunrise City" ranked first with a score of 3.92 out of 4.00 because it matched the preferred genre and mood and had similar energy.

For Chill Lofi, "Library Rain" received a perfect score of 4.00 because it matched all three preferences.

For Deep Intense Rock, "Storm Runner" ranked first with 3.96, demonstrating that the algorithm correctly prioritizes songs matching the requested genre and mood.

**Results from Adversarial Profiles**

The Conflicting Preferences profile requested sad pop music with high energy. However, "Gym Hero" ranked first with 2.97 even though its mood did not match. This demonstrates how the algorithm's genre weight can dominate the recommendation results.

The Unfamiliar Genre profile requested classical music with a mysterious mood. None of the recommendations matched either category. The highest-scoring song, "Midnight Coding," received only 0.92 points based entirely on energy similarity.

**Strengths**

- The scoring system is transparent and provides understandable explanations.
- Songs matching genre, mood, and energy consistently receive high scores.
- The ranking function correctly orders songs from highest to lowest score.
- The recommender handles unusual user profiles without crashing.

**Weaknesses**

- Genre receives twice the weight of mood, potentially overemphasizing genre.
- Exact matching does not recognize relationships between similar genres or moods.
- The recommender returns five songs even when none are strong matches.
- The small 10-song catalog limits recommendation variety.

**Potential Improvements**

Future improvements could include allowing users to adjust the importance of genre, mood, and energy, expanding the catalog, introducing a minimum recommendation score, and using additional song attributes such as tempo, danceability, and acousticness.

**Conclusion**

Overall, the system performs well when the song catalog contains music matching the user's preferences. However, the adversarial tests demonstrate that producing a ranked list does not necessarily mean the recommendations are appropriate. Recommendation quality depends on the scoring weights, the available songs, and how well the algorithm handles preferences that cannot be satisfied.

### Terminal Output

Run the application using:

```powershell
python -m src.main
```

Paste the complete terminal output below, inside a fenced code block:

```text
====================================================
          MUSIC RECOMMENDER SIMULATION
====================================================
Songs in catalog: 10
Favorite genre: pop
Favorite mood: happy
Target energy: 0.80

TOP 5 RECOMMENDATIONS
----------------------------------------------------

1. Sunrise City
   Final Score: 3.98 / 4.00
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)

2. Gym Hero
   Final Score: 2.87 / 4.00
   Reasons: genre match (+2.0), energy similarity (+0.87)

3. Rooftop Lights
   Final Score: 1.96 / 4.00
   Reasons: mood match (+1.0), energy similarity (+0.96)

4. Night Drive Loop
   Final Score: 0.95 / 4.00
   Reasons: energy similarity (+0.95)

5. Storm Runner
   Final Score: 0.89 / 4.00
   Reasons: energy similarity (+0.89)

====================================================
```

## Experiments You Tried

```I tested the recommendation algorithm using a user who prefers rock music, an intense mood, and an energy level of 0.90. The song "Storm Runner" received a score of 3.99 because it matched the preferred genre and mood and had nearly identical energy. In comparison, "Midnight Coding" received a score of 0.52 because it did not match the preferred genre or mood.

I also tested the ranking function by placing a lower-scoring song before a higher-scoring song in the input list. The recommender correctly selected the higher-scoring song. All three automated tests passed.
```

## Limitations and Risks

My recommendation system has several limitations. First, it relies on a small catalog, which limits the variety of recommendations. Second, genre receives twice as much weight as mood, potentially favoring familiar genres over songs that might otherwise suit the listener. Third, the system uses exact category matching and does not recognize similarities between related genres or moods.

The algorithm also does not consider listening history, user feedback, lyrics, or changes in preferences over time. These limitations could make recommendations repetitive or less personalized. Future improvements could include additional song features and a feedback mechanism.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)


Building this music recommendation system helped me understand how recommendation algorithms turn user preferences and song characteristics into numerical scores. I learned that a recommendation does not necessarily require a complex machine learning model. A straightforward scoring algorithm can produce useful results when the inputs, weights, and ranking rules are clearly defined. I also learned the importance of testing the algorithm to verify that it ranks songs correctly rather than simply returning them in their original order.

One important takeaway was that the design of the scoring algorithm directly influences which songs are recommended. By assigning more weight to genre than mood, I introduced a preference that may not reflect every listener's interests. This demonstrated how bias can enter an algorithm through design decisions, even when those decisions are not intentionally unfair. Providing explanations alongside recommendation scores makes the system more transparent and easier to evaluate.


### Interpretation

The results demonstrate that the recommendation algorithm successfully ranks songs according to the listener's preferences.

Sunrise City received the highest score of 3.98 because it matched both the preferred genre and mood, and its energy level was very close to the target of 0.80.

Gym Hero ranked second with 2.87 because it matched the preferred pop genre and had reasonably similar energy, although its mood did not match.

Rooftop Lights ranked third with 1.96 because it matched the preferred happy mood and had strong energy similarity, but did not match the preferred genre.

The remaining recommendations received points primarily for energy similarity.

These results demonstrate that the scoring algorithm prioritizes genre, then mood, while using energy similarity to distinguish between songs. The system also provides transparent explanations so users can understand why each song was recommended.

