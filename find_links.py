from playwright.sync_api import sync_playwright

def run():
    url = "https://www.withlocals.com/experience/the-10-tastings-of-bangkok-street-food-d5c9f078/reviews/"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('div[class*="experienceReview_"]')
        
        # Check for links with suspicious text
        links = page.locator('a').all_inner_texts()
        for l in links:
            l_clean = l.strip().lower()
            if l_clean in ["next", "more", "load more", "show more", ">", ">>"] or l_clean.isdigit():
                print(f"Potential pagination link: '{l}'")
        
        # Also check just div/span with "Show more" text
        show_more = page.get_by_text("Show more", exact=False)
        if show_more.count() > 0:
            print("Found text 'Show more'")
            
        load_more = page.get_by_text("Load more", exact=False)
        if load_more.count() > 0:
            print("Found text 'Load more'")

        browser.close()

if __name__ == "__main__":
    run()
