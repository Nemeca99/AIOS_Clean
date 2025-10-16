# AIOS Test Suite Notes

## File Creation Log (Engineering Work)

The following configuration and test files were **created** (not modified) during V5.1 test refinement.
This is engineering work, outside the Auditor's modify-only boundary.

**Created Files:**
- `pytest.ini` - Test configuration with markers
- `.coveragerc` - Coverage configuration
- `tests/conftest.py` - Pytest hooks and fixtures
- `tests/test_aios_core_files.py` - Comprehensive AIOS core file testing
- `tests/test_streamlit_vendor_sanity.py` - Vendor code sanity checks
- `tests/test_system_integration.py` - System integration tests
- `tests/test_top_level_imports.py` - Import health checks
- `consciousness_core/__init__.py` - Package marker
- `data_core/__init__.py` - Package marker
- `enterprise_core/__init__.py` - Package marker
- `support_core/__init__.py` - Package marker

**Role Separation:**
- **External Auditor GPT:** Design-time architectural validation (advisory only, no file creation)
- **Internal Auditor (V3 Sovereign):** Code quality, static analysis, self-healing (modify-only)
- **Engineer (Travis + Cursor):** Implementation and file creation

## Test Architecture

**Separation Principle:**
- AIOS Core Tests: Test YOUR code (369 Python files)
- Vendor Tests: Sanity-check third-party code (sample only)

**Deterministic Sampling:**
- Vendor files sorted before slicing (first 50 files, stable across runs)
- Template files explicitly skipped

**Stats Accuracy:**
- `conftest.py` reads actual pytest stats from terminal reporter
- JSON artifact has accurate pass/fail/skip counts (not estimated)

## Coverage Policy

**Threshold:** 90% minimum (`fail_under = 90` in `.coveragerc`)

**Excluded from coverage:**
- `streamlit_core/**` (vendor code)
- `*/__init__.py` (stub files)
- Archive and test directories
- Generated version files

## CI Integration (Future)

**Recommended test lanes:**
```bash
# Daily pipeline
pytest -m "core and not vendor" --cov --cov-fail-under=90

# Nightly pipeline
pytest -m "vendor"
```

---
**Version:** 5.1.0  
**Last Updated:** 2025-10-16  
**Auditor:** AIOS External Auditor GPT  
**Engineer:** Travis Miner + Cursor (Kia)

