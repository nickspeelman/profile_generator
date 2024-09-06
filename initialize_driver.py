def initialize_driver():
    """Initialize a headless Selenium WebDriver."""
    service = Service('path/to/chromedriver')  # Replace with the path to your ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headless, no GUI
    driver = webdriver.Chrome(service=service, options=options)
    return driver