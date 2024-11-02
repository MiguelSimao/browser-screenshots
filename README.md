# Webpage Screenshot Taker

This project is designed to take screenshots of webpages using Selenium and Docker. It includes a Python script that connects to a Selenium WebDriver running inside a Docker container to capture screenshots.

## Prerequisites

- Docker
- Docker Compose
- Python 3.8

## Setup

1. **Environment set:**

    ```sh
    git clone https://github.com/MiguelSimao/browser-screenshots.git
    cd browser-screenshots
    ```

2. **Environment setup:**

    ```sh
    mkdir screenshots
    ```

## Usage

### Running with Docker Compose

1. **Start the Selenium container:**

    ```sh
    docker compose up selenium -d
    ```
2. **Take a screenshot:**
    ```sh
    docker compose run --rm scraper python screenshot.py "https://www.google.com" screenshots/google --wait-time 2
    ```

## Configuration

- **docker-compose.yml**: Defines the services for Selenium and the scraper.
- **Dockerfile**: Sets up the Python environment and runs the [screenshot.py] script.
- **requirements.txt**: Lists the Python dependencies.
- **screenshot.py**: Contains the logic for taking screenshots.

## License

This project is licensed under the MIT License.
