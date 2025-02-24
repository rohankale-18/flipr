import requests
import json
import time
import re
from IndiaTVnews import scrap
import cloudinary
import cloudinary.uploader
import os
Response = scrap(1,"crime")

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)

def generate_image(headline):
    """Uploads an image from a given URL to Cloudinary and returns the URL."""
    
    # URL of the image to upload (you can replace this with any image source)
    image_url = f"https://pollinations.ai/p/{headline}?width=1024&height=1024&seed=42&model=flux"
    
    try:
        # Upload image to Cloudinary
        upload_result = cloudinary.uploader.upload(
            image_url,  
            folder="products",  # Uploads to 'products' folder in Cloudinary
            public_id=headline.replace(" ", "_").lower(),  # Generate a unique ID based on the headline
            overwrite=True
        )
        
        # Return the Cloudinary URL
        return upload_result.get("secure_url", "Upload failed")

    except Exception as e:
        return f"Error: {str(e)}"
    

def make_api_call(prompt, content, max_tokens=512, retry_count=3):
    url = "https://api.hyperbolic.xyz/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqaWduZXNocGF0aWwxMjA0MDRAZ21haWwuY29tIiwiaWF0IjoxNzMzOTk2NDAyfQ.rQRJ7PG4I47_DfAN7gYcujdophpT42B4sNnEZjE156E"
    }
    
    data = {
        "messages": [{"role": "user", "content": prompt.format(content=content)}],
        "model": "deepseek-ai/DeepSeek-V3",
        "max_tokens": max_tokens,
        "temperature": 0.1,
        "top_p": 0.9
    }
    
    for attempt in range(retry_count):
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content'].strip()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Too Many Requests
                wait_time = 5 * (attempt + 1)  # Exponential backoff
                print(f"Rate limit hit, waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue
            print(f"API call failed: {str(e)}")
        except Exception as e:
            print(f"API call failed: {str(e)}")
        
        if attempt < retry_count - 1:  # Don't sleep on last attempt
            time.sleep(3)  # Basic delay between retries
    
    return ""

def get_summary(content):
    prompt = "Write a concise 200-220 word summary of this article: {content}"
    return make_api_call(prompt, content, max_tokens=512)

def get_seo_tags(content):
    prompt = "List exactly 3-4 most relevant SEO keywords for this article. Return only the keywords, one per line: {content}"
    result = make_api_call(prompt, content, max_tokens=128)
    return [tag.strip() for tag in result.split('\n') if tag.strip()]

def process_content():
    try:
        articles = Response
        processed_articles = []
        
        for article in articles:
            content = article['content']
            
            processed_article = {
                'headline': article['headline'],
                'domain': article['domain'],
                'date': article['date'],
                'summary': get_summary(content),
                'seo_tags': get_seo_tags(content),
                'image': generate_image(article['headline'])
            }
            
            processed_articles.append(processed_article)
        
        with open('processed_articles.json', 'w', encoding='utf-8') as file:
            json.dump(processed_articles, file, indent=2)
            
    except Exception as e:
        print(f"Error processing content: {str(e)}")

if __name__ == "_main_":
    process_content()