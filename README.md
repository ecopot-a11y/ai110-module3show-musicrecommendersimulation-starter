# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

I conducted a weight shift experiment to determine how sensitive my recommendation system was to changes in the scoring algorithm.

In the original formula, genre contributed 2 points, mood contributed 1 point, and energy similarity contributed up to 1 point. For the experiment, I reduced the genre weight to 1 point and doubled the energy weight to 2 points. Mood remained at 1 point, and the maximum possible score remained 4.00.

After running the same five user profiles, I discovered that the first-place recommendations and top-five ranking orders did not change. However, their numerical scores changed.

For example, Sunrise City decreased from 3.92 to 3.84 for High-Energy Pop, while Library Rain remained at a perfect 4.00 for Chill Lofi. Gym Hero remained the top recommendation for Conflicting Preferences, decreasing slightly from 2.97 to 2.94.

The most surprising result occurred with the Unfamiliar Genre profile. Midnight Coding's score increased from 0.92 to 1.84 even though it still did not match the requested classical genre or mysterious mood. Its score increased simply because energy similarity received more weight.

This experiment demonstrated that changing scoring weights can make recommendations look stronger or weaker numerically without necessarily improving their relevance. Although the scores changed, the recommendations remained in the same order for all five profiles.

I concluded that the experimental weight shift did not demonstrate a clear improvement in recommendation accuracy. A larger and more diverse song catalog, along with actual listener feedback, would be needed to determine whether the new weights are more effective.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



