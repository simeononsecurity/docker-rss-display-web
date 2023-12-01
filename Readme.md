# RSS Feed Display Docker Container

This Docker container is designed to fetch and display the latest posts from a specified RSS feed using Python, Flask, and feedparser.

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/simeononsecurity/docker-rss-display-web
    ```

2. Build the Docker image:

    ```bash
    docker build -t rss-display .
    ```

    or pull it from [dockerhub](https://hub.docker.com/r/simeononsecurity/rss-display-web)


    ```bash
    docker pull simeononsecurity/rss-display-web
    ```


3. Run the Docker container:

    ```bash
    docker run -p 8080:80 --name rss-container rss-display
    ```

4. Visit [http://localhost:8080](http://localhost:8080) in your web browser to view the latest posts from the specified RSS feed.

## Configuration

To change the RSS feed source, modify the `RSS_FEED_URL` environment variable in the Dockerfile:

```Dockerfile
ENV RSS_FEED_URL=https://simeononsecurity.com/index.xml
```
or

Pass it in at run time.

```bash
docker run -p 8080:80 --name rss-container -e RSS_FEED_URL=https://example.com/rss.xml rss-display
```
## Dependencies

- Flask==2.2.5
- Werkzeug==2.0.1
- feedparser==6.0.8

These dependencies are listed in the `requirements.txt` file.

## Customization

Feel free to customize the Flask application (`app.py`) and HTML template (`templates/index.html`) to suit your needs. You can modify the number of displayed posts, the appearance of the webpage, and more.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
