import os
from datetime import datetime

# Configuration
BASE_URL = "https://www.frankchen.tw/pdfkey/"
SOURCE_DIR = "pdfkey"
OUTPUT_FILE = os.path.join(SOURCE_DIR, "sitemap.xml")

# Priority and Changefreq settings
# Default: priority 0.8, changefreq monthly
# Index: priority 1.0, changefreq weekly
URL_CONFIG = {
    "index.html": {"priority": "1.0", "changefreq": "weekly", "loc_suffix": ""},
}

DEFAULT_CONFIG = {"priority": "0.8", "changefreq": "monthly"}

def generate_sitemap():
    urls = []
    
    # Get all HTML files in the source directory
    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".html")]
    
    # Sort files to ensure consistent output
    files.sort()
    
    # Ensure index.html comes first if it exists
    if "index.html" in files:
        files.remove("index.html")
        files.insert(0, "index.html")

    sitemap_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for filename in files:
        config = URL_CONFIG.get(filename, DEFAULT_CONFIG)
        
        # Determine location URL
        loc_suffix = config.get("loc_suffix", filename)
        loc = f"{BASE_URL}{loc_suffix}"
        
        priority = config.get("priority", DEFAULT_CONFIG["priority"])
        changefreq = config.get("changefreq", DEFAULT_CONFIG["changefreq"])
        
        sitemap_content.append('  <url>')
        sitemap_content.append(f'    <loc>{loc}</loc>')
        sitemap_content.append(f'    <changefreq>{changefreq}</changefreq>')
        sitemap_content.append(f'    <priority>{priority}</priority>')
        sitemap_content.append('  </url>')

    sitemap_content.append('</urlset>')
    
    # Write to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_content))
        f.write("\n") # Add trailing newline

    print(f"Sitemap generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_sitemap()
