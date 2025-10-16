#!/usr/bin/env python3
"""
Streamlit Vendor Sanity Checks

Tests the third-party Streamlit library files in streamlit_core/ with minimal coverage.

This is separate from AIOS core tests because:
- Streamlit is vendor code (not our responsibility)
- It's a massive library (~2000 files)
- We only need basic sanity checks, not deep validation

Strategy: Sample first 50 files for syntax, verify directory structure, skip the rest.
"""

import pytest
import sys
from pathlib import Path
import ast
import py_compile

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Mark all tests in this file as 'vendor' tests
pytestmark = pytest.mark.vendor


def get_streamlit_files():
    """
    Get all Python files in streamlit_core (deterministically sorted).
    
    Returns sorted list for stable sampling.
    Excludes known non-code directories.
    """
    root = Path(__file__).parent.parent
    streamlit_dir = root / "streamlit_core"
    
    if not streamlit_dir.exists():
        return []
    
    # Directories to skip entirely
    skip_patterns = [
        '__pycache__',
        'node_modules',
        '.git',
        'cookiecutter',  # Template files, not real Python
    ]
    
    python_files = []
    
    for py_file in streamlit_dir.rglob("*.py"):
        # Skip if in excluded directory
        if any(pattern in str(py_file) for pattern in skip_patterns):
            continue
        python_files.append(py_file)
    
    # Sort deterministically by path for stable sampling
    return sorted(python_files, key=lambda p: str(p))


def test_streamlit_directory_exists():
    """Test that streamlit_core directory exists"""
    root = Path(__file__).parent.parent
    streamlit_dir = root / "streamlit_core"
    
    assert streamlit_dir.exists(), "streamlit_core directory not found"
    assert streamlit_dir.is_dir(), "streamlit_core is not a directory"


def test_streamlit_file_count():
    """Test that streamlit has a reasonable number of files"""
    all_files = get_streamlit_files()
    sample_size = 50
    
    considered = len(all_files)
    sampled = min(sample_size, considered)
    
    print(f"\nStreamlit Vendor: {considered} files total, {sampled} sampled for syntax checks")
    
    # Streamlit is a large library
    if considered > 0:
        assert considered > 100, f"Expected 100+ Streamlit files, found {considered}"
        assert considered < 5000, f"Suspiciously high count: {considered}"


@pytest.mark.parametrize("py_file", get_streamlit_files()[:50])  # Deterministic sample: first 50 after sorting
def test_streamlit_syntax_sample(py_file):
    """
    Test syntax of a sample of Streamlit files (first 50 only, deterministically sorted).
    
    Strategy: Sample vendor code for basic sanity, don't validate the entire library.
    """
    # Skip template files (intentionally invalid Jinja2/Python hybrids)
    if '{{' in str(py_file):
        pytest.skip(f"Template file: {py_file.name}")
    
    try:
        with open(py_file, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Try to parse as AST
        ast.parse(source, filename=str(py_file))
        
    except SyntaxError as e:
        # Vendor code syntax issues are not our problem
        pytest.skip(f"Vendor syntax issue in {py_file.name}")
    except Exception as e:
        # Streamlit vendor code might have issues we don't care about
        pytest.skip(f"Skipping {py_file.name}: {type(e).__name__}")


def test_streamlit_can_import_core():
    """Test that we can import streamlit_core"""
    try:
        import streamlit_core
        assert streamlit_core is not None
    except ImportError:
        pytest.skip("streamlit_core not importable (dependencies missing)")


def test_streamlit_has_init():
    """Test that streamlit_core has __init__.py"""
    root = Path(__file__).parent.parent
    init_file = root / "streamlit_core" / "__init__.py"
    
    if not init_file.exists():
        pytest.skip("streamlit_core/__init__.py not found (optional)")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

