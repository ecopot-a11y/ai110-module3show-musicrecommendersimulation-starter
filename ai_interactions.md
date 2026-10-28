# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

For Challenge 1, I used AI to help extend my existing VibeFinder 1.0 music recommendation system. My goal was to introduce at least five additional song attributes, update the scoring algorithm to consider these features, and preserve the functionality of my original recommender.

**What task did you give the agent?**

Extend the 10-song VibeFinder classroom recommender with at least five additional song attributes and make the scoring logic use them, while preserving the existing baseline results when advanced preferences are absent.

**Prompts used:**

I used the following prompts and follow-up requests to guide the AI-assisted development process.

Prompt 1 — Add Advanced Features

"Introduce 5 or more complex attributes to my music recommendation dataset that are not currently present, such as song popularity, release decade, and detailed mood tags. Update both data/songs.csv and the scoring logic in src/recommender.py so scoring accounts for the new attributes."

Prompt 2 — Preserve Existing Functionality

"Keep the original genre, mood, and energy scoring as the foundation. Make the advanced preferences optional so my existing listener profiles and recommendation scores remain unchanged when those preferences are not provided."

Prompt 3 — Generate Tests

"Create automated tests to verify that the original scoring still works, that all six advanced attributes contribute to recommendation scores, and that advanced user preferences can change song rankings."

Prompt 4 — Document the Workflow

"Document the agentic workflow in ai_interactions.md, including the AI prompts, changes generated, and manual verification notes."

**What did the agent generate or change?**

- Added six simulated fields to all ten rows in `data/songs.csv`: `popularity` (0–100), `release_decade`, `detailed_mood_tags` (pipe-separated), `instrumentalness` (0–1), `is_live` (yes/no), and `listening_context`.
- Updated `src/recommender.py` to load these fields and add up to 0.5 points each when the user supplies the corresponding optional preference: `target_popularity`, `preferred_decade`, `detailed_mood_tag`, `target_instrumentalness`, `prefers_live`, `listening_context`.
- Added explanations for the advanced score components. The maximum is 4.0 with baseline preferences and 7.0 when all six advanced preferences are provided and match perfectly.
- Kept older CSV rows and existing `Song` construction compatible by providing defaults for new fields.
- Added `tests/test_advanced.py` to verify baseline compatibility and advanced scoring.

**What did you verify or fix manually?**

Verification 1 — Automated testing

I activated my Python virtual environment and ran:

python -m pytest -v

The results showed:
test_baseline_unchanged — PASSED
test_all_six_features_affect_scoring — PASSED
test_advanced_preferences_change_ranking — PASSED
test_recommend_returns_songs_sorted_by_score — PASSED
test_explain_recommendation_returns_non_empty_string — PASSED
test_recommend_songs_ranks_highest_score_first — PASSED

Final result: 6 tests passed in 0.66 seconds.
This confirmed that the original automated tests continued to pass and that the new advanced scoring tests passed.

Verification 2 — Running the application

I then ran:

python -m src.main

The application successfully processed all 10 songs and completed the five original evaluation profiles.
The baseline High-Energy Pop recommendation remained `Sunrise City` at **3.92**.
- Verified that a profile matching all six new fields adds **3.0 points** to the same song's baseline score and includes explanatory reasons.

The AI-assisted implementation included three additional tests in tests/test_advanced.py:

test_baseline_unchanged: Verifies that the original scoring behavior remains unchanged.

test_all_six_features_affect_scoring: Verifies that the six advanced attributes contribute to scoring.

test_advanced_preferences_change_ranking: Verifies that advanced preferences can affect recommendation rankings.

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->
