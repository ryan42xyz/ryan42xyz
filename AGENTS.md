# AGENTS.md

This document provides coding agents with essential information about this repository's structure, conventions, and workflows.

## Repository Overview

This is a **personal tech identity repository** containing:
- LaTeX resume files (`resume.tex`, `resume-expand.tex`)
- Interview preparation materials (Kubernetes upgrades, traffic switching, monitoring, on-call)
- Technical documentation and design notes
- Python build tooling for PDF generation

**Primary stack**: LaTeX (XeLaTeX), Python 3, Markdown

## Build Commands

### Build Resume PDF

```bash
# Generate PDF from resume.tex (runs xelatex twice for refs/hyperref)
python3 tex2pdf.py
```

**Expected output**: `resume.pdf` with validation message: `PDF header OK, ready to use.`

### Build Specific Resume Variant

To build `resume-expand.tex` instead of `resume.tex`, modify `tex2pdf.py:10-11`:

```python
TEX = SCRIPT_DIR / "resume-expand.tex"
PDF = SCRIPT_DIR / "resume-expand.pdf"
```

Then run: `python3 tex2pdf.py`

### Verify PDF Integrity

The build script automatically:
1. Checks PDF file existence
2. Validates PDF header (`%PDF` magic bytes)
3. Reports file size in KB

### One-Time Setup (LaTeX)

```bash
# Install BasicTeX (macOS only)
brew install --cask basictex

# Install required LaTeX packages
sudo /usr/local/texlive/2025basic/bin/universal-darwin/tlmgr update --self
sudo /usr/local/texlive/2025basic/bin/universal-darwin/tlmgr install titlesec enumitem hyperref setspace fontspec
```

**Note**: Adjust TeX Live version path (e.g., `2025basic`) based on your installation. Check with: `ls /usr/local/texlive/*/bin/*/tlmgr`

## Testing & Validation

### No Automated Tests

This repository does not have a test suite. Validation is manual:

1. **Build validation**: Run `python3 tex2pdf.py` and verify success message
2. **Visual inspection**: Open generated PDF and check formatting, content, links
3. **Link validation**: Verify hyperlinks in PDF (email, GitHub, blog)

### Single File Testing

To validate a specific LaTeX file:

```bash
# Build and inspect a single .tex file
xelatex -interaction=nonstopmode -halt-on-error resume.tex
# Verify output
open resume.pdf
```

## Code Style Guidelines

### Python (tex2pdf.py)

**Imports**:
- Standard library only (no external dependencies)
- Order: `os`, `subprocess`, `sys`, `pathlib`
- Group by: stdlib → third-party → local (none in this repo)

**Formatting**:
- **Line length**: 88 characters (Black-compatible)
- **Indentation**: 4 spaces
- **Quotes**: Double quotes for strings, single quotes for dict keys
- **Trailing commas**: Yes, in multi-line structures

**Types**:
- Use `Path` objects for filesystem operations (not raw strings)
- Type hints not currently used, but preferred for new code

**Naming conventions**:
- Constants: `UPPER_SNAKE_CASE` (e.g., `SCRIPT_DIR`, `TEX_BIN`)
- Functions: `snake_case` (e.g., `main()`)
- Variables: `snake_case` (e.g., `size_kb`)

**Error handling**:
- Exit with non-zero code on failure: `sys.exit(1)` or `sys.exit(r.returncode)`
- Print errors to `stderr`: `print(..., file=sys.stderr)`
- Validate inputs before processing (e.g., check `TEX.exists()`)

**Docstrings**:
- Module-level docstring describing purpose and usage
- Format: Single-line summary, then blank line, then details
- Example: See `tex2pdf.py:1-3`

### LaTeX (resume.tex)

**Structure**:
- Logical sections with comment headers: `% ---------- Section Name ----------`
- Order: Packages → Fonts → Styles → Document
- Keep preamble modular and well-commented

**Formatting**:
- Consistent indentation (2 spaces inside environments)
- One setting per line in package options
- Align similar commands vertically for readability

**Naming**:
- Custom colors: `PascalCase` (e.g., `CompanyColor`)
- Macro names: `\camelCase` or `\PascalCase`

**Fonts**:
- Default: Times New Roman (`\setmainfont{Times New Roman}`)
- Fallback to system fonts if unavailable

**Hyperlinks**:
- Use `\href{url}{text}` for clickable links
- Set `colorlinks=true, urlcolor=black` for print-friendly output

### Markdown

**Formatting**:
- Use `##` for main sections, `###` for subsections
- Code blocks: Triple backticks with language identifier (```bash, ```python)
- Lists: `-` for unordered, `1.` for ordered
- Emphasis: `**bold**`, `*italic*`, `` `code` ``

**Structure**:
- Start with H1 title (`# Title`)
- Include clear section headers
- Use horizontal rules (`---`) sparingly

**Links**:
- Inline format: `[text](url)`
- Reference format for repeated links: `[text][ref]` + `[ref]: url` at bottom

**Technical writing style**:
- Concise, imperative tone (e.g., "Run the command" not "You should run")
- Focus on "why" and "what", minimize "how" unless critical
- Use code examples for clarity

## File Organization

```
github-profile/
├── resume.tex               # Primary resume (concise version)
├── resume-expand.tex        # Extended resume variant
├── tex2pdf.py               # Build script for PDF generation
├── BUILD.md                 # Build instructions (Chinese)
├── README.md                # Profile README
├── .gitignore               # Ignores LaTeX build artifacts
├── interview-*.md           # Interview prep materials
├── *_story-*.md             # Interview narratives
├── monitoring_design.md     # Monitoring design notes
├── thinking/                # Design philosophy and notes
│   └── platform_engineering.md
└── *.pdf, *.aux, *.log      # Generated artifacts (gitignored)
```

**Do not commit**:
- LaTeX build artifacts: `*.aux`, `*.log`, `*.out`, `*.fls`, `*.fdb_latexmk`, `*.synctex.gz`
- These are listed in `.gitignore` and auto-generated by build script

## Git Workflow

**Commit message style** (from recent commits):
- Imperative mood: "Add", "Update", "Fix" (not "Added", "Updated")
- Concise subject line (50 chars preferred)
- No body/footer for simple changes
- Examples:
  - `Add blog and GitHub profile links`
  - `Update resume.tex and resume.pdf`
  - `Add resume.tex, resume.pdf, and local build script`

**When to commit PDFs**:
- Commit generated PDFs (`resume.pdf`, `resume-expand.pdf`) for easy access
- Update PDF whenever `.tex` source changes

**Branch strategy**:
- Single-user repo: work on `main` or feature branches as needed
- No strict branching model enforced

## Common Tasks

### Update Resume Content

1. Edit `resume.tex` or `resume-expand.tex`
2. Run `python3 tex2pdf.py` to generate PDF
3. Verify output: `open resume.pdf`
4. Commit both `.tex` and `.pdf`: `git add resume.tex resume.pdf && git commit -m "Update resume with [change description]"`

### Add Interview Prep Material

1. Create new Markdown file: `interview-N-topic_name.md`
2. Follow existing structure (see `interview-1-k8s_upgrade.md` for reference)
3. Add to README.md if publicly referenced
4. Commit: `git add interview-N-*.md && git commit -m "Add interview prep: [topic]"`

### Modify Build Script

1. Edit `tex2pdf.py`
2. Test build: `python3 tex2pdf.py`
3. Verify error handling by introducing intentional errors (e.g., rename `.tex` file)
4. Restore and commit: `git add tex2pdf.py && git commit -m "Update build script: [change description]"`

## Troubleshooting

**Error: `xelatex: command not found`**
- Install BasicTeX: `brew install --cask basictex`
- Script auto-adds `/Library/TeX/texbin` to PATH

**Error: `titlesec.sty not found`**
- Install missing packages: See "One-Time Setup (LaTeX)" section above

**Error: `resume.pdf is not a valid PDF file`**
- Check LaTeX compilation errors in console output
- Review `.log` file for detailed error messages
- Common causes: Missing fonts, syntax errors in `.tex`

**PDF builds but looks wrong**
- Clear build artifacts: `rm *.aux *.log *.out`
- Rebuild: `python3 tex2pdf.py`
- Verify font installation (Times New Roman required)

## Agent-Specific Notes

- **No linter/formatter**: No Python linter (flake8/pylint) or formatter (black) configured. Follow PEP 8 conventions.
- **No CI/CD**: No automated checks. Validate locally before committing.
- **No package manager**: Python script uses stdlib only. No `requirements.txt` or `pyproject.toml`.
- **Platform**: Developed on macOS. LaTeX paths assume macOS TeX Live installation.
- **Language**: Mixed Chinese/English content. Resume is English; BUILD.md is Chinese.
