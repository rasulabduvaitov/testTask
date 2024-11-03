# import aiohttp
# import asyncio
#
# import asyncpg
# from bs4 import BeautifulSoup
#
# from database import AsyncSessionLocal
# from models import Product
#
# # scraper.py
# import aiohttp
# import asyncio
# from bs4 import BeautifulSoup
#
#
# class ProductScraper:
#     def __init__(self):
#         self.products_data = []
#
#     async def fetch_page_content(self, url, session):
#         async with session.get(url) as response:
#             if response.status == 200:
#                 return await response.text()
#             else:
#                 print(f"Failed to fetch {url}, Status code: {response.status}")
#                 return None
#
#     async def extract_product_data(self, url, session):
#         html_content = await self.fetch_page_content(url, session)
#         if html_content is None:
#             return []
#
#         soup = BeautifulSoup(html_content, 'html.parser')
#         products_box = soup.select("div.products-box div.col-3")
#         print(products_box)
#
#         products = []
#         for product in products_box:
#             name_tag = product.select_one("a.product-name")
#             name = name_tag.text.strip() if name_tag else "N/A"
#
#             price_tag = product.select_one("div.product-price__current")
#             if price_tag:
#                 price_text = price_tag.get_text(strip=True).replace("сўм", "").replace(" ", "")
#                 price = int(price_text) if price_text.isdigit() else None
#             else:
#                 price = None
#
#             image_tag = product.select_one("img.product-image")
#             image_url = image_tag["src"] if image_tag else "N/A"
#
#             description = []
#             characteristic_items = product.select("ul.product-characteristic li.product-characteristic__item")
#             for item in characteristic_items:
#                 characteristic_name = item.select_one("span.characteristic-name").get_text(strip=True)
#                 characteristic_value = item.select_one("span.characteristic-value").get_text(strip=True)
#                 description.append(f"{characteristic_name}: {characteristic_value}")
#             description_text = ", ".join(description)
#
#             products.append({
#                 "name": name,
#                 "price": price,
#                 "image_url": image_url,
#                 "description": description_text,
#             })
#
#         return products
#
#     async def scrape_multiple_pages(self, urls):
#         async with aiohttp.ClientSession() as session:
#             tasks = [self.extract_product_data(url, session) for url in urls]
#             results = await asyncio.gather(*tasks)
#
#             # Flatten the list of results
#             for product_list in results:
#                 self.products_data.extend(product_list)
#
#         return self.products_data
#
# # class ProductScraperMediaPark:
# #     def __init__(self):
# #         self.products_data = []
# #
# #     async def fetch_page_content(self, url, session):
# #         async with session.get(url) as response:
# #             if response.status == 200:
# #                 return await response.text()
# #             else:
# #                 print(f"Failed to fetch {url}, Status code: {response.status}")
# #                 return None
# #
# #     async def get_fully_rendered_html(self, url):
# #         async with aiohttp.ClientSession() as session:
# #             html_content = await self.fetch_page_content(url, session)
# #             return html_content
# #
# #     async def extract_product_data(self, url, session):
# #         html_content = await self.fetch_page_content(url, session)
# #         if html_content is None:
# #             return []
# #
# #         soup = BeautifulSoup(html_content, 'html.parser')
# #         products_data = []
# #         product_cards = soup.find_all("a", class_="product-cart")
# #
# #         for product in product_cards:
# #             name = product.find("p", class_="text-dark").text.strip()
# #             price_element = product.find("span", {"price": True})
# #             price = int(price_element["price"]) if price_element and price_element.get("price") else None
# #             image_el = product.find("img", class_="product-image")
# #             print(image_el)
# #             image_url = image_el.get("src", "N/A") if image_el else None
# #
# #             description = name
# #             category = "N/A"
# #
# #             products_data.append({
# #                 "name": name,
# #                 "price": price,
# #                 "category": category,
# #                 "image_url": image_url,
# #                 "description": description,
# #             })
# #
# #         return products_data
# #
# #     # async def save_to_db(self, products):
# #     #     async with AsyncSessionLocal() as session:
# #     #         async with session.begin():
# #     #             for product_data in products:
# #     #                 product = Product(**product_data)
# #     #                 session.add(product)
# #     #         await session.commit()
# #
# #     async def scrape_multiple_pages(self, urls):
# #         async with aiohttp.ClientSession() as session:
# #             tasks = [self.extract_product_data(url, session) for url in urls]
# #             results = await asyncio.gather(*tasks)
# #
# #             # Flatten the results
# #             all_products = [product for product_list in results for product in product_list]
# #             # await self.save_to_db(all_products)
# #             return all_products
# #

# scraper.py
import aiohttp
import asyncio
from bs4 import BeautifulSoup


class ProductScraper:
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
            print(image_tag)
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



async def main():
    # List of URLs to scrape
    urls = [
        # "https://texnomart.uz/katalog/noutbuki/",
        "https://texnomart.uz/katalog/smartfony/",
        # Add more URLs here as needed
    ]

    scraper = ProductScraper()
    products = await scraper.scrape_multiple_pages(urls)

    # Print results
    for product in products:
        print(product)


# Run the scraper
asyncio.run(main())