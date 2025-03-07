import os
import requests
import schedule
import time
from itertools import cycle

# Fetch the secrets from environment variables set in GitHub Actions
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

if not BOT_TOKEN or not CHANNEL_ID:
    raise ValueError("Bot Token or Channel ID is missing. Make sure they are set as GitHub secrets.")

POSTS_FILE = "posts.txt"

# Read non-empty lines from the file and strip whitespace
with open(POSTS_FILE, "r", encoding="utf-8") as f:
    posts = [line.strip() for line in f if line.strip()]

if not posts:
    raise ValueError("The posts file is empty or contains only blank lines!")

# Create an iterator that cycles over the posts continuously
post_cycle = cycle(posts)

def send_daily_post():
    # Get the next post from the cycle
    message = next(post_cycle)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": "TEST 1",
        "parse_mode": "Markdown"  # Optional: change if you prefer HTML or plain text
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", response.text)

# Schedule the post for 09:00 AM every day

send_daily_post()
