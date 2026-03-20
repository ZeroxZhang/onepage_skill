#!/usr/bin/env python3
"""
OnePage Generator — HTML to PNG capture script.

Uses Playwright to render an HTML file and capture it as a high-quality PNG image.
Supports fixed dimensions and auto-height (full-page) modes.

Usage:
    python3 capture.py <input.html> --output <output.png> --width <px> [--height <px|auto>] [--scale <factor>]

Examples:
    # Portrait (auto height)
    python3 capture.py onepage.html --output onepage.png --width 800 --height auto

    # Landscape (fixed)
    python3 capture.py onepage.html --output onepage.png --width 1920 --height 1080

    # Square (fixed)
    python3 capture.py onepage.html --output onepage.png --width 1080 --height 1080

    # High-DPI (2x scale)
    python3 capture.py onepage.html --output onepage.png --width 800 --height auto --scale 2
"""

import argparse
import asyncio
import os
import sys


async def capture(input_path: str, output_path: str, width: int, height: str, scale: float):
    """Render HTML and capture screenshot."""
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("ERROR: Playwright is not installed.")
        print("Run: pip install playwright && python -m playwright install chromium")
        sys.exit(1)

    abs_input = os.path.abspath(input_path)
    if not os.path.exists(abs_input):
        print(f"ERROR: Input file not found: {abs_input}")
        sys.exit(1)

    file_url = f"file://{abs_input}"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(
            viewport={"width": width, "height": 800},
            device_scale_factor=scale,
        )

        # Navigate and wait for fonts and rendering to complete
        await page.goto(file_url, wait_until="networkidle")
        # Extra wait for font loading
        await page.wait_for_timeout(2000)

        if height == "auto":
            # Full-page screenshot (auto height)
            await page.screenshot(
                path=output_path,
                full_page=True,
                type="png",
            )
        else:
            # Fixed viewport screenshot
            h = int(height)
            await page.set_viewport_size({"width": width, "height": h})
            await page.screenshot(
                path=output_path,
                full_page=False,
                clip={"x": 0, "y": 0, "width": width, "height": h},
                type="png",
            )

        await browser.close()

    print(f"OK: Screenshot saved to {output_path}")
    print(f"    Dimensions: {width}px × {height}px (scale: {scale}x)")


def main():
    parser = argparse.ArgumentParser(description="Capture HTML as PNG image.")
    parser.add_argument("input", help="Path to input HTML file")
    parser.add_argument("--output", "-o", required=True, help="Path to output PNG file")
    parser.add_argument("--width", "-w", type=int, required=True, help="Viewport width in pixels")
    parser.add_argument("--height", default="auto", help="Viewport height in pixels, or 'auto' for full page")
    parser.add_argument("--scale", "-s", type=float, default=2.0, help="Device scale factor (default: 2.0 for Retina)")
    args = parser.parse_args()

    asyncio.run(capture(args.input, args.output, args.width, args.height, args.scale))


if __name__ == "__main__":
    main()