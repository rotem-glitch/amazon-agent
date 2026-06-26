from playwright.sync_api import sync_playwright
import ollama

# פונקציה לבדיקת מוצר
def analyze_product(product_name):
    try:
        response = ollama.chat(model='llama3', messages=[
            {'role': 'user', 'content': f'Is {product_name} a good product for dropshipping? Answer in one sentence.'},
        ])
        return response['message']['content']
    except Exception as e:
        return "Could not analyze"

# הרצת הסורק
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    print("Connecting to Amazon...")
    page.goto("https://www.amazon.com/Best-Sellers/zgbs")
    
    # שליפת שמות מוצרים
    elements = page.query_selector_all(".p13n-sc-truncate-desktop-type2")
    products = [el.inner_text() for el in elements[:3]]
    
    for name in products:
        print(f"\nAnalyzing: {name}")
        print(f"AI Verdict: {analyze_product(name)}")
        
    browser.close()