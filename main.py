import requests
from send_mail import send_email
topic = "bitcoin"
api_key = "dcafa7e13c1a46f88178a3c6bd4ac2d9"
url = f"https://newsapi.org/v2/everything?"\
      f"q={topic}&"\
      "sortBy=publishedAt&"\
      "apiKey=dcafa7e13c1a46f88178a3c6bd4ac2d9&" \
      "language=es"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)