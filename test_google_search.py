"""
Playwright automation script to search Google for SDET role information
"""
from playwright.sync_api import sync_playwright, expect
import time


def test_google_search():
    """Test function to search Google for SDET role information"""
    with sync_playwright() as p:
        # Launch browser (headless mode for CI/CD)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        page = context.new_page()
        
        try:
            # Navigate to Google
            print("Navigating to Google...")
            page.goto("https://www.google.com")
            
            # Wait for page to load
            page.wait_for_load_state("networkidle")
            
            # Accept cookies if the dialog appears (common in EU)
            try:
                accept_button = page.locator("button:has-text('Accept'), button:has-text('I agree'), button:has-text('Accept all')").first
                if accept_button.is_visible(timeout=2000):
                    accept_button.click()
                    print("Accepted cookies")
            except:
                print("No cookie dialog found or already accepted")
            
            # Find the search box and enter search query
            print("Entering search query...")
            search_query = "what is the future of SDET role in IT"
            
            # Try different selectors for the search box
            search_box = page.locator("textarea[name='q'], input[name='q']").first
            search_box.fill(search_query)
            
            # Submit the search
            print("Submitting search...")
            search_box.press("Enter")
            
            # Wait for search results to load
            page.wait_for_load_state("networkidle")
            print("Search results loaded")
            
            # Wait a bit to see the results
            time.sleep(2)
            
            # Verify we're on the search results page
            expect(page).to_have_url("https://www.google.com/search", timeout=10000)
            
            # Get the page title
            page_title = page.title()
            print(f"Page title: {page_title}")
            
            # Take a screenshot for verification
            page.screenshot(path="search_results.png")
            print("Screenshot saved as search_results.png")
            
            # Print first few search result titles
            result_titles = page.locator("h3").all()
            print(f"\nFound {len(result_titles)} search result titles")
            print("\nFirst 5 search results:")
            for i, title in enumerate(result_titles[:5], 1):
                try:
                    title_text = title.inner_text()
                    if title_text:
                        print(f"{i}. {title_text}")
                except:
                    pass
            
            print("\n✅ Test completed successfully!")
            
        except Exception as e:
            print(f"❌ Error occurred: {str(e)}")
            page.screenshot(path="error_screenshot.png")
            raise
        
        finally:
            # Close browser
            browser.close()


if __name__ == "__main__":
    test_google_search()
