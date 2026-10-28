# 🎧 Model Card: VibeFinder 1.0

## 1. Model Name

VibeFinder 1.0 — Music Recommender Simulation

## 2. Goal / Task 

VibeFinder suggests five songs based on a listener's favorite genre, preferred mood, and target energy level. It is a classroom demonstration of a simple rule-based simulation, not a trained machine-learning model. 

## 3. Intended Use and Non-Intended Use

It is intended for learning, testing scoring rules, and explaining why songs are ranked. It should not be used to predict a person's real musical taste, make commercial playlist decisions, or evaluate people. It assumes the listener can describe their preferences using the available categories.

## 4. Algorithm Summary

The system reads a song catalog and compares each song with the listener's preferences. A matching genre earns **2 points**. A matching mood earns **1 point**. A song can earn **up to 1 point** when its energy is close to the requested level. The highest possible score is **4 points**. The system sorts songs by score and shows the top five with short explanations. It does not learn from listening history or feedback.

## 5. Data Used

The catalog has **10 songs** in `data/songs.csv`. Each record includes an ID, title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The current scoring rule uses only genre, mood, and energy. The catalog has **three lofi songs, two pop songs, and one each** in rock, ambient, jazz, synthwave, and indie pop. It does not include classical music, and it cannot cover every listening preference. No new songs were needed for the evaluation; I changed user profiles and tested a temporary scoring adjustment.

## 6. Strengths

The system gives understandable results when matching songs are available. **Library Rain** scored **4.00** for the Chill Lofi profile because genre, mood, and energy all matched. **Storm Runner** scored **3.96** for Deep Intense Rock. Each recommendation includes a score explanation, making the ranking easy to inspect.

## 7. Limitations and Bias

The catalog is small, so some genres have more choices than others. Genre earns twice as many points as mood, which can repeatedly favor songs from the listener's preferred genre and limit variety. For the Unfamiliar Genre profile, the system recommended **Midnight Coding** with only **0.92** points because no song matched the requested classical genre or mysterious mood. The system still returns five songs even when none is a strong match. A larger catalog, adjustable weights, and a minimum match threshold could help.

## 8. Evaluation

### User Profiles Tested

I evaluated my music recommendation system using five different listener profiles to determine how changing genre, mood, and energy preferences affects the recommendations.

| User Profile | Genre | Mood | Energy | Top Recommendation | Score |
|---|---|---|---|---|---|
| High-Energy Pop | pop | happy | 0.90 | Sunrise City | 3.92 |
| Chill Lofi | lofi | chill | 0.35 | Library Rain | 4.00 |
| Deep Intense Rock | rock | intense | 0.95 | Storm Runner | 3.96 |
| Conflicting Preferences | pop | sad | 0.90 | Gym Hero | 2.97 |
| Unfamiliar Genre | classical | mysterious | 0.50 | Midnight Coding | 0.92 |

### Comparing the User Profiles

**Comparison 1: High-Energy Pop vs. Chill Lofi**

High-Energy Pop recommended "Sunrise City" first because it matches the pop genre, happy mood, and high-energy preference. Chill Lofi recommended "Library Rain" first because it matches the lofi genre, chill mood, and lower energy preference. This makes sense because someone looking for upbeat pop music would likely want a different listening experience from someone looking for relaxing study music.

**Comparison 2: High-Energy Pop vs. Deep Intense Rock**

High-Energy Pop ranked "Sunrise City" first with 3.92, while Deep Intense Rock ranked "Storm Runner" first with 3.96. Both users requested energetic music, but their genre and mood preferences were different. This demonstrates that the recommender considers more than energy alone when choosing songs.

**Comparison 3: Chill Lofi vs. Deep Intense Rock**

Chill Lofi produced a perfect match with "Library Rain," scoring 4.00. Deep Intense Rock recommended "Storm Runner" with 3.96. The recommendations changed because the first profile preferred calm, low-energy music while the second preferred intense, high-energy rock. The catalog also contains three lofi songs but only one rock song, giving the lofi listener more genre-matching options.

**Comparison 4: High-Energy Pop vs. Conflicting Preferences**

Both profiles requested pop music with a target energy of 0.90, but High-Energy Pop requested a happy mood while Conflicting Preferences requested a sad mood. "Sunrise City" ranked first for High-Energy Pop because it matched both genre and mood. "Gym Hero" ranked first for Conflicting Preferences because it matched the pop genre and had slightly closer energy, even though it did not match the requested sad mood. This demonstrates how changing just one preference can affect the rankings.

**Comparison 5: Conflicting Preferences vs. Unfamiliar Genre**

Conflicting Preferences ranked "Gym Hero" first with 2.97 because its pop genre matched the listener's preference. Unfamiliar Genre ranked "Midnight Coding" first with only 0.92 because none of the songs matched the requested classical genre or mysterious mood. This demonstrates that the system can still rank songs even when it cannot find a strong match.

### Surprising Results

One surprising result was that "Gym Hero" appeared near the top of several recommendation lists, even though it has an intense mood rather than a happy mood.

For example, "Gym Hero" ranked second for High-Energy Pop because it matched the pop genre and had energy close to 0.90. Its genre match contributed 2.0 points, while energy similarity contributed 0.97 points. This gave it a total score of 2.97 despite not matching the requested happy mood.

Another surprising result occurred with the Unfamiliar Genre profile. The system returned five recommendations even though none matched the requested genre or mood. The highest score was only 0.92.

### Accuracy and Limitations

The results generally made sense for the three normal profiles. The highest-ranked songs matched the requested genre and mood and had energy levels close to the listener's target.

However, the adversarial profiles revealed that a high ranking does not necessarily mean a song is appropriate. The algorithm gives genre twice the weight of mood, which can favor songs with the correct genre but an unsuitable mood.

The dataset also limits variety. There are three lofi songs but only one rock song, meaning some listeners have more matching options than others.

### Evaluation Conclusion

Overall, the recommender successfully changes its rankings based on user preferences and provides understandable explanations for its decisions.

The experiments showed that the system works best when the catalog contains songs matching the listener's preferred genre, mood, and energy. When those matches are unavailable, it still returns recommendations, but their quality may be poor.

Future improvements could include expanding the catalog, allowing users to adjust scoring weights, and introducing a minimum score threshold so the system can warn users when no strong recommendations are available.

### Weight Shift Experiment (Step 3)

I temporarily reduced the genre weight from **2 to 1** and increased the maximum energy weight from **1 to 2**. Mood stayed at **1**, so the maximum total remained **4**. I reran all five profiles and compared the results with the original formula.

| Profile | First-place song | Original score | Experimental score |
|---|---|---:|---:|
| High-Energy Pop | Sunrise City | 3.92 | 3.84 |
| Chill Lofi | Library Rain | 4.00 | 4.00 |
| Deep Intense Rock | Storm Runner | 3.96 | 3.92 |
| Conflicting Preferences | Gym Hero | 2.97 | 2.94 |
| Unfamiliar Genre | Midnight Coding | 0.92 | 1.84 |

The top-five order did not change for any profile, although scores changed. The biggest surprise was **Midnight Coding**, whose score doubled for the Unfamiliar Genre profile even though its genre and mood still did not match. This shows that a higher score does not always mean a better recommendation. I restored the original scoring weights after the experiment. The experiment did not show a clear improvement in recommendation quality.

## 9. Ideas for Improvement

1. Add more songs and more genres so different listeners have better choices.
2. Let listeners adjust how important genre, mood, and energy are to them.
3. Warn the listener when all scores are low instead of presenting weak matches as strong recommendations.

## 10. Personal Reflection

My biggest learning moment during this project was understanding that building a recommendation system involves more than writing an algorithm that produces scores. I learned that the decisions I make about scoring weights, data selection, and ranking rules directly affect the recommendations. For example, I gave genre twice as much weight as mood, which sometimes caused songs to rank highly even when their mood did not match the listener's preference. Testing the Conflicting Preferences and Unfamiliar Genre profiles helped me recognize that a program can work correctly from a technical standpoint while still producing recommendations that are not particularly useful.

AI tools helped me understand Python functions, organize the recommendation logic, troubleshoot issues, and think through different ways to test the system. They were especially useful for explaining scoring calculations and suggesting improvements. However, I learned that I could not simply assume an AI-generated explanation or suggested change was correct. I needed to review the code, run automated tests, examine the terminal output, and compare the actual scores against the expected results. This became particularly important during my weight-shift experiment, when I temporarily reduced the genre weight and increased the energy weight. Although the scores changed, the recommendation rankings remained the same. I restored the original weights after evaluating the results.

What surprised me most was how a relatively simple algorithm could produce results that felt personalized. VibeFinder does not use a trained machine-learning model or learn from listening history. It simply compares genre, mood, and energy preferences against a small catalog of songs. Nevertheless, when it recommended Library Rain for Chill Lofi and Storm Runner for Deep Intense Rock, the results seemed appropriate for those listeners. The experience showed me that personalization can begin with clear rules and well-defined data, although that does not mean the system truly understands someone's musical tastes.

If I continued developing this project, I would first expand the song catalog to include more genres, moods, and musical styles. Next, I would allow users to adjust how much importance they place on genre, mood, and energy instead of using fixed scoring weights. Finally, I would introduce a minimum recommendation score or warning when the system cannot find a strong match. These improvements would help make the recommendations more flexible, transparent, and useful.

Overall, this project taught me the importance of combining programming, experimentation, critical thinking, and human verification when developing AI-related systems. I now better understand that successful engineering is not just about making software run; it is also about evaluating whether its results make sense and recognizing when the system's limitations affect its usefulness.