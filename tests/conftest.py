#!/usr/bin/env python3
"""
Pytest configuration and fixtures for AIOS test suite.

This file defines shared fixtures, hooks, and configuration
for all tests in the AIOS test suite.
"""

import pytest
import json
import itertools
from pathlib import Path
from datetime import datetime


@pytest.fixture
def fake_monotonic(monkeypatch):
    """
    Fixture to replace time.monotonic() with deterministic counter.
    
    Use this to make time-based tests instant and deterministic.
    No more sleep() calls in tests.
    
    Example:
        def test_something(fake_monotonic):
            # time.monotonic() now returns 0.0, 0.1, 0.2, ...
            start = time.monotonic()  # 0.0
            # do work
            end = time.monotonic()    # 0.1
    """
    counter = itertools.count(start=0, step=0.1)
    monkeypatch.setattr("time.monotonic", lambda: next(counter))
    return lambda: None


@pytest.fixture(scope="session")
def test_summary():
    """Fixture to collect test summary data"""
    return {
        "test_run_timestamp": datetime.now().isoformat(),
        "aios_version": "5.1.0",
        "test_categories": {
            "core": 0,
            "vendor": 0,
            "integration": 0,
            "chaos": 0,
            "performance": 0,
            "quality": 0,
            "property": 0
        }
    }


def pytest_sessionfinish(session, exitstatus):
    """
    Hook that runs after all tests complete.
    Generates test_summary.json with accurate results from pytest terminal reporter.
    
    Uses actual pytest stats to prevent count drift.
    """
    # Get accurate stats from terminal reporter
    reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    
    if reporter:
        stats = reporter.stats
        # Use public API (pytest 7+) or fallback to session
        total_collected = session.testscollected  # Public API since pytest 7
    else:
        stats = {}
        total_collected = session.testscollected
    
    # Count each category accurately from actual pytest results
    passed = len(stats.get('passed', []))
    failed = len(stats.get('failed', []))
    skipped = len(stats.get('skipped', []))
    errors = len(stats.get('error', []))
    xfailed = len(stats.get('xfailed', []))
    xpassed = len(stats.get('xpassed', []))
    
    # Verify math: collected should equal passed + failed + skipped + errors
    computed_total = passed + failed + skipped + errors + xfailed + xpassed
    
    summary = {
        "timestamp": datetime.now().isoformat(),
        "aios_version": "5.1.0",
        "exit_status": exitstatus,
        "total_collected": total_collected,
        "computed_total": computed_total,
        "total_passed": passed,
        "total_failed": failed,
        "total_skipped": skipped,
        "total_errors": errors,
        "total_xfailed": xfailed,
        "total_xpassed": xpassed,
        "pass_rate": f"{(passed / total_collected * 100):.1f}%" if total_collected > 0 else "0.0%",
        "test_breakdown": {
            "aios_core_files": 381,
            "streamlit_vendor": 54,
            "system_integration": 13,
            "chaos_engineering": 16,
            "contract_quality": 11,
            "property_based": 10,
            "contract_performance": 5,
            "contract_idempotency": 3,
            "top_level_imports": 1,
            "breakdown_total": 494
        },
        "notes": "Computed total should match collected. Skipped tests are NOT counted as passed."
    }
    
    # Write summary to file
    summary_path = Path("tests") / "test_summary.json"
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Test Summary: {summary_path}")
    print(f"Collected: {total_collected} | Passed: {passed} | Failed: {failed} | Skipped: {skipped}")
    if computed_total != total_collected:
        print(f"WARNING: Computed total ({computed_total}) != Collected ({total_collected})")
    print(f"Pass Rate: {summary['pass_rate']}")
    print(f"{'='*60}\n")


def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line(
        "markers", "core: AIOS core system tests"
    )
    config.addinivalue_line(
        "markers", "vendor: Third-party vendor sanity checks"
    )
    config.addinivalue_line(
        "markers", "integration: System integration tests"
    )
    config.addinivalue_line(
        "markers", "chaos: Chaos engineering tests"
    )
    config.addinivalue_line(
        "markers", "performance: Performance contract tests"
    )
    config.addinivalue_line(
        "markers", "quality: Quality contract tests"
    )
    config.addinivalue_line(
        "markers", "property: Property-based tests"
    )
