from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os
import requests

def fetch_webpage_content_selenium(url, profile_folder):
    """Fetch the body content of a webpage using Selenium, or download the PDF if applicable."""
    try:
        # Set up Selenium WebDriver with Chrome options (headless mode and suppressing logs)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--log-level=3")  # Suppress logs

        # Path to your ChromeDriver or configure it in PATH
        driver_path = r"C:\chromedriver-win64\chromedriver.exe"  # Update with your actual ChromeDriver path
        service = Service(driver_path)

        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the URL
        driver.get(url)

        # Wait for the page to load completely
        time.sleep(3)

        # Extract the body content of the page
        body_content = driver.find_element(By.TAG_NAME, "body").text

        # Close the driver
        driver.quit()

        return body_content

    except Exception as e:
        print(f"Error fetching content from {url}: {e}")

        # For PDFs, handle download
        if url.lower().endswith('.pdf'):
            pdf_name = save_pdf(profile_folder, url)
            if pdf_name:
                return f"PDF saved as {pdf_name}"
            else:
                return "Error saving PDF"
        return "Content could not be retrieved."
