import requests

api_key = "dcafa7e13c1a46f88178a3c6bd4ac2d9"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2024-06-17&sortBy=publishedAt&apiKey="\
    "dcafa7e13c1a46f88178a3c6bd4ac2d9"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])