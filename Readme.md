# TexnoMart & MediaPark Scraper Project

This project provides a web scraping tool for extracting product data from TexnoMart and MediaPark e-commerce websites. The project uses `aiohttp` for asynchronous HTTP requests, `selenium` for handling dynamic content, and stores the scraped data in a PostgreSQL database.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Docker Setup](#docker-setup)

---

## Project Overview

This scraper:
- Extracts product data from given URLs on TexnoMart and MediaPark.
- Handles both static and dynamic page content.
- Stores extracted data in a PostgreSQL database for easy access and further analysis.
- Includes unit tests to verify data storage and scraping functionality.

## Technologies Used

- Python 3.11
- Selenium
- aiohttp
- BeautifulSoup4
- SQLAlchemy (ORM)
- Alembic (Migrations)
- PostgreSQL
- Docker & Docker Compose (for containerization)
- Pytest (for testing)

---

## Installation

### Prerequisites

- Python 3.8+
- Docker & Docker Compose

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rasulabduvaitov/testTask
    cd testTask
    ```

2. **Install dependencies**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    Create a `.env` file in the root directory with the following variables:

    ```ini
    DB_USER=your_db_user
    DB_PASS=your_db_password
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=your_db_name
   ```
If you running in docker :

```ini
    DB_USER=postgres
    DB_PASS=postgres
    DB_HOST=db
    DB_PORT=5432
    DB_NAME=postgres
   ```

4. **Run Database Migrations**:
    ```bash
    alembic upgrade head
    ```

---

## Environment Variables

The `.env` file should contain:

- **Database configuration**:
    - `DB_USER`, `DB_PASS`, `DB_HOST`, `DB_PORT`, `DB_NAME`
- **Selenium ChromeDriver Configuration**:
    - `CHROME_DRIVER`, `CHROME_BIN`

---

## Usage

### Running the Scraper

Run the `main.py` file to start scraping and saving data to the database.

```bash
python main.py
```


## Docker SetUp
```bash
    docker-compose up --build
```
