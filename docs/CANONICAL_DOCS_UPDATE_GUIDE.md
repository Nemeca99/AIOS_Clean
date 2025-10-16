# Canonical Documentation Update Guide

**Status:** CRITICAL PROTOCOL  
**Protection Level:** Presidential  
**Version:** 1.0  
**Date:** October 16, 2025

---

## The Three Protected Files

AIOS has **three canonical documentation files** that are THE SOURCE OF TRUTH for the entire system:

1. **`AIOS_MANUAL.md`** (~37,000 lines) - Complete system documentation
2. **`AIOS_EXECUTIVE_SUMMARY.md`** - High-level architecture overview  
3. **`MANUAL_TOC.md`** - Navigation table of contents

**These files are PROTECTED like the president.**

### Why They Matter

- **Internal use:** Developers reference them for how AIOS works
- **External Auditor GPT:** These files are uploaded to provide the GPT with system knowledge
- **Architectural decisions:** All design choices are validated against these docs
- **Onboarding:** New contributors learn AIOS from these files
- **Compliance:** Audit system validates code against documented standards

**If these files are inaccurate, the entire system's integrity is compromised.**

---

## Update Protocol

### When to Update

**MANDATORY updates after:**
- ✅ New core added (e.g., consciousness_core integration)
- ✅ Major feature integrated (e.g., lingua calc, mirror reflection)
- ✅ Architecture changes (e.g., dual-evaluation system)
- ✅ New subsystem created (e.g., CFIA, RVC, TTE)
- ✅ API changes (e.g., new methods in core modules)
- ✅ Configuration options added (e.g., new config files)

**RECOMMENDED updates after:**
- Minor feature additions
- Bug fixes that change behavior
- Performance optimizations that affect usage
- New scripts or utilities added to `scripts/`

**NOT required for:**
- Internal refactoring (no behavior change)
- Test file additions
- Temporary files or experiments
- Non-production code

---

## The Update Checklist

### Step 1: AIOS_MANUAL.md

**Location:** `F:\AIOS_Clean\AIOS_MANUAL.md`  
**Size:** ~37,489 lines (as of V5)

**What to update:**

- [ ] **New section** if adding a core/subsystem
  - Use consistent heading format: `## X.Y core_name - Description`
  - Include: Purpose, Capabilities, Architecture, Usage, Configuration
  - Add code examples, commands, configuration snippets

- [ ] **Existing section** if modifying a feature
  - Update capability lists
  - Add new methods/functions
  - Update usage examples
  - Revise configuration options

- [ ] **Integration section** if systems now interact
  - Document new integration points
  - Show data flow between systems
  - Explain when each system is used

- [ ] **Troubleshooting section** if new issues possible
  - Add common errors
  - Provide solutions
  - Link to relevant sections

**Format standards:**
- Use markdown headers consistently
- Include code blocks with syntax highlighting
- Add section anchors: `{#section.name}`
- Keep line length reasonable (~120 chars)
- Use bullet points for lists
- Bold important terms on first use

**Example addition (Lingua Calc):**

```markdown
## 2.X Luna Core - Linguistic Calculus Integration

### What is Linguistic Calculus? {#what.is.linguistic.calculus}

The Linguistic Calculus is an interrogative operator system that compresses
natural language reasoning into graph operations...

**Core Operators:**
- Why(a,b) - Causal edge introduction
- How(a,b) - Mechanism chain with depth scoring
- What(a,τ) - Type classification
...

### Usage {#linguistic.calculus.usage}

The lingua calc runs automatically on every Luna response:

\`\`\`python
from luna_core.core.luna_core import LunaCore
luna = LunaCore()
response = luna.generate_response("Why does heat cause expansion?")
# Lingua calc processes question automatically
\`\`\`

### Integration Points {#linguistic.calculus.integration}

- **Mirror:** Feeds ExperienceState to consciousness_core mirror
- **Arbiter:** Stores depth/gain in CacheEntry
- **Drift Monitor:** Logs derivations for pattern analysis
...
```

### Step 2: AIOS_EXECUTIVE_SUMMARY.md

**Location:** `F:\AIOS_Clean\AIOS_EXECUTIVE_SUMMARY.md`  
**Purpose:** High-level overview for architects/executives

**What to update:**

- [ ] **Architecture Overview** if system structure changed
  - Core count (e.g., "18 cores" → "19 cores")
  - New major components
  - Key relationships

- [ ] **Capabilities** if new high-level features added
  - One-line feature description
  - Why it matters
  - What problem it solves

- [ ] **Statistics** if system metrics changed
  - Total lines of code
  - Number of modules
  - Performance metrics

- [ ] **Philosophy** if design principles evolved
  - Core beliefs about the system
  - Why architectural choices were made

**Keep it concise:**
- Executive summary should be readable in 10-15 minutes
- Focus on **what** and **why**, not **how**
- Link to AIOS_MANUAL.md for details

### Step 3: MANUAL_TOC.md

**Location:** `F:\AIOS_Clean\MANUAL_TOC.md`  
**Purpose:** Navigation structure for AIOS_MANUAL.md

**What to update:**

- [ ] **New sections** if you added major sections to manual
  - Section number (e.g., `## 2.7 New Core`)
  - Section title
  - Line number where section starts
  - Subsection references

- [ ] **Line numbers** if sections moved
  - Re-run TOC generator script: `py scripts\generate_manual_toc.py`
  - Or manually update line numbers
  - Verify all references are accurate

**Format:**
```markdown
## 2.X core_name - Description {#section.anchor}

**Line:** XXXXX

### Subsections
- What core_name Does (Line XXXXX)
- Architecture (Line XXXXX)
- Usage (Line XXXXX)
...
```

---

## Verification

### Internal Consistency Check

**Before committing updates:**

1. **Cross-reference check:**
   - Does AIOS_MANUAL.md mention the feature?
   - Does AIOS_EXECUTIVE_SUMMARY.md reflect it?
   - Does MANUAL_TOC.md include it?

2. **Accuracy check:**
   - Are code examples correct?
   - Are file paths valid?
   - Are commands tested?
   - Are line numbers accurate in TOC?

3. **Completeness check:**
   - Is usage documented?
   - Are integration points explained?
   - Are configuration options listed?
   - Are troubleshooting tips included?

4. **Format check:**
   - Consistent markdown style?
   - Headers follow pattern?
   - Code blocks have language tags?
   - No broken links?

### External Auditor GPT Sync

**After updating docs:**

1. **Upload to ChatGPT GPT:**
   - Go to AIOS Auditor GPT settings
   - Upload updated `AIOS_MANUAL.md`
   - Upload updated `AIOS_EXECUTIVE_SUMMARY.md`
   - Upload updated `MANUAL_TOC.md`

2. **Verify GPT knowledge:**
   ```
   Ask: "What is linguistic calculus in AIOS?"
   Expected: Accurate description from updated manual
   
   Ask: "How many cores does AIOS have?"
   Expected: Correct count from updated summary
   ```

3. **Test evaluation:**
   ```
   Send a design proposal related to the new feature
   GPT should:
   - Recognize the feature exists
   - Evaluate against documented standards
   - Reference correct manual sections
   ```

---

## Example: Lingua Calc Integration

### What Was Done (Actual Implementation)

1. **Code changes:**
   - Created `luna_core/core/luna_lingua_calc.py`
   - Modified `luna_core/core/response_generator.py`
   - Updated `luna_core/systems/luna_arbiter_system.py`
   - Implemented `consciousness_core/biological/mirror.py`

2. **Documentation created:**
   - ✅ `LINGUA_CALC_INTEGRATION_COMPLETE.md` (summary)
   - ✅ `scripts/test_lingua_calc_integration.py` (tests)
   - ✅ `docs/ARBITER_DUAL_AUDIT_ARCHITECTURE.md` (arch docs)

### What Should Be Done (Canonical Docs)

3. **Canonical doc updates needed:**

   **AIOS_MANUAL.md:**
   - [ ] Add section: `## 2.X Luna Core - Linguistic Calculus`
   - [ ] Document operators (Why/How/What/Where/When/Who)
   - [ ] Explain rewrite rules (Why+Why→How, Why+How→What)
   - [ ] Show usage examples
   - [ ] Document mirror integration
   - [ ] Explain arbiter feature tracking

   **AIOS_EXECUTIVE_SUMMARY.md:**
   - [ ] Update capabilities: "Linguistic reasoning compression"
   - [ ] Mention V5 lingua calc integration
   - [ ] Note mirror becomes functional semantic compressor

   **MANUAL_TOC.md:**
   - [ ] Add entry: `## 2.X luna_core - Linguistic Calculus (Line XXXXX)`
   - [ ] Include subsections

4. **External Auditor GPT sync:**
   - [ ] Re-upload all three files to GPT
   - [ ] Test: "How does linguistic calculus work in AIOS?"
   - [ ] Verify GPT can evaluate lingua calc designs

---

## Maintenance Cadence

### Immediate (Same Session)
- Update docs as part of the feature implementation
- Don't consider feature "complete" until docs updated
- Travis reviews doc updates before merging code

### Weekly
- Review manual for outdated sections
- Check for new scripts/utilities not documented
- Verify External Auditor GPT has latest files

### Monthly
- Full manual audit (internal auditor can help)
- Check for broken references
- Update statistics (line counts, etc.)
- Re-generate MANUAL_TOC.md from scratch

### Per Release
- Comprehensive doc review
- External auditor GPT full context refresh
- Generate changelog from doc updates

---

## Protection Measures

### Backup Policy

**Before making changes:**
```powershell
# Backup the three protected files
copy AIOS_MANUAL.md AIOS_MANUAL.md.backup
copy AIOS_EXECUTIVE_SUMMARY.md AIOS_EXECUTIVE_SUMMARY.md.backup
copy MANUAL_TOC.md MANUAL_TOC.md.backup
```

**After verifying changes:**
- Commit to git immediately
- Tag important doc updates: `git tag doc-update-lingua-calc`

### Git Commit Message Format

```
docs: Add linguistic calculus to canonical documentation

- Added Luna Core - Linguistic Calculus section to AIOS_MANUAL.md
- Updated AIOS_EXECUTIVE_SUMMARY.md with V5 lingua calc mention
- Added lingua calc entry to MANUAL_TOC.md
- Re-uploaded to External Auditor GPT

Related: LINGUA_CALC_INTEGRATION_COMPLETE.md
```

### Review Checklist

Before committing canonical doc changes:

- [ ] All three files updated?
- [ ] Consistent information across files?
- [ ] Code examples tested?
- [ ] Line numbers accurate (MANUAL_TOC.md)?
- [ ] No typos or formatting errors?
- [ ] External Auditor GPT will be updated?
- [ ] Git commit message explains changes?

---

## Tools

### Automated TOC Generation

```powershell
py scripts\generate_manual_toc.py
```

Automatically generates MANUAL_TOC.md from AIOS_MANUAL.md headers.

### Consistency Checker (Future)

```powershell
py scripts\check_canonical_docs.py
```

Would verify:
- All cores mentioned in manual
- All documented features exist in code
- All code examples are syntactically correct
- No broken references

### External Auditor GPT Upload Script (Future)

```powershell
py scripts\sync_external_auditor.py
```

Would automatically upload the three files to GPT via API.

---

## Emergency Protocol

### If Canonical Docs Get Out of Sync

**Symptoms:**
- External Auditor GPT gives outdated guidance
- Developers confused about how features work
- Audit system flags code as "non-standard" despite being correct

**Recovery:**
1. **Stop all feature work** - docs first
2. **Run full audit:** Review every core vs manual
3. **Systematic update:** Go core-by-core, update all three files
4. **Verify:** Test with External Auditor GPT
5. **Resume:** Feature work continues only when docs accurate

### If Manual Becomes Too Large

**Current:** 37,489 lines (manageable but getting large)

**Mitigation strategies:**
1. Split into multiple files (keep AIOS_MANUAL.md as master)
2. Move detailed API docs to separate files
3. Create per-core detailed documentation
4. Keep main manual at "usage" level, link to deep dives

**Don't:**
- Sacrifice completeness for brevity
- Remove examples (they're critical)
- Delete troubleshooting sections

---

## Summary

### The Golden Rule

**"If it's not in the manual, it doesn't exist."**

### The Three Commandments

1. **Thou shalt update AIOS_MANUAL.md** with every major feature
2. **Thou shalt keep AIOS_EXECUTIVE_SUMMARY.md accurate** for architects
3. **Thou shalt sync MANUAL_TOC.md** so navigation works

### The Protection Pledge

**"I will treat these three files as THE SOURCE OF TRUTH for AIOS.**  
**I will update them immediately after changes.**  
**I will verify External Auditor GPT stays in sync.**  
**I will never let them drift from reality."**

---

**Created by:** Travis Miner  
**Purpose:** Maintain canonical documentation integrity  
**Protection Level:** Presidential - highest priority for accuracy

