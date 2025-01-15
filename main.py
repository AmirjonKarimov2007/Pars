import asyncio
from playwright.async_api import async_playwright, Playwright
import os
path_to_extension = "/home/amirjon/Documents/web_Scraping/coursera_login/ezyZip"
user_data_dir = "user_dataa"

async def run(playwright: Playwright):
    context = await playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        args=[
            f"--disable-extensions-except={path_to_extension}",
            f"--load-extension={path_to_extension}",
        ],
    )

    # Create a new page in the context
    page = await context.new_page()

    # Navigate to the desired URL
    await page.goto("https://www.coursera.org/?authMode=signup")

    # You can add more code here to interact with the page or wait as needed
    await page.wait_for_timeout(10000)  # Wait for 10 seconds before closing (optional)
    import time
    time.sleep(100)

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
