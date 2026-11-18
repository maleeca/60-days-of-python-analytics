import os
import shutil

# Full list of 60 Data Analyst portfolio projects across 6 tracks
PROJECTS = [
    # Data Cleaning & Wrangling 
    "messy-customer-csv-cleaning",
    "regex-text-parser",
    "datetime-timezone-normalizer",
    "missing-data-imputation",
    "json-api-flattener",
    "duplicate-transaction-resolver",
    "large-csv-chunking-pipeline",
    "multilingual-string-cleaner",
    "outlier-detection-zscore",
    "hierarchical-data-reshaper",
    
    # Exploratory Data Analysis & Statistics    
    "retail-sales-eda",
    "hypothesis-ab-testing",
    "correlation-matrix-analysis",
    "customer-segmentation-rfm",
    "distribution-skewness-analyzer",
    "cohort-retention-curve",
    "employee-attrition-eda",
    "weather-trends-time-series",
    "healthcare-readmission-stats",
    "survey-response-sentiment-eda",

    
    # Business Metrics & Financial/Product Analytics
    "saas-mr-arr-calculator",
    "customer-lifetime-value-ltv",
    "ecommerce-funnel-conversion",
    "churn-prediction-logic",
    "user-engagement-dau-mau",
    "cac-payback-period-model",
    "inventory-turnover-ratio",
    "pricing-elasticity-analyzer",
    "discount-coupon-impact",
    "subscription-renewal-forecast",

    # Web Scraping & API Data Ingestion
    "real-estate-scraper-bs4",
    "github-trending-api-extractor",
    "stock-market-yfinance-pipeline",
    "weather-forecast-api-ingest",
    "job-board-selenium-scraper",
    "social-media-hashtag-tracker",
    "crypto-price-websocket-logger",
    "rss-feed-news-aggregator",
    "public-transit-gtfs-parser",
    "rate-limited-api-crawler",

    # Interactive Dashboarding & Automation
    "streamlit-kpi-dashboard",
    "automated-pdf-report-generator",
    "excel-to-csv-batch-converter",
    "email-alert-summary-script",
    "interactive-plotly-sales-viewer",
    "markdown-report-compiler",
    "cli-data-profiling-tool",
    "config-driven-etl-runner",
    "streamlit-customer-segment-app",
    "end-to-end-analytics-portfolio-cli"
]

TEMPLATE_DIR = "templates/data-analyst-template"
PROJECTS_DIR = "projects"

def main():
    if not os.path.exists(TEMPLATE_DIR):
        print(f" Error: Template directory '{TEMPLATE_DIR}' not found!")
        print("Make sure you created the template folder first.")
        return

    os.makedirs(PROJECTS_DIR, exist_ok=True)

    print(f" Starting scaffolding for {len(PROJECTS)} projects...")

    created_count = 0
    skipped_count = 0

    for i, proj_name in enumerate(PROJECTS, start=1):
        folder_name = f"{i:02d}-{proj_name}"
        target_path = os.path.join(PROJECTS_DIR, folder_name)
        
        if os.path.exists(target_path):
            skipped_count += 1
            continue
            
        # Copy template folder structure and files
        shutil.copytree(TEMPLATE_DIR, target_path)
        
        # Automatically update README title
        readme_path = os.path.join(target_path, "README.md")
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            pretty_title = f"Project {i:02d}: {proj_name.replace('-', ' ').title()}"
            content = content.replace("[Insert Project Title Here]", pretty_title)
            
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
                
        created_count += 1
        print(f"[{i:02d}/60] Created: {target_path}")

    print("\n✨ Scaffolding Complete!")
    print(f"   - Newly created: {created_count}")
    print(f"   - Skipped (already existed): {skipped_count}")

if __name__ == "__main__":
    main()