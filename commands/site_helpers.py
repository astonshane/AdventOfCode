import os
import requests

# returns your session token
#   Search order:
#       1. AOC_SESSION_TOKEN env var
#       2. .aoc_session_token file
def get_session_token():
    token = os.getenv("AOC_SESSION_TOKEN")
    if token:
        return token.strip()

    token_path = '.aoc_session_token'
    if os.path.exists(token_path):
        with open(token_path) as f:
            token = f.readline().strip()

    return token

# fetches your actual input from the AOC servers
def fetch_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_token = get_session_token()
    if session_token is None:
        print("No AOC Session Token found - puzzle input not fetched")
        return
    # print(session_token)
    response = requests.get(url, cookies={
        "session": session_token
    })
    response.raise_for_status()
    return response.text

# contains star counts
def fetch_events_page():
    url = "https://adventofcode.com/events"
    session_token = get_session_token()
    if session_token is None:
        print("No AOC Session Token found - stats not fetched")
        return
    response = requests.get(url, cookies={
        "session": session_token
    })
    response.raise_for_status()
    return response.text