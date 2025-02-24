from flask import Flask, jsonify
from Test import get_summary, get_seo_tags, generate_image
from IndiaTVnews import scrap
import aiohttp
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get values from environment variables
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
WP_URL = os.getenv("WP_URL")
VALID_DOMAINS = ['crime', 'sports', 'health', 'business', 'education']

async def to_wp(session, blog):
    """Posts a blog to WordPress."""
    url=f"https://public-api.wordpress.com/rest/v1.1/sites/{WP_URL}/posts/new"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    async with session.post(url, json=blog, headers=headers) as response:
        result = await response.text()
        if response.status == 201:
            print(f"Successfully posted: {blog['headline']}")
        else:
            print(f"Failed to post: {blog['headline']}, Error: {result}")


async def post_blogs(blogs):
    """Handles async posting of multiple blogs."""
    async with aiohttp.ClientSession() as session:
        tasks = [to_wp(session, blog) for blog in blogs]
        await asyncio.gather(*tasks)


@app.route('/process_articles', methods=['GET'])
def process_articles():
    try:
        quantity = 1  # Fixed quantity
        processed_articles = []

        # Loop through the 5 domains
        for domain in VALID_DOMAINS:
            articles = scrap(quantity, domain)
            if not articles:
                continue  # Skip if no articles found

            article = articles[0]  # Take the first article

            processed_article = {
                'title': article['headline'],
                'categories': article['domain'],
                'content': get_summary(article['content']),
                'tags': get_seo_tags(article['content']),
                'featured_image': generate_image(article['headline'])
            }

            print(f"Processed: {processed_article['featured_image']}")

            processed_articles.append(processed_article)

        # Post articles to WordPress asynchronously
        asyncio.run(post_blogs(processed_articles))
        block = jsonify(processed_articles)
        return block

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '_main_':
    app.run(debug=True, port=10000)