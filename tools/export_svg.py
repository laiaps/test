#!/usr/bin/env python3
import argparse
import os
import sys

def ensure_cairosvg_installed() -> None:
    try:
        import cairosvg  # noqa: F401
    except Exception:
        print("Installing cairosvg...", flush=True)
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cairosvg==2.7.1"])  # pinned


def convert(svg_path: str, png_path: str, scale: float = 1.0) -> None:
    from cairosvg import svg2png
    with open(svg_path, "rb") as f:
        svg_bytes = f.read()
    os.makedirs(os.path.dirname(png_path), exist_ok=True)
    svg2png(bytestring=svg_bytes, write_to=png_path, scale=scale)
    print(f"Exported {png_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Export an SVG to PNG")
    parser.add_argument("svg", help="Absolute path to the SVG file")
    parser.add_argument("png", help="Absolute path to the output PNG file")
    parser.add_argument("--scale", type=float, default=1.0, help="Scale factor (default 1.0)")
    args = parser.parse_args()

    if not os.path.isabs(args.svg) or not os.path.isabs(args.png):
        print("Please use absolute paths for both input and output.")
        sys.exit(2)

    ensure_cairosvg_installed()
    convert(args.svg, args.png, args.scale)


if __name__ == "__main__":
    main()

