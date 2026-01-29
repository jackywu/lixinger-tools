#!/usr/bin/env python3
"""
Script to download Lixinger API documentation pages using Playwright.
Saves each page as a markdown file in the docs/ directory.
"""

import asyncio
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from playwright.async_api import async_playwright
from markdownify import markdownify as md


# All API documentation URLs extracted from the website
API_URLS = [
    "https://www.lixinger.com/open/api/doc",
    # 大陆 (Mainland China) - 公司接口
    "https://www.lixinger.com/open/api/doc?api-key=cn/company",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/profile",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/equity-change",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/candlestick",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/shareholders-count",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/executives-equity-change",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/majority-shareholders-equity-change",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/top-list",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/block-trade",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/pledge",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/operation-revenue-constitution",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/operating-data",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/indices",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/industries",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/announcement",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/regulatory-measures",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/inquiry",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/top-10-shareholders",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/top-10-tradable-shareholders",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fund-collection-shareholders",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fund-company-shareholders",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/dividend",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/allotment",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/customers",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/suppliers",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fundamental/non_financial",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fundamental/bank",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fundamental/security",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fundamental/insurance",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fundamental/other_financial",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fs/non_financial",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fs/bank",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fs/security",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fs/insurance",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/fs/other_financial",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/tr_dri",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/mm_ha",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/mtasl",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/esc",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/mssc",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/t_a",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/elr",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/ple",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/capita",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/shnc",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/df",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/npd",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/hot/tr",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/mutual-market",
    "https://www.lixinger.com/open/api/doc?api-key=cn/company/margin-trading-and-securities-lending",
    # 大陆 - 指数接口
    "https://www.lixinger.com/open/api/doc?api-key=cn/index",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/constituents",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/constituent-weightings",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/candlestick",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/drawdown",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/tracking-fund",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/fundamental",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/fs/hybrid",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/fs/non_financial",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/fs/bank",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/fs/security",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/hot/mm_ha",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/hot/mtasl",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/hot/cp",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/hot/tr_cp",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/hot/ic",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/hot/ifet_sni",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/hot/tr",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/mutual-market",
    "https://www.lixinger.com/open/api/doc?api-key=cn/index/margin-trading-and-securities-lending",
    # 大陆 - 行业接口
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/constituents/sw_2021",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/fundamental/sw_2021",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/fs/sw_2021/hybrid",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/fs/sw_2021/non_financial",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/fs/sw_2021/bank",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/fs/sw_2021/security",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/fs/sw_2021/insurance",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/hot/mm_ha/sw_2021",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/hot/mtasl/sw_2021",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/mutual-market/sw_2021",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/margin-trading-and-securities-lending/sw_2021",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/constituents/sw",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/fundamental/sw",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/fs/sw/hybrid",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/fs/sw/non_financial",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/fs/sw/bank",
    "https://www.lixinger.com/open/api/doc?api-key=cn/industry/fs/sw/security",
    # 大陆 - 基金接口
    "https://www.lixinger.com/open/api/doc?api-key=cn/fund/liquidity/subscription-net-inflow",
    "https://www.lixinger.com/open/api/doc?api-key=cn/fund/hot/tr",
    # 香港 (Hong Kong)
    "https://www.lixinger.com/open/api/doc?api-key=hk/company",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/profile",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/candlestick",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/equity-change",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/employee",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/repurchase",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/short-selling",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/operation-revenue-constitution",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/indices",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/industries",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/announcement",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/latest-shareholders",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/shareholders-equity-change",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fund-shareholders",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fund-collection-shareholders",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/dividend",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/split",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/allotment",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fundamental/non_financial",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fundamental/bank",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fundamental/security",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fundamental/insurance",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fundamental/reit",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fundamental/other_financial",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fs/non_financial",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fs/bank",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fs/security",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fs/insurance",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fs/reit",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/fs/other_financial",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/tr_dri",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/mm_ah",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/rep",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/ss",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/director_equity_change",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/npd",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/capita",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/tr",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/hot/ss_ha",
    "https://www.lixinger.com/open/api/doc?api-key=hk/company/mutual-market",
    "https://www.lixinger.com/open/api/doc?api-key=hk/index",
    # 美国 (USA)
    "https://www.lixinger.com/open/api/doc?api-key=us/index",
    "https://www.lixinger.com/open/api/doc?api-key=us/index/candlestick",
    "https://www.lixinger.com/open/api/doc?api-key=us/index/constituents",
    "https://www.lixinger.com/open/api/doc?api-key=us/index/drawdown",
    "https://www.lixinger.com/open/api/doc?api-key=us/index/tracking-fund",
    "https://www.lixinger.com/open/api/doc?api-key=us/index/fundamental",
    "https://www.lixinger.com/open/api/doc?api-key=us/index/fs/non_financial",
    "https://www.lixinger.com/open/api/doc?api-key=us/index/hot/cp",
    "https://www.lixinger.com/open/api/doc?api-key=us/index/hot/ifet_sni",
    # 宏观 (Macro)
    "https://www.lixinger.com/open/api/doc?api-key=macro/investor",
    "https://www.lixinger.com/open/api/doc?api-key=macro/credit-securities-account",
    "https://www.lixinger.com/open/api/doc?api-key=macro/stamp-duty",
    "https://www.lixinger.com/open/api/doc?api-key=macro/price-index",
    "https://www.lixinger.com/open/api/doc?api-key=macro/required-reserves",
    "https://www.lixinger.com/open/api/doc?api-key=macro/money-supply",
    "https://www.lixinger.com/open/api/doc?api-key=macro/national-debt",
    "https://www.lixinger.com/open/api/doc?api-key=macro/interest-rates",
    "https://www.lixinger.com/open/api/doc?api-key=macro/social-financing",
    "https://www.lixinger.com/open/api/doc?api-key=macro/rmb-loans",
    "https://www.lixinger.com/open/api/doc?api-key=macro/rmb-deposits",
    "https://www.lixinger.com/open/api/doc?api-key=macro/central-bank-balance-sheet",
    "https://www.lixinger.com/open/api/doc?api-key=macro/official-reserve-assets",
    "https://www.lixinger.com/open/api/doc?api-key=macro/foreign-assets",
    "https://www.lixinger.com/open/api/doc?api-key=macro/domestic-debt-securities",
    "https://www.lixinger.com/open/api/doc?api-key=macro/leverage-ratio",
    "https://www.lixinger.com/open/api/doc?api-key=macro/population",
    "https://www.lixinger.com/open/api/doc?api-key=macro/gdp",
    "https://www.lixinger.com/open/api/doc?api-key=macro/unemployment-rate",
    "https://www.lixinger.com/open/api/doc?api-key=macro/foreign-trade",
    "https://www.lixinger.com/open/api/doc?api-key=macro/bop",
    "https://www.lixinger.com/open/api/doc?api-key=macro/investment-in-fixed-assets",
    "https://www.lixinger.com/open/api/doc?api-key=macro/domestic-trade",
    "https://www.lixinger.com/open/api/doc?api-key=macro/traffic-transportation",
    "https://www.lixinger.com/open/api/doc?api-key=macro/real-estate",
    "https://www.lixinger.com/open/api/doc?api-key=macro/petroleum",
    "https://www.lixinger.com/open/api/doc?api-key=macro/energy",
    "https://www.lixinger.com/open/api/doc?api-key=macro/crude-oil",
    "https://www.lixinger.com/open/api/doc?api-key=macro/natural-gas",
    "https://www.lixinger.com/open/api/doc?api-key=macro/gold-price",
    "https://www.lixinger.com/open/api/doc?api-key=macro/silver-price",
    "https://www.lixinger.com/open/api/doc?api-key=macro/platinum-price",
    "https://www.lixinger.com/open/api/doc?api-key=macro/non-ferrous-metals",
    "https://www.lixinger.com/open/api/doc?api-key=macro/usdx",
    "https://www.lixinger.com/open/api/doc?api-key=macro/rmbidx",
    "https://www.lixinger.com/open/api/doc?api-key=macro/currency-exchange-rate",
    "https://www.lixinger.com/open/api/doc?api-key=macro/industrialization",
]


def get_filename_from_url(url: str) -> str:
    """Generate a filename from the URL."""
    parsed = urlparse(url)
    query = parse_qs(parsed.query)

    if "api-key" in query:
        api_key = query["api-key"][0]
        # Replace / with _ to create a valid filename
        return api_key.replace("/", "_") + ".md"
    else:
        return "index.md"


async def download_page(page, url: str, output_dir: Path) -> bool:
    """Download a single page and save as markdown."""
    try:
        await page.goto(url, wait_until="networkidle", timeout=30000)

        # Wait for content to fully render
        await page.wait_for_timeout(2000)

        # Try to find the main content area (API documentation typically in a specific container)
        content_selectors = [
            ".api-doc-content",
            ".doc-content",
            ".content",
            "main",
            ".main-content",
            "#app > div > div:nth-child(2)",  # Common Vue app structure
        ]

        html_content = None
        for selector in content_selectors:
            try:
                element = page.locator(selector).first
                if await element.count() > 0:
                    html_content = await element.inner_html()
                    if len(html_content) > 100:  # Ensure we have meaningful content
                        break
            except:
                continue

        if not html_content:
            # Fallback: get the whole body
            html_content = await page.locator("body").inner_html()

        # Convert HTML to markdown
        markdown_content = md(html_content, heading_style="ATX")

        # Clean up markdown
        lines = markdown_content.split("\n")
        cleaned_lines = []
        for line in lines:
            # Skip navigation-related lines
            if any(
                skip in line.lower()
                for skip in ["网站链接", "友情链接", "快速链接", "©2016"]
            ):
                continue
            cleaned_lines.append(line)

        markdown_content = "\n".join(cleaned_lines)

        # Generate filename and save
        filename = get_filename_from_url(url)
        filepath = output_dir / filename

        # Add URL as header
        full_content = f"# Source: {url}\n\n{markdown_content}"

        filepath.write_text(full_content, encoding="utf-8")
        print(f"✓ Saved: {filename}")
        return True

    except Exception as e:
        print(f"✗ Error downloading {url}: {e}")
        return False


async def main():
    """Main function to download all documentation pages."""
    output_dir = Path(__file__).parent / "docs"
    output_dir.mkdir(exist_ok=True)

    print(f"Downloading {len(API_URLS)} documentation pages...")
    print(f"Output directory: {output_dir}")
    print("-" * 60)

    success_count = 0
    failed_urls = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
        )
        page = await context.new_page()

        for i, url in enumerate(API_URLS, 1):
            print(f"[{i}/{len(API_URLS)}] Downloading: {url}")

            if await download_page(page, url, output_dir):
                success_count += 1
            else:
                failed_urls.append(url)

            # Rate limiting
            await page.wait_for_timeout(500)

        await browser.close()

    print("-" * 60)
    print(f"Downloaded: {success_count}/{len(API_URLS)} pages")

    if failed_urls:
        print(f"\nFailed URLs ({len(failed_urls)}):")
        for url in failed_urls:
            print(f"  - {url}")


if __name__ == "__main__":
    asyncio.run(main())
