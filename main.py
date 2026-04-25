import requests
import json
import os
from datetime import datetime, timedelta

BASE_URL = "https://newsapi.org/v2/everything"


def fetch_news(query, api_key):
    date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    url = f"{BASE_URL}?q={query}&from={date}&sortBy=publishedAt&apiKey={api_key}"

    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching news:", e)
        return None

    if data.get("status") != "ok":
        print("❌ API Error:", data)
        return None

    return data.get("articles", [])


def display_news(articles):
    if not articles:
        print("⚠️ No articles found.")
        return

    print(f"\n📰 Found {len(articles)} articles. Showing top {min(10, len(articles))}...\n")

    for article in articles[:10]:
        print("=" * 60)
        print(f"Title      : {article.get('title', 'No title')}")
        print(f"Source     : {article['source']['name']}")
        print(f"Published  : {article.get('publishedAt', 'Unknown')}")
        print(f"About      : {article.get('description', 'No description')}\n")


def save_to_file(data):
    with open("news_results.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("\n💾 All articles saved to 'news_results.json'")


def main():
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        print("❌ Please set your NEWS_API_KEY environment variable.")
        print("Example (Windows) - set NEWS_API_KEY=your_api_key\nIn powershell use - $env:NEWS_API_KEY=your_api_key")
        print("Example (Linux/Mac) - export NEWS_API_KEY=your_api_key")
        return

    query = input("🔍 Which topic of news are you interested in: ")

    articles = fetch_news(query, api_key)

    if articles is None:
        return

    display_news(articles)
    save_to_file(articles)


if __name__ == "__main__":
    main()