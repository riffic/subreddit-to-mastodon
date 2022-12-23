import feedparser
import mastodon

# Set up Mastodon API client
mastodon_client = mastodon.Mastodon(
    client_id="client_id.txt",
    client_secret="client_secret.txt",
    access_token="access_token.txt",
    api_base_url="https://mastodon.social"
)

# Set up feedparser
feed = feedparser.parse("https://www.reddit.com/r/help/.rss")

# Keep track of already posted items
posted_items = []

# Read the list of posted items from a file
with open("posted_items.txt", "r") as f:
    for line in f:
        posted_items.append(line.strip())

# Iterate through the items in the feed
for item in feed["items"]:
    # Check if the item has already been posted
    if item["link"] not in posted_items:
        # Add hashtag to the post
        post_text = item["title"] + "\n" + item["link"] + "\n" + "#hashtag"
        # Post the item to Mastodon
        mastodon_client.status_post(post_text)
        # Add the item to the list of posted items
        posted_items.append(item["link"])

# Save the list of posted items to the file
with open("posted_items.txt", "w") as f:
    for item in posted_items:
        f.write(item + "\n")
