import asyncio
from scraper import ProductScraperMediaPark, ProductScraperTexnoMart

async def main():
    # List of URLs to scrape for TexnoMart and MediaPark
    urls_texno = [
        "https://texnomart.uz/katalog/noutbuki/",
        "https://texnomart.uz/katalog/smartfony/",
        # Add more URLs here as needed
    ]

    urls_media = [
        "https://mediapark.uz/products/category/noutbuki-i-ultrabuki-22/noutbuki-313",
        "https://mediapark.uz/products/category/stiralnye-i-sushilnye-mashiny-735/stiralnye-mashiny-70"

    ]

    # Instantiate TexnoMart scraper
    scraper_texno = ProductScraperTexnoMart()
    products_texno = await scraper_texno.scrape_multiple_pages(urls_texno)
    for product in products_texno:
        print("TexnoMart:", product)

    # Instantiate MediaPark scraper
    scraper_media = ProductScraperMediaPark(headless=True)
    try:
        # Scrape data from each URL in the `urls_media` list individually
        for url in urls_media:
            products_media = scraper_media.extract_product_data(url)
            for product in products_media:
                print("Media Park:", product)
    finally:
        # Ensure the browser is closed
        scraper_media.close()

# Run the main function
asyncio.run(main())
