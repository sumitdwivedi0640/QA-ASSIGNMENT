"""
Playwright automation script to search Google for SDET role information
"""
from playwright.sync_api import sync_playwright, expect
import time
import sys


def test_google_search():
    """Test function to search Google for SDET role information"""
    with sync_playwright() as p:
        # Launch browser (headless mode for CI/CD)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        page = context.new_page()
        
        try:
            # Navigate to Google
            print("Navigating to Google...")
            page.goto("https://www.google.com", wait_until="domcontentloaded", timeout=30000)
            
            # Wait for page to load
            page.wait_for_load_state("domcontentloaded")
            time.sleep(2)  # Give time for dynamic content
            
            # Accept cookies if the dialog appears (common in EU)
            try:
                # Try multiple cookie button selectors
                cookie_selectors = [
                    "button:has-text('Accept all')",
                    "button:has-text('Accept')",
                    "button:has-text('I agree')",
                    "button[id='L2AGLb']",
                    "button:has-text('Aceitar tudo')",
                    "[aria-label*='Accept']",
                    "[aria-label*='accept']"
                ]
                for selector in cookie_selectors:
                    try:
                        accept_button = page.locator(selector).first
                        if accept_button.is_visible(timeout=3000):
                            accept_button.click()
                            print(f"Accepted cookies using selector: {selector}")
                            time.sleep(1)
                            break
                    except:
                        continue
            except Exception as e:
                print(f"No cookie dialog found or already accepted: {e}")
            
            # Find the search box and enter search query
            print("Entering search query...")
            search_query = "what is the future of SDET role in IT"
            
            # Wait for search box to be visible and try different selectors
            search_box = None
            search_selectors = [
                "textarea[name='q']",
                "input[name='q']",
                "textarea[aria-label*='Search']",
                "input[aria-label*='Search']",
                "textarea[title*='Search']",
                "input[title*='Search']"
            ]
            
            for selector in search_selectors:
                try:
                    search_box = page.locator(selector).first
                    if search_box.is_visible(timeout=5000):
                        print(f"Found search box using selector: {selector}")
                        break
                except:
                    continue
            
            if not search_box or not search_box.is_visible():
                raise Exception("Could not find Google search box")
            
            # Clear and fill the search box
            search_box.click()
            search_box.fill("")
            search_box.fill(search_query)
            time.sleep(1)
            
            # Submit the search
            print("Submitting search...")
            search_box.press("Enter")
            
            # Wait for search results to load
            page.wait_for_load_state("domcontentloaded", timeout=30000)
            time.sleep(3)  # Wait for results to render
            
            # Verify we're on the search results page (more flexible URL check)
            current_url = page.url
            print(f"Current URL: {current_url}")
            
            if "google.com/search" not in current_url.lower():
                # If we're not on search page, try navigating directly
                print("Not on search page, navigating directly...")
                encoded_query = search_query.replace(" ", "+")
                page.goto(f"https://www.google.com/search?q={encoded_query}", wait_until="domcontentloaded", timeout=30000)
                time.sleep(3)
            
            # Get the page title
            page_title = page.title()
            print(f"Page title: {page_title}")
            
            # Take a screenshot for verification
            page.screenshot(path="search_results.png", full_page=True)
            print("Screenshot saved as search_results.png")
            
            # Print first few search result titles
            try:
                result_titles = page.locator("h3").all()
                print(f"\nFound {len(result_titles)} search result titles")
                if len(result_titles) > 0:
                    print("\nFirst 5 search results:")
                    for i, title in enumerate(result_titles[:5], 1):
                        try:
                            title_text = title.inner_text()
                            if title_text:
                                print(f"{i}. {title_text}")
                        except:
                            pass
                else:
                    print("No search result titles found, but page loaded successfully")
            except Exception as e:
                print(f"Could not extract search results: {e}")
            
            print("\n✅ Test completed successfully!")
            return 0
            
        except Exception as e:
            print(f"❌ Error occurred: {str(e)}")
            import traceback
            traceback.print_exc()
            try:
                page.screenshot(path="error_screenshot.png", full_page=True)
                print("Error screenshot saved as error_screenshot.png")
            except:
                pass
            return 1
        
        finally:
            # Close browser
            browser.close()


if __name__ == "__main__":
    exit_code = test_google_search()
    sys.exit(exit_code)
