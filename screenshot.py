import os
import argparse
import time
from datetime import datetime, timezone
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging


def take_screen_shot(
    url: str,
    wait_time_seconds: int,
    output_dir: str,
    width: int,
    height: int,
    scroll_height: int = 400,
    retries: int = 5,
    retry_delay: int = 5
):
    
    logging.info(f"Taking screenshot of {url}...")
    logging.info(f"Wait time: {wait_time_seconds} seconds")
    

    dt = datetime.now(timezone.utc).isoformat()
    output_file = f'{output_dir}/{dt}.png'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    options = Options()
    options.add_argument('--headless')
    

    attempt = 0
    while attempt < retries:
        try:
            # Connect to the WebDriver running inside the container
            driver = webdriver.Remote(
                command_executor='http://selenium:4444/wd/hub',
                options=options
            )
            driver.set_window_size(width, height)
            driver.get(url)
            
            time.sleep(wait_time_seconds)
            driver.execute_script(f"window.scrollTo(0, {scroll_height});")
            driver.save_screenshot(output_file)
            logging.info(f"Screenshot saved to {output_file}")

            driver.quit()
            break
        except Exception as e:
            attempt += 1
            logging.info(f"Attempt {attempt} failed: {e}")
            if attempt < retries:
                logging.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logging.info("All attempts failed. Exiting.")
                raise


if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser(description='Take a screenshot of a webpage')
    parser.add_argument('url', type=str, help='URL of the webpage')
    parser.add_argument('output_dir', type=str, help='Output directory')
    parser.add_argument('--wait-time', type=int, default=60, help='Wait time in seconds')
    parser.add_argument('--width', type=int, default=1920, help='Width of the browser window')
    parser.add_argument('--height', type=int, default=1080, help='Height of the browser window')
    parser.add_argument('--scroll-height', type=int, default=400, help='Height to scroll the page')

    args = parser.parse_args()
    take_screen_shot(args.url, args.wait_time, args.output_dir, args.width, args.height)

