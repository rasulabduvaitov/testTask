import asyncio
from scraper import ProductScraperMediaPark, ProductScraperTexnoMart

async def main():
    urls_texno = [
        "https://texnomart.uz/katalog/noutbuki/",
        "https://texnomart.uz/katalog/smartfony/",
    ]

    urls_media = [
        "https://mediapark.uz/products/category/noutbuki-i-ultrabuki-22/noutbuki-313",
        "https://mediapark.uz/products/category/stiralnye-i-sushilnye-mashiny-735/stiralnye-mashiny-70"

    ]

    scraper_texno = ProductScraperTexnoMart()
    products_texno = await scraper_texno.scrape_multiple_pages(urls_texno)
    for product in products_texno:
        print("TexnoMart:", product)

    scraper_media = ProductScraperMediaPark(headless=True)
    try:
        for url in urls_media:
            products_media = scraper_media.extract_product_data(url)
            for product in products_media:
                print("Media Park:", product)
    finally:
        scraper_media.close()

asyncio.run(main())
