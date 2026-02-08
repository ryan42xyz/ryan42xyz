#!/usr/bin/env python3
"""Build resume.tex to PDF using xelatex, then verify the PDF.
Requires TeX: brew install --cask basictex (once), then run this script."""
import os
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
TEX = SCRIPT_DIR / "resume.tex"
PDF = SCRIPT_DIR / "resume.pdf"

# Prefer TeX bin so script works right after brew install (no terminal restart)
TEX_BIN = Path("/Library/TeX/texbin")
ENV = os.environ.copy()
if TEX_BIN.exists():
    ENV["PATH"] = str(TEX_BIN) + os.pathsep + ENV.get("PATH", "")


def main():
    if not TEX.exists():
        print(f"Not found: {TEX}", file=sys.stderr)
        sys.exit(1)
    # Run xelatex twice for refs/hyperref
    for i in range(2):
        r = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", str(TEX)],
            cwd=SCRIPT_DIR,
            capture_output=True,
            text=True,
            env=ENV,
        )
        if r.returncode != 0:
            print(r.stderr or r.stdout, file=sys.stderr)
            sys.exit(r.returncode)
    # Verify PDF
    if not PDF.exists():
        print("Error: resume.pdf was not created", file=sys.stderr)
        sys.exit(1)
    raw = PDF.read_bytes()[:8]
    if not raw.startswith(b"%PDF"):
        print("Error: resume.pdf is not a valid PDF file", file=sys.stderr)
        sys.exit(1)
    size_kb = PDF.stat().st_size / 1024
    print(f"Done: {PDF} ({size_kb:.1f} KB)")
    print("PDF header OK, ready to use.")


if __name__ == "__main__":
    main()
