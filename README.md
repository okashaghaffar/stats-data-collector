# Web Scraping App with Python Selenium

This application is built using Python and Selenium to scrape data from a particular website and display the collected data.

## Features

- **Web Scraping**: Utilizes Selenium to automate the process of navigating through web pages and extracting desired data.
- **Data Collection**: Gathers information from a specific website.
- **Data Presentation**: Presents the collected data in a user-friendly format.

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/okashaghaffar/stats-data-collector
    ```
2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
3. **Download WebDriver:**
    You need to download the WebDriver for your browser and place it in the project directory. The WebDriver acts as a bridge between Selenium and your chosen web browser.
    - For Chrome: Download Chromedriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - For Firefox: Download Geckodriver from [here](https://github.com/mozilla/geckodriver/releases).

## Usage

1. **Run the Python script:**
    ```
    python scrape_and_display.py
    ```
2. **Follow the instructions:**
    The script will prompt you to enter necessary information or configurations required for scraping data from the website.

## Configuration

- **Website URL:** Modify the `website_url` variable in the script to change the target website.
- **Data Extraction:** Adjust the Selenium code in the script according to the structure of the website and the data you want to extract.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to fork this repository and submit a pull request.

## License

[MIT License](LICENSE)
