# Manual Update Workflow - Quick Reference

## TL;DR - One Command Does Everything

```bash
py scripts/update_manual_complete.py
```

This single command:
1. ✅ Verifies `AIOS_MANUAL.md` exists
2. ✅ Regenerates `MANUAL_TOC.md` with line numbers
3. ✅ Updates metadata timestamps
4. ✅ Rebuilds RAG database with embeddings

**Takes:** ~10-20 seconds total

---

## When to Run This

Run `update_manual_complete.py` after:
- ✏️ Editing `AIOS_MANUAL.md`
- 📝 Adding new sections
- 🔄 Reorganizing content
- 📊 Updating documentation
- 🐛 Fixing typos or errors

**Basically:** Run this **every time** you edit the manual!

---

## Detailed Workflow

### Step-by-Step Process

```bash
# 1. Edit the manual
code AIOS_MANUAL.md  # or any editor

# 2. Save your changes

# 3. Run the update script
py scripts/update_manual_complete.py

# 4. Verify everything works
py main.py --rag search "your test query"

# 5. Commit changes
git add AIOS_MANUAL.md MANUAL_TOC.md rag_core/manual_oracle/
git commit -m "docs: update manual - [brief description]"
```

### What Happens Automatically

#### Step 1: Verification (instant)
```
[1/4] Verifying AIOS_MANUAL.md...
   Manual found: 0.87 MB, 35,569 lines
```
- Checks file exists
- Shows size and line count

#### Step 2: TOC Generation (~1 second)
```
[2/4] Regenerating MANUAL_TOC.md...
   TOC updated: 2,706 entries
```
- Scans all headings (`#`, `##`, `###`)
- Extracts line numbers
- Creates navigation table
- Preserves anchor IDs

#### Step 3: Metadata Update (instant)
```
[3/4] Updating manual metadata...
   Timestamp: 2025-10-15 15:15
   Lines: 35,569
```
- Records update timestamp
- Tracks line count

#### Step 4: RAG Database Rebuild (~10-15 seconds)
```
[4/4] Rebuilding RAG database with embeddings...
   This will take ~10-20 seconds for embedding generation...
   RAG database rebuilt in 12.3s
   Index size: 571 KB
```
- Re-parses manual sections
- Generates embeddings (cached after first run)
- Updates oracle index
- Verifies integrity

---

## Command Options

### Full Update (Default)
```bash
py scripts/update_manual_complete.py
```
Updates everything. **Recommended.**

### Skip TOC (if you only changed embeddings)
```bash
py scripts/update_manual_complete.py --skip-toc
```
Skips TOC regeneration, only rebuilds RAG database.

### Skip Embeddings (if you only changed headings)
```bash
py scripts/update_manual_complete.py --skip-embeddings
```
Regenerates TOC but skips RAG rebuild.

### Verbose Mode
```bash
py scripts/update_manual_complete.py --verbose
```
Shows detailed output from embedding generation.

---

## Manual Components

### 1. AIOS_MANUAL.md (Main Document)
- **What:** The complete user manual
- **Size:** ~0.87 MB (35,569 lines)
- **Format:** Markdown with anchor IDs
- **Location:** Root directory

**Example Structure:**
```markdown
## 2.6 Audit System & Self-Healing {#audit.system.self-healing}

The V3 Sovereign audit system provides...
```

### 2. MANUAL_TOC.md (Table of Contents)
- **What:** Auto-generated navigation index
- **Format:** Markdown table with line numbers
- **Updates:** Automatically on every manual update
- **Location:** Root directory

**Example Structure:**
```markdown
| Line | Section | Topic |
|------|---------|-------|
| 123  | 2.6     | Audit System & Self-Healing |
| 456  | 2.6.1   | V3 Features |
```

### 3. RAG Database (Manual Oracle)
- **What:** Searchable database with embeddings
- **Location:** `rag_core/manual_oracle/oracle_index.json`
- **Size:** ~571 KB
- **Format:** JSON with pre-computed embeddings

**Contains:**
```json
{
  "anchor": "audit.system.self-healing",
  "title": "Audit System & Self-Healing",
  "line_number": 123,
  "embedding": [0.123, -0.456, ...],
  "byte_start": 12345,
  "byte_end": 67890,
  "section_sha256": "abc123..."
}
```

---

## Testing After Updates

### Quick Search Test
```bash
py main.py --rag search "audit system"
```
**Expected:**
```
Found 5 results:
  1. Audit System & Self-Healing (score: 0.850)
  2. V3 Sovereign Features (score: 0.723)
  ...
```

### Lookup Specific Section
```bash
py main.py --rag lookup "audit.system.self-healing"
```
**Expected:** Returns the section content

### Run Full Audit (with Oracle)
```bash
py main.py --audit --v3
```
**Expected:** Oracle provides citations for findings

---

## Troubleshooting

### Error: "AIOS_MANUAL.md not found"
**Solution:** Make sure you're in the repo root
```bash
cd F:\AIOS_Clean
py scripts/update_manual_complete.py
```

### Error: "TOC generation failed"
**Problem:** Invalid markdown in manual
**Solution:** Check for unclosed code blocks, malformed headings

### Error: "RAG rebuild had issues"
**Problem:** Usually Unicode characters in output (cosmetic)
**Solution:** Ignore if embeddings were generated successfully

### Search Returns No Results
**Problem:** Oracle not rebuilt or corrupted
**Solution:** Force rebuild
```bash
py scripts/build_oracle_with_embeddings.py
```

---

## Advanced: Manual-Only Updates

### If You Need Fine Control

**Update TOC Only:**
```python
py -c "
from pathlib import Path
with open('AIOS_MANUAL.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
# ... TOC generation code ...
"
```

**Rebuild RAG Only:**
```bash
py scripts/build_oracle_with_embeddings.py
```

**Generate Canonical PDF:**
```bash
py scripts/convert_manual_canonical.ps1
```

---

## Performance Metrics

### Typical Update Times

| Component | Time | Notes |
|-----------|------|-------|
| Manual verification | <1ms | Instant |
| TOC generation | ~1s | Scans 35k lines |
| RAG database rebuild | ~12s | Embeds 48 sections |
| **Total** | **~15s** | Complete update |

### File Sizes

| File | Size | Format |
|------|------|--------|
| AIOS_MANUAL.md | 0.87 MB | Markdown |
| MANUAL_TOC.md | ~50 KB | Markdown table |
| oracle_index.json | 571 KB | JSON + embeddings |
| **Total** | **~1.5 MB** | All components |

---

## Git Workflow

### After Manual Updates

```bash
# 1. Update everything
py scripts/update_manual_complete.py

# 2. Check what changed
git status

# 3. Review changes
git diff AIOS_MANUAL.md
git diff MANUAL_TOC.md

# 4. Stage changes
git add AIOS_MANUAL.md MANUAL_TOC.md rag_core/manual_oracle/

# 5. Commit with descriptive message
git commit -m "docs: update manual - added embedder optimization guide"

# 6. Push to remote
git push
```

### Commit Message Examples

**Good:**
- `docs: update manual - added auto-venv activation guide`
- `docs: fix typos in audit system section`
- `docs: reorganize CARMA optimization strategies`

**Bad:**
- `update` (too vague)
- `changes` (no context)
- `wip` (not descriptive)

---

## Automation Ideas (Future)

### Pre-Commit Hook
```bash
# Auto-update on commit
# .git/hooks/pre-commit
#!/bin/sh
if git diff --cached --name-only | grep -q "AIOS_MANUAL.md"; then
    py scripts/update_manual_complete.py
    git add MANUAL_TOC.md rag_core/manual_oracle/
fi
```

### Watch Mode
```bash
# Auto-rebuild on file change
pip install watchdog
watchmedo shell-command \
  --patterns="AIOS_MANUAL.md" \
  --command='py scripts/update_manual_complete.py' \
  .
```

---

## Best Practices

### 1. Update After Every Edit
✅ **DO:** Run update script after saving manual changes
❌ **DON'T:** Edit manual and forget to rebuild

### 2. Test Searches
✅ **DO:** Test a search query after updating
❌ **DON'T:** Assume it works without testing

### 3. Commit Together
✅ **DO:** Commit manual + TOC + RAG together
❌ **DON'T:** Commit only manual, forget TOC/RAG

### 4. Descriptive Messages
✅ **DO:** `docs: update manual - added XYZ section`
❌ **DON'T:** `update stuff`

### 5. Verify Integrity
✅ **DO:** Run audit to verify oracle works
❌ **DON'T:** Skip verification

---

**Quick Reference Card:**
```
AFTER EDITING MANUAL:
1. py scripts/update_manual_complete.py
2. py main.py --rag search "test"
3. git add AIOS_MANUAL.md MANUAL_TOC.md rag_core/
4. git commit -m "docs: ..."
```

**That's it! Simple, fast, automated.** 🚀

