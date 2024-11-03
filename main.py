# import asyncio
# from scraper import ProductScraper
#
#
# async def main():
#     urls_texno_park = [
#         "https://texnomart.uz/katalog/noutbuki/",
#         "https://texnomart.uz/katalog/smartfony/",
#         "https://texnomart.uz/katalog/holodilniki/"
#     ]
#
#     # urls_media_park = [
#     #     "https://mediapark.uz/products/category/apple-249",
#     #     "https://mediapark.uz/products/category/televizory-i-smart-televizory-8/televizory-307",
#     #     "https://mediapark.uz/products/category/gadzhety-18/smart-chasy-51"
#     # ]
#
#     # Instantiate the scrapers
#     scraper_texno_park = ProductScraper()
#     # scraper_media_park = ProductScraperMediaPark()
#
#     # Scrape and save data for TexnoPark
#     products_texno_park = await scraper_texno_park.scrape_multiple_pages(urls_texno_park)
#
#     # Scrape and save data for MediaPark
#     # products_media_park = await scraper_media_park.scrape_multiple_pages(urls_media_park)
#     print(products_texno_park)
#
#     # Print results for verification
#     # for product in products_media_park:
#     #     print("Media Park:", product)
#
#     # for product in products_texno_park:
#     #     print("Texno Park:", product)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

import asyncio
from scraper import ProductScraper


async def main():
    # List of URLs to scrape
    urls = [
        "https://texnomart.uz/katalog/noutbuki/",
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
