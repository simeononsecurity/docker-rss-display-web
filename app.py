from flask import Flask, render_template
from flask_caching import Cache
import feedparser
import os

# Create a Flask application
app = Flask(__name__)

# Configure caching for the application using Flask-Caching
cache = Cache(app, config={'CACHE_TYPE': 'simple'})  # Use 'simple' cache for development; choose appropriate cache for production

# Define the route for the root URL '/'
@app.route('/')
@cache.cached(timeout=3600)  # Cache for 60 minutes
def index():
    # Retrieve the RSS feed URL from environment variables
    rss_feed_url = os.environ.get('RSS_FEED_URL')
    
    try:
        # Parse the RSS feed using the feedparser library
        feed = feedparser.parse(rss_feed_url)
    except Exception as e:
        # Handle the exception, e.g., log the error and return an error page
        return render_template('error.html', error_message=str(e))

    # Extract feed metadata and the latest posts from the parsed feed
    parsedfeed = feed.feed
    latest_posts = feed.entries[:50]  # Displaying the latest 50 posts as an example
    
    # Render the HTML template with feed information and latest posts
    return render_template('index.html', feed=parsedfeed, posts=latest_posts, rss_feed_url=rss_feed_url)

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)