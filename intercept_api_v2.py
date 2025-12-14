from playwright.sync_api import sync_playwright

def run():
    url = "https://www.withlocals.com/experience/the-10-tastings-of-bangkok-street-food-d5c9f078/reviews/"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Log all data requests
        page.on("request", lambda request: print(f">> {request.method} {request.resource_type} {request.url}") if request.resource_type in ["fetch", "xhr", "script"] else None)
        
        page.goto(url)
        page.wait_for_timeout(5000)
        
        print("Scrolling...")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(5000)
        
        browser.close()

if __name__ == "__main__":
    run()
