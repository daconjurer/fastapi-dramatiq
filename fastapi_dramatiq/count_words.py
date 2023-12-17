import dramatiq
import requests


@dramatiq.actor
def count_words(url: str):
    response = requests.get(url)
    count = len(response.text.split(" "))
    print(f"There are {count} words at {url!r}.")
