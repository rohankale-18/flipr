## Project Overview

This project was developed for a hackathon, aiming to automate and enhance news content creation and delivery. We built a comprehensive pipeline that:

1.  **Scrapes news articles** from IndiaTVNews using Selenium.
2.  **Generates SEO tags and summaries** using an Deepseek V3.
3.  **Creates engaging images** using Pollinations AI.
4.  **Deploys the scraper as a Flask API.**
5.  **Integrates the API with a WordPress website.**
6.  **Stores and manages data** in a database.
7.  **Deploys the entire website.**
8.  **Updates news articles at regular intervals.**

This pipeline automates the entire process from extraction to publication, significantly reducing manual effort and improving content quality.

## Features

* **Automated News Scraping:** Extracts news articles from IndiaTVNews using Selenium for dynamic content handling.
* **AI-Powered SEO Optimization:** Generates relevant SEO tags and summaries using an AI model.
* **AI-Generated Images:** Creates visually appealing images using Pollinations AI based on news headlines.
* **Flask API:** Deploys the scraper as a RESTful API for easy integration.
* **WordPress Integration:** Seamlessly integrates the API with a WordPress website to publish scraped and enhanced news.
* **Database Storage:** Stores scraped news, AI-generated content, and images in a database for efficient management.
* **End-to-End Automation:** Automates the entire content pipeline from scraping to publishing.
* **Regular News Updates:** Updates news articles at predefined intervals to keep content fresh.
* **Deployed Website:** The entire news aggregation website has been deployed for public access.

## Technologies Used

* **Python:** For scraping, AI processing, and Flask API.
* **Selenium:** For dynamic web scraping.
* **Flask:** For creating the API.
* **Pollinations AI:** For image generation.
* **AI Model (Deepseek V3):** For SEO tag and summary generation.
* **Database (Wordpress CMS):** For data storage.
* **WordPress:** For website integration.
* **Requests (Python Library):** For making HTTP requests.
* **Deployment Platform (Wordpress):** For deploying the WordPress website.

## Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/rohankale-18/flipr[https://github.com/rohankale-18/flipr]
    cd flipr
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Selenium Drivers:**

    * Download the appropriate WebDriver (e.g., ChromeDriver, GeckoDriver) for your browser.
    * Place the WebDriver executable in a directory accessible by your system's PATH.

5.  **Configure Database:**

    * Set up your chosen database.
    * Update the database connection details in the application configuration files.

6.  **Configure API Keys:**

    * Obtain API keys for Pollinations AI and any other required services.
    * Update the API keys in the application configuration files.

7.  **Run the Flask API:**

    ```bash
    python app.py
    ```

8.  **WordPress Integration:**

    * Install a plugin or develop a custom plugin to consume the Flask API.
    * Configure the plugin to fetch news articles from the API and publish them on your WordPress website.

9.  **Run the AI Optimization and Image Generation:**

    * Run the scripts that handle the AI model and Pollinations AI integration.

10. **Deployment:**

    * Deploy the Flask API and WordPress website to your chosen hosting platform.
    * Configure the scheduling tool to update news articles at regular intervals.

## Project Structure

├── app.py # Flask API application 
├── scraper.py # Web scraping logic (using Selenium) 
├── ai_optimization.py # AI model for SEO and summary 
├── image_generator.py # Pollinations AI integration 
├── database.py # Database interaction logic 
├── requirements.txt # Python dependencies 
├── README.md # Project documentation 
└── ... # Other files

## Usage

1.  **Run the Flask API:** The API will scrape news articles periodically (or on demand) using Selenium and store them in the database.
2.  **WordPress Integration:** The WordPress website will fetch news articles from the API and publish them automatically.
3.  **AI Processing:** The AI optimization and image generation scripts will process the scraped news and generate SEO tags, summaries, and images.
4.  **Scheduled Updates:** News articles will be updated automatically at the configured intervals.
5.  **Access the Website:** Visit the deployed website to view the aggregated news.

## Future Improvements

* **Enhanced AI Models:** Improve the accuracy and relevance of AI-generated content.
* **Real-Time Scraping:** Implement real-time news scraping and publishing.
* **Improved Image Generation:** Explore advanced image generation techniques.
* **User Interface:** Develop a user interface for managing news articles and configurations.
* **Error Handling and Logging:** Implement robust error handling and logging mechanisms.
* **Scalability:** Optimize the application for scalability and performance.
* **Add more news sources:** Add functionality to scrape from more news sources.
* **Improve scheduling:** Add a better scheduling system with a UI.

## Contributors

* Vedant Raulkar
* Pranav Sonar
* Rohan Kale
* Jignesh Patil