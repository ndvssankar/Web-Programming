import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "dMiMo5UwKqB038a2d2SQ", "isbns": "9781632168146"})
print(res.json())

