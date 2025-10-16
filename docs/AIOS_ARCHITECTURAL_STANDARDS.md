# AIOS Architectural Standards

## Overview
The AIOS system enforces strict architectural standards across all modules to ensure consistency, maintainability, and reliability. The V3 Sovereign audit system includes comprehensive standards checking to validate compliance.

## Core Structure Standards

### 1. Folder Structure (`*_core` Pattern)
**Required Pattern:** All core modules must follow the `*_core` naming convention.

**Required Directories:**
- `config/` - Configuration files (JSON, YAML)
- `__init__.py` - Module initialization file

**Optional Directories:**
- `core/` - Core functionality
- `systems/` - System components
- `utils/` - Utility functions
- `implementations/` - Alternative implementations
- `extra/` - Additional resources

**Standards Violations:**
- ❌ Non-`*_core` folder names
- ❌ Missing `config/` directory
- ❌ Non-standard directory names (without exceptions)

### 2. Main Core Files (`*_core.py`)
**Required Elements:**
```python
#!/usr/bin/env python3
"""
MODULE DOCSTRING
Description of the core module
"""

import sys
from pathlib import Path

# Unicode safety (recommended)
from utils_core.unicode_safe_output import setup_unicode_safe_output
setup_unicode_safe_output()

def handle_command(args: List[str]) -> bool:
    """
    Handles commands for the core module.
    Expected args: ['--module', 'command', ...]
    """
    # Implementation here
    pass
```

**Standards Violations:**
- ❌ Missing shebang (`#!/usr/bin/env python3`)
- ❌ Missing module docstring
- ❌ Missing `handle_command()` function
- ❌ Incorrect `handle_command()` signature
- ❌ Missing Unicode safety imports (Windows compatibility)

### 3. File Linking Patterns
**Required Elements:**
- `__init__.py` must expose `handle_command`
- No circular imports within the core
- Proper import organization (stdlib → third-party → local)

**Standards Violations:**
- ❌ Missing `__init__.py`
- ❌ `__init__.py` doesn't expose `handle_command`
- ❌ Circular imports within core
- ❌ Incorrect import order

### 4. JSON Configuration Standards
**Required Structure:**
```json
{
  "schema_version": 1,
  "version": "1.0",
  "last_updated": "2025-10-15",
  "description": "Configuration description",
  "config_section": {
    // Configuration data
  }
}
```

**Model Config Standards:**
```json
{
  "model_config": {
    "version": "1.0",
    "models": {
      "main_llm": {
        "name": "model-name",
        "type": "main_model",
        "tier": "high_complexity",
        "api_endpoint": "http://localhost:1234/v1/chat/completions"
      }
    }
  }
}
```

**AIOS Config Standards:**
```json
{
  "AIOS_ROOT": "F:\\AIOS_Clean",
  "PYTHON_ENV_PATH": "F:\\AIOS_Clean\\venv",
  "MONITORING_ENABLED": true,
  "DEBUG_MODE": false
}
```

**Standards Violations:**
- ❌ Invalid JSON syntax
- ❌ Missing `schema_version` or `version` fields
- ❌ Missing required keys for specific config types
- ❌ Malformed model configuration
- ❌ Missing AIOS configuration keys

### 5. Coding Standards
**Required Elements:**
- Shebang on main files
- Module docstrings
- Proper import organization
- Standard library imports first
- Third-party imports second
- Local imports last

**Import Organization:**
```python
# 1. Standard library
import sys
import os
import json
from pathlib import Path
from typing import Dict, List

# 2. Third-party
import numpy as np
import requests

# 3. Local imports
from utils_core.unicode_safe_output import setup_unicode_safe_output
from support_core.support_core import SystemConfig
```

**Standards Violations:**
- ❌ Missing shebang on main files
- ❌ Missing module docstrings
- ❌ Incorrect import order
- ❌ Mixed import types

## Integration Standards

### Main.py Integration
All cores must be discoverable by `main.py` through:
1. `*_core` folder pattern
2. `handle_command()` function
3. Proper module structure

### Cross-Core Communication
- Use `utils_core` for shared utilities
- Use `support_core` for system integration
- Avoid direct cross-core imports
- Use configuration files for shared settings

## Audit Integration

### V3 Sovereign Standards Check
The audit system automatically validates:
- ✅ Folder structure compliance
- ✅ Main file standards
- ✅ File linking patterns
- ✅ JSON configuration validity
- ✅ Coding standards adherence

### Scoring System
- **Critical Violations:** -25 points each
- **Warning Violations:** -10 points each
- **Maximum Standards Penalty:** -20 points per core

### Compliance Tracking
Each core is scored on five compliance categories:
1. **Folder Structure** - Directory organization
2. **Main File** - Core file standards
3. **File Linking** - Import and linking patterns
4. **JSON Standards** - Configuration file validity
5. **Coding Standards** - Code quality and organization

## Current Status

### Standards Compliance Summary
Based on recent audit results:

| Core | Score | Critical | Warnings | Compliance |
|------|-------|----------|----------|------------|
| carma_core | 0/100 | 18 | 0 | ❌ All Failed |
| rag_core | 50/100 | 0 | 5 | ❌ Mixed |
| data_core | 0/100 | 17 | 0 | ❌ All Failed |
| luna_core | 0/100 | 66 | 0 | ❌ All Failed |

### Common Violations
1. **Missing `handle_command()`** - Most cores lack proper command handling
2. **Non-standard directories** - Many cores have custom directory structures
3. **Missing configuration** - Several cores lack proper `config/` directories
4. **JSON standards** - Many config files missing version fields
5. **Import organization** - Inconsistent import ordering

## Recommendations

### Immediate Actions
1. **Standardize folder structures** - Remove non-standard directories
2. **Implement `handle_command()`** - Add command handling to all cores
3. **Add configuration files** - Ensure all cores have proper `config/` directories
4. **Fix JSON standards** - Add version fields to all configuration files
5. **Organize imports** - Standardize import ordering across all files

### Long-term Improvements
1. **Automated standards enforcement** - Pre-commit hooks for standards
2. **Template generation** - Create core templates for new modules
3. **Documentation generation** - Auto-generate standards documentation
4. **Continuous monitoring** - Real-time standards compliance tracking

## Tools and Resources

### Audit Tools
- **V3 Sovereign Audit:** `py main.py --audit --v3`
- **Standards Test:** `py scripts/test_standards_check.py`
- **Individual Core Test:** `py scripts/test_standards_check.py`

### Configuration Files
- **Policy:** `main_core/audit_core/config/policy.yaml`
- **Check Patterns:** `main_core/audit_core/config/check_patterns.json`
- **Standards Check:** `main_core/audit_core/checks/standards_check.py`

### Documentation
- **Manual:** `AIOS_MANUAL.md`
- **Standards:** `docs/AIOS_ARCHITECTURAL_STANDARDS.md`
- **Audit Reports:** `reports/dashboard.html`

---

**Last Updated:** 2025-10-15  
**Standards Version:** 1.0  
**Audit System:** V3 Sovereign (20 features)
