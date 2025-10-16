# Contributing to AIOS_clean

Thank you for your interest in contributing to AIOS_clean, the canonical Adaptive Intelligence Operating System baseline.

## File Organization

### Production Files (User-Facing)

Everything outside `archive_dev_core/` is public-facing and uploaded to GitHub:

- **Root:** README.md, AIOS_MANUAL.md, AIOS_EXECUTIVE_SUMMARY.md, MANUAL_TOC.md, SYSTEM_CARD.md
- **Validation:** V1_TESTING_COMPLETE.md, validation reports referenced by README
- **Core code:** All `*_core/` folders with production implementations
- **Documentation:** Essential architecture docs in `docs/`
- **Infrastructure:** main.py, streamlit_app.py, setup.ps1, requirements.txt

### Development Files (Dev-Only)

Everything inside `archive_dev_core/` is local-only and **NOT uploaded to GitHub**:

- Session summaries and build logs (SESSION_*.md, *_COMPLETE.md)
- Development archaeology and lineage docs
- Historical status files and integration summaries
- Generated files (HTML/PDF versions of manuals)
- Test scripts and demo files
- Workspace files (.code-workspace)
- **Preserved locally for lineage, hidden from production repo**

## Adding Files

**User-facing documentation:**
- Add to root (if referenced by README) or `docs/` (if essential architecture)
- Ensure it's referenced somewhere (README, MANUAL, or another canonical doc)

**Development notes and session logs:**
- Add to `archive_dev_core/` (automatically gitignored)
- Organize by category (docs/, scripts/, etc.)

**Core-specific documentation:**
- Add to `<core_name>/docs/` if it documents that core's internals
- Reference it from the core's README.md

**Test scripts:**
- Production tests: `tests/` folder
- Dev/demo scripts: `archive_dev_core/scripts/`

## Core Folder Structure

Each `*_core/` folder should have:

```
*_core/
├── README.md           # What it does, how to use it
├── __init__.py         # Python module init
├── *.py                # Core implementation files
├── config/             # Configuration files (optional)
│   └── *.json
└── docs/               # Core-specific documentation (optional)
    └── *.md
```

## Housekeeping

To maintain clean separation between production and dev files, run:

```powershell
# Check what would be moved to archive
py scripts\housekeep_repo.py --dry-run

# Actually move dev files to archive
py scripts\housekeep_repo.py

# Verify clean state
py scripts\housekeep_repo.py --verify
```

The housekeeping script automatically:
- Moves session summaries, integration docs, and build logs to archive
- Archives test/demo scripts
- Archives workspace files
- Preserves all files locally (no deletions)
- Generates reports in `archive_dev_core/housekeeping_reports/`

## Updating Canonical Documentation

The three core documents are protected and require special care:

1. **AIOS_MANUAL.md** - Complete system documentation (37k+ lines)
2. **AIOS_EXECUTIVE_SUMMARY.md** - High-level overview
3. **MANUAL_TOC.md** - Navigation index with line numbers

See `docs/CANONICAL_DOCS_UPDATE_GUIDE.md` for the update protocol.

After updating the manual:
```powershell
py scripts\update_manual_complete.py
```

This regenerates the TOC and rebuilds the RAG database.

## Pull Request Guidelines

1. **Test your changes:** Run `pytest` before submitting
2. **Update documentation:** If you add features, document them
3. **Follow standards:** See `STANDARDS_MANIFEST.md` and `docs/AIOS_ARCHITECTURAL_STANDARDS.md`
4. **Clean commits:** Use clear commit messages
5. **No dev files:** Ensure `archive_dev_core/` is not included (it's gitignored)

## Code Style

- Python: PEP 8 with 4-space indents
- Docstrings: Google style
- Type hints: Use where helpful
- Logging: Use `support_core.logger`
- Configuration: JSON files in `config/` folders

## Security

- Never commit API keys or credentials
- Use environment variables for secrets
- Test sandbox isolation for any code execution
- Report security issues privately to the maintainer

## Questions?

- Read `docs/WHY_AIOS.md` for philosophy
- Read `docs/AIOS_QUICK_CONTEXT.md` for architecture overview
- Check `AIOS_MANUAL.md` for detailed documentation
- Review `docs/ARBITER_DUAL_AUDIT_ARCHITECTURE.md` for quality systems

---

**Remember:** Outside `archive_dev_core/` = For users. Inside `archive_dev_core/` = For Travis (dev-only, local).

**No deletions. Only organization.**

