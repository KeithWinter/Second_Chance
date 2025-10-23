import redditwarp.SYNC

client = redditwarp.SYNC.Client()

def get_top_temple_posts():
    """Gets the top 5 posts on the r/Temple subreddit, returns string with titles and usernames"""

    top_posts = ""
    m = client.p.subreddit.pull.top('Temple', amount=5, time='hour')

    for post in m:
        top_posts += post.author_display_name + ": " + post.title + "\n\n"

    return top_posts
