import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
    else:
        posts = response.json()

        print("First 5 post titles:")

        for post in posts[:5]:
            title = post.get("title", "No title found")
            print(f"- {title}")

except requests.exceptions.RequestException as error:
    print(f"Something went wrong with the request: {error}")