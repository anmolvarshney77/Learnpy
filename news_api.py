import json
import requests
def get_news():
    url = "https://newsapi.org/v2/everything?q=stock&apiKey=8c4c0c8294754004b34e0df87706e51c"
    response = requests.get(url, timeout=1)
    if response.status_code == 200:     
        data = response.json()
        articles = data.get("articles", [])
        news_list = []
        for article in articles:
            title = article.get("title")
            description = article.get("description")
            url = article.get("url")
            news_list.append({"title": title, "description": description, "url": url})
        return news_list
    return None             
print(get_news())
def jprint(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))