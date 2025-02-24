import csv
import time
import json
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
def scrap(quantity, domain):
    scraped_data = []

    for i in range(1, quantity + 1):  
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")  # Headless mode to avoid UI issues
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")  # Bypass /dev/shm issues
        chrome_options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging
        chrome_options.add_argument("--disable-software-rasterizer")  # Disable software rasterizer


        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            url = f"https://www.indiatvnews.com/{domain}/{i}"
            driver.get(url)

            newsdiv = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/main/section[2]/div/div[1]/div[1]/div/ul"))
            )
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            NewsLinks = WebDriverWait(newsdiv, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
            )

            # Extract and remove duplicate links
            links = list(set(news.get_attribute("href") for news in NewsLinks if news.get_attribute("href")))

            for link in links[:1]:
                driver.get(link)

                # Extract headline
                HeadLine = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/main/section[2]/div/div/div[1]/div[1]/h1"))
                ).text       

                # Extract content
                Content = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/main/section[2]/div/div/div[1]"))
                ).text
                date=WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/main/section[2]/div/div/div[1]/div[2]/div[1]/div[2]/time[1]"))
                ).text
                scraped_data.append({
                    "domain": domain,
                    "headline": HeadLine,
                    "content": Content,
                    "date":date
                })

        except Exception as e:
            print(f"Error on page {i}: {str(e)}")

        finally:
            driver.quit()

    return scraped_data