import redditwarp.SYNC

client = redditwarp.SYNC.Client()

def get_top_temple_posts():
    """Gets the top 5 posts on the r/Temple subreddit, returns string with titles and usernames. If no posts in the hour, then display top posts of the day"""

    top_posts = "Top r/Temple posts of the "
    m = list(client.p.subreddit.pull.top('Temple', amount=5, time='hour'))
    if m:
        top_posts += "hour\n\n"
    else:
        top_posts+= "day\n\n"
        m =list(client.p.subreddit.pull.top('Temple', amount=5, time='day'))

    for post in m:
        top_posts += post.author_display_name + ": " + post.title + "\n\n"

    return top_posts
