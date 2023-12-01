from flask import Flask, render_template
import feedparser
import os

app = Flask(__name__)

@app.route('/')
def index():
    rss_feed_url = os.environ.get('RSS_FEED_URL')
    
    try:
        feed = feedparser.parse(rss_feed_url)
    except Exception as e:
        # Handle the exception, e.g., log the error and return an error page
        return render_template('error.html', error_message=str(e))

    parsedfeed = feed.feed
    latest_posts = feed.entries[:50]  # Displaying the latest 5 posts as an example
    return render_template('index.html', feed=parsedfeed, posts=latest_posts, rss_feed_url=rss_feed_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
