import asyncio
from playwright.async_api import async_playwright

path_to_extension = "/Users/amirjon/Documents/parsing/Pars/capsolve"
user_data_dir = "user_dataa"

async def run(playwright):
    browser_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    context = await playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        executable_path=browser_path,
        args=[
            f"--disable-extensions-except={path_to_extension}",
            f"--load-extension={path_to_extension}",
        ],
    )

    page = context.pages[0] if context.pages else await context.new_page()

    # ✅ Sahifani yuklash tezroq bo‘lishi uchun 'domcontentloaded' ishlatamiz
    await page.goto("https://www.coursera.org/?authMode=signup", wait_until="domcontentloaded")
    # Login sahifasining automatlashishi
    # Name uchun bo'lim
    await page.wait_for_selector("input[name='name']", state="visible", timeout=5000)
    await page.locator("input[name='name']").fill("Amirjon Karimov")
    
    # ✅ Email inputni yuklanishini kutish va to‘ldirish
    await page.wait_for_selector("input[name='email']", state="visible", timeout=5000)
    await page.locator("input[name='email']").fill("your_email@example.com")
    # ✅Password uchun bo'lim
    await page.wait_for_selector("input[name='password']", state="visible", timeout=5000)
    await page.locator("input[name='password']").fill("Karimoff2007")
    # ✅ "Join for Free" tugmasini bosish
    await page.wait_for_selector("button[data-e2e='signup-form-submit-button']", state="visible", timeout=5000)
    await page.locator("button[data-e2e='signup-form-submit-button']").click()

        # ⏳ Kutish vaqtini qisqartiramiz yoki olib tashlaymiz
    await page.wait_for_timeout(10000000)  # 1 sekund kifoya

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
