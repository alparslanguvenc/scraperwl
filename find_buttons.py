from playwright.sync_api import sync_playwright

def run():
    url = "https://www.withlocals.com/experience/the-10-tastings-of-bangkok-street-food-d5c9f078/reviews/"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('div[class*="experienceReview_"]')
        
        # List all buttons
        buttons = page.locator('button').all_inner_texts()
        print("Buttons found:", buttons)
        
        # Check specifically for show more candidates
        for b in buttons:
            if "show" in b.lower() or "load" in b.lower() or "more" in b.lower():
                print(f"Potential load button: '{b}'")
                
        browser.close()

if __name__ == "__main__":
    run()
