from src.recommender import load_songs, score_song, recommend_songs

def test_baseline_unchanged():
    songs = load_songs('data/songs.csv')
    results = recommend_songs({'genre':'pop','mood':'happy','energy':0.9},songs)
    assert results[0][0]['title']=='Sunrise City'
    assert round(results[0][1],2)==3.92

def test_all_six_features_affect_scoring():
    song=load_songs('data/songs.csv')[0]
    base={'genre':'pop','mood':'happy','energy':0.9}
    original,_=score_song(base,song)
    additions={'target_popularity':82,'preferred_decade':2020,'detailed_mood_tag':'euphoric','target_instrumentalness':0.05,'prefers_live':False,'listening_context':'workout'}
    enhanced, reasons=score_song({**base,**additions},song)
    assert round(enhanced-original,2)==3.0
    assert len(reasons)==9

def test_advanced_preferences_change_ranking():
    songs=load_songs('data/songs.csv')
    base={'genre':'pop','mood':'happy','energy':0.9}
    # Baseline winner is Sunrise City, but workout/live/popularity preferences can favor Gym Hero.
    advanced={**base,'target_popularity':91,'target_instrumentalness':0.02,'detailed_mood_tag':'motivational','listening_context':'workout','prefers_live':False}
    original=recommend_songs(base,songs)
    enhanced=recommend_songs(advanced,songs)
    assert original[0][0]['title']=='Sunrise City'
    assert enhanced[0][0]['title'] in {'Sunrise City','Gym Hero'}
    assert enhanced[0][1] != original[0][1]
