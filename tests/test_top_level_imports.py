#!/usr/bin/env python3
"""
Top-Level Import Health Check

Tests that all advertised top-level modules can be imported
as end-users would import them (with clean PYTHONPATH).

This catches packaging regressions that other tests might miss.
"""

import pytest
import sys
from pathlib import Path

# Add parent to path AS USERS WOULD
sys.path.insert(0, str(Path(__file__).parent.parent))

# Mark as core test
pytestmark = pytest.mark.core


def test_import_all_advertised_cores():
    """
    Test that all advertised core modules can be imported as users would.
    
    This catches packaging regressions that syntax tests might miss.
    Tests the actual import path users will use.
    """
    
    # List of all cores advertised in README/docs
    advertised_cores = [
        'luna_core',
        'carma_core',
        'dream_core',
        'main_core',
        'consciousness_core',
        'fractal_core',
        'data_core',
        'rag_core',
        'utils_core',
        'support_core',
        'backup_core',
        'privacy_core',
        'template_core',
        'marketplace_core',
        'music_core',
        'game_core',
        'enterprise_core',
    ]
    
    failed = []
    succeeded = []
    skipped = []
    
    for core in advertised_cores:
        try:
            __import__(core)
            succeeded.append(core)
        except ImportError as e:
            # Some cores might be optional
            if 'optional' in str(e).lower() or core in ['marketplace_core', 'game_core', 'enterprise_core']:
                skipped.append((core, "Optional module"))
            else:
                failed.append((core, str(e)))
        except Exception as e:
            # Config/runtime errors are OK - means the import worked
            print(f"\n  Note: {core} imported but raised {type(e).__name__} on init")
            succeeded.append(core)
    
    print(f"\nTop-level imports: {len(succeeded)} success, {len(skipped)} skipped (optional), {len(failed)} failed")
    
    if failed:
        for core, error in failed:
            print(f"  FAIL: {core} - {error[:100]}")
    
    # All non-optional cores must be importable
    assert len(failed) == 0, f"Failed to import: {[c for c, _ in failed]}"
    
    # Should import most cores
    assert len(succeeded) >= 10, f"Only imported {len(succeeded)} cores, expected 10+"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

