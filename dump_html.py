from playwright.sync_api import sync_playwright
import time
import sys

def run():
    target_url = "https://www.withlocals.com/experience/the-10-tastings-of-bangkok-street-food-d5c9f078/reviews/"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print(f"Navigating to {target_url}...")
        page.goto(target_url, timeout=60000)
        time.sleep(5)
        
        # Scroll a bit
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        
        content = page.content()
        with open("reviews_page.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Dumped HTML to reviews_page.html")
            
        browser.close()

if __name__ == "__main__":
    run()
