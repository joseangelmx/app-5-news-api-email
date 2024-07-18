import requests
from send_mail import send_email
api_key = "dcafa7e13c1a46f88178a3c6bd4ac2d9"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "sortBy=publishedAt&apiKey="\
    "dcafa7e13c1a46f88178a3c6bd4ac2d9"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"
body = body.encode("utf-8")
send_email(body)