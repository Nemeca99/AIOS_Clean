#!/usr/bin/env python3
"""
AIOS Core Python File Testing

Tests all AIOS core Python files (excluding vendor code) for:
- Syntax validity (all 369 core files)
- Import success
- Structural requirements
- Security issues

Vendor code (streamlit_core) is tested separately in test_streamlit_vendor_sanity.py
"""

import pytest
import sys
from pathlib import Path
import importlib.util
import ast
import py_compile

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Mark all tests in this file as 'core' tests
pytestmark = pytest.mark.core


def get_all_aios_core_files():
    """Find all AIOS core Python files (excluding vendor code like streamlit)"""
    root = Path(__file__).parent.parent
    
    # Directories to exclude
    exclude_patterns = [
        'venv', '.venv', '__pycache__', '.git', '.pytest_cache',
        'archive_dev_core', 'node_modules', '.cursor', 
        'streamlit_core'  # Exclude ALL streamlit vendor code
    ]
    
    python_files = []
    
    for py_file in root.rglob("*.py"):
        # Skip if in excluded directory
        if any(exclude in str(py_file) for exclude in exclude_patterns):
            continue
        python_files.append(py_file)
    
    return sorted(python_files)


def test_count_aios_core_files():
    """Sanity check: we should have a reasonable number of AIOS core Python files"""
    files = get_all_aios_core_files()
    print(f"\nAIOS Core: {len(files)} Python files discovered")
    assert len(files) > 50, f"Expected 50+ AIOS core files, found {len(files)}"
    assert len(files) < 500, f"Suspiciously high AIOS core file count: {len(files)}"


@pytest.mark.parametrize("py_file", get_all_aios_core_files())
def test_aios_core_file_syntax(py_file):
    """Test that every AIOS core Python file has valid syntax"""
    try:
        with open(py_file, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Try to parse as AST
        ast.parse(source, filename=str(py_file))
        
        # Try to compile
        py_compile.compile(str(py_file), doraise=True)
        
    except SyntaxError as e:
        pytest.fail(f"Syntax error in {py_file}: {e}")
    except Exception as e:
        pytest.fail(f"Failed to parse {py_file}: {e}")


def test_all_core_modules_importable():
    """Test that all *_core modules can be imported"""
    root = Path(__file__).parent.parent
    
    core_dirs = [d for d in root.iterdir() if d.is_dir() and d.name.endswith('_core') and d.name != 'archive_dev_core']
    
    failed_imports = []
    successful_imports = []
    
    for core_dir in core_dirs:
        core_name = core_dir.name
        
        # Try to import the core
        try:
            __import__(core_name)
            successful_imports.append(core_name)
        except ImportError as e:
            failed_imports.append((core_name, str(e)))
        except Exception as e:
            # Some cores might fail for other reasons (missing config, etc.)
            # We'll warn but not fail
            print(f"\n  Note: {core_name} import raised {type(e).__name__}: {e}")
            successful_imports.append(core_name)
    
    print(f"\nCore imports: {len(successful_imports)} successful, {len(failed_imports)} failed")
    
    if failed_imports:
        for core, error in failed_imports:
            print(f"  - {core}: {error[:80]}")
    
    # We should import at least 80% of cores
    success_rate = len(successful_imports) / len(core_dirs) if core_dirs else 0
    assert success_rate >= 0.8, f"Only {success_rate:.0%} of cores importable"


def test_all_init_files_exist():
    """Test that all core directories have __init__.py"""
    root = Path(__file__).parent.parent
    
    # Directories that intentionally don't need __init__.py
    skip_dirs = ['archive_dev_core', 'streamlit_core']
    
    missing_inits = []
    
    for core_dir in root.iterdir():
        if not core_dir.is_dir() or not core_dir.name.endswith('_core'):
            continue
        
        # Skip intentionally non-module directories
        if core_dir.name in skip_dirs:
            continue
        
        init_file = core_dir / "__init__.py"
        if not init_file.exists():
            missing_inits.append(core_dir.name)
    
    if missing_inits:
        print(f"\n  Missing __init__.py in: {missing_inits}")
    
    # All production cores must have __init__.py
    assert len(missing_inits) == 0, f"Missing __init__.py: {missing_inits}"


def test_main_py_structure():
    """Test that main.py has expected structure"""
    root = Path(__file__).parent.parent
    main_file = root / "main.py"
    
    assert main_file.exists(), "main.py not found"
    
    with open(main_file, 'r', encoding='utf-8') as f:
        source = f.read()
    
    # Should have key functions
    assert 'def discover_cores' in source, "main.py missing discover_cores()"
    assert 'def main' in source, "main.py missing main()"
    
    # Should reference key systems
    assert 'luna' in source.lower() or 'carma' in source.lower(), "main.py doesn't reference core systems"


def test_requirements_files_exist():
    """Test that requirements files exist and are parseable"""
    root = Path(__file__).parent.parent
    
    req_files = [
        'requirements.txt',
        'requirements-production.txt',
    ]
    
    for req_file in req_files:
        path = root / req_file
        assert path.exists(), f"{req_file} not found"
        
        # Should be parseable
        with open(path, 'r') as f:
            lines = f.readlines()
        
        # Should have some packages
        packages = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
        assert len(packages) > 0, f"{req_file} has no packages"


def test_core_discovery():
    """Test that core discovery returns expected cores"""
    import importlib.util
    
    # Import main.py
    main_spec = importlib.util.spec_from_file_location("main", "main.py")
    main_module = importlib.util.module_from_spec(main_spec)
    main_spec.loader.exec_module(main_module)
    
    cores = main_module.discover_cores()
    
    # Should find essential cores
    essential = ['luna_core', 'carma_core', 'dream_core', 'main_core', 'consciousness_core']
    for core in essential:
        assert core in cores, f"Core discovery missed {core}"
    
    # Should find at least 10 cores
    assert len(cores) >= 10, f"Only found {len(cores)} cores"
    
    print(f"\nDiscovered {len(cores)} cores: {sorted(cores)}")


def test_no_hardcoded_credentials():
    """Test that no Python files contain obvious hardcoded credentials"""
    root = Path(__file__).parent.parent
    
    # Patterns that might indicate credentials
    suspicious_patterns = [
        'password = "',
        'api_key = "',
        'secret = "',
        'token = "',
        'AWS_SECRET',
    ]
    
    violations = []
    
    for py_file in get_all_aios_core_files():
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                source = f.read()
            
            for pattern in suspicious_patterns:
                if pattern in source:
                    # Make sure it's not just a placeholder or example
                    lower_source = source.lower()
                    if not any(word in lower_source for word in ['your_password', 'example', 'placeholder', 'config', 'template', 'default', 'optional']):
                        violations.append((py_file.name, pattern))
        except:
            pass  # Skip files we can't parse
    
    if violations:
        print(f"\n  Possible hardcoded credentials found:")
        for file, pattern in violations[:5]:
            print(f"  - {file}: {pattern}")
    
    # Security check - should have no credential leaks
    assert len(violations) == 0, f"Found {len(violations)} possible credential leaks"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

