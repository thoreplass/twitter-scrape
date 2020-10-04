TRACK_TERMS = ["trump", "biden", "donald trump", "joe biden"]
CONNECTION_STRING = "sqlite:///tweets.db"
CSV_NAME = "tweets.csv"
TABLE_NAME = "election"

try:
    from private import TWITTER_KEY, TWITTER_SECRET, TWITTER_APP_KEY, TWITTER_APP_SECRET
except Exception:
    pass