import aiohttp
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


class ProductScraperTexnoMart:
    def __init__(self):
        self.products_data = []

    async def fetch_page_content(self, url, session):
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"Failed to fetch {url}, Status code: {response.status}")
                return None

    async def extract_product_data(self, url, session):
        html_content = await self.fetch_page_content(url, session)
        if html_content is None:
            return []

        soup = BeautifulSoup(html_content, 'html.parser')
        products_box = soup.select("div.products-box div.col-3")

        products = []
        for product in products_box:
            name_tag = product.select_one("a.product-name")
            name = name_tag.text.strip() if name_tag else "N/A"

            price_tag = product.select_one("div.product-price__current")
            if price_tag:
                price_text = price_tag.get_text(strip=True).replace("сўм", "").replace(" ", "")
                price = int(price_text) if price_text.isdigit() else None
            else:
                price = None

            image_tag = product.select_one("img.product-image")
            image_url = image_tag["data-src"] if image_tag else "N/A"

            description = []
            characteristic_items = product.select("ul.product-characteristic li.product-characteristic__item")
            for item in characteristic_items:
                characteristic_name = item.select_one("span.characteristic-name").get_text(strip=True)
                characteristic_value = item.select_one("span.characteristic-value").get_text(strip=True)
                description.append(f"{characteristic_name}: {characteristic_value}")
            description_text = ", ".join(description)

            products.append({
                "name": name,
                "price": price,
                "image_url": image_url,
                "description": description_text,
            })

        return products

    async def scrape_multiple_pages(self, urls):
        async with aiohttp.ClientSession() as session:
            tasks = [self.extract_product_data(url, session) for url in urls]
            results = await asyncio.gather(*tasks)

            # Flatten the list of results
            for product_list in results:
                self.products_data.extend(product_list)

        return self.products_data



class ProductScraperMediaPark:
    def __init__(self, headless=True):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)

    def scroll_to_load_all_content(self, scroll_pause_time=2):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def extract_product_data(self, url):
        self.driver.get(url)
        self.scroll_to_load_all_content()
        html_content = self.driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        products_data = []
        product_cards = soup.find_all("a", class_="product-cart")

        for product in product_cards:
            name = product.find("p", class_="text-dark").text.strip()
            price_element = product.find("span", {"price": True})
            price = int(price_element["price"]) if price_element and price_element.get("price") else None

            image_el = product.find("img", class_="product-image")
            image_url = image_el["src"] if image_el else "N/A"
            description = name
            category = "N/A"

            products_data.append({
                "name": name,
                "price": price,
                "category": category,
                "image_url": image_url,
                "description": description,
            })

        return products_data

    def close(self):
        self.driver.quit()






