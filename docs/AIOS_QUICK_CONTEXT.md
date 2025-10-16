# AIOS Quick Context - For New AI Conversations

## Copy-Paste This For New Chats

```
I'm working on AIOS (AI Operating System) - a modular Python system with 19 *_core plugins.

Key Context:
- Main file: main.py (auto-discovers cores, auto-activates .venv)
- Manual: AIOS_MANUAL.md (35,569 lines, use MANUAL_TOC.md for navigation)
- Architecture: Each core has *_core.py with handle_command()
- Audit: V3 Sovereign (20 features, 8.9s, enforces standards)
- RAG: Manual Oracle with local embeddings (11.5ms searches)
- Python: 3.11 in .venv, sentence-transformers for embeddings

To understand the system:
1. Read: docs/AIOS_QUICK_CONTEXT.md (this file)
2. Status: `py main.py --status`
3. Cores: `py main.py --ping --health`

Full docs: AIOS_MANUAL.md (660 pages PDF) or MANUAL_TOC.md (quick nav)
```

---

## System Overview (2-Minute Read)

### What is AIOS?
A self-contained AI operating system with:
- **19 modular cores** (plugins that auto-discover)
- **Luna** (AI personality/conversation)
- **CARMA** (memory system with integrity verification)
- **Dream** (background optimization)
- **V3 Sovereign Audit** (production-grade health checks)
- **Manual Oracle** (searchable docs with embeddings)

### Architecture Pattern
```
main.py (bootstrap)
  ├── Discovers *_core folders
  ├── Auto-activates .venv
  └── Routes commands via handle_command()

Each *_core/:
  ├── *_core.py (main file with handle_command)
  ├── config/ (JSON configs)
  ├── core/ (business logic)
  └── __init__.py (exports)
```

### Key Commands
```bash
py main.py --status          # System info
py main.py --ping --health   # Discover cores
py main.py --audit --v3      # Run audit (8.9s)
py main.py --rag search "X"  # Search manual (11.5ms)
py main.py --help            # All commands
```

### Recent Improvements (Current State)
1. **Embeddings:** 173x faster (2s → 11.5ms) using local SentenceTransformers
2. **Standards:** Architectural standards enforcement (20th audit feature)
3. **CARMA:** SHA256 integrity verification
4. **Auto-venv:** Automatic virtual environment activation
5. **Manual workflow:** One-command update (`py scripts/update_manual_complete.py`)

### Files to Know
- `main.py` - Bootstrap (586 lines)
- `AIOS_MANUAL.md` - Full docs (35,569 lines)
- `MANUAL_TOC.md` - Navigation (2,706 entries)
- `requirements.txt` - Dependencies
- `rag_core/manual_oracle/oracle_index.json` - Searchable DB (571 KB)

### Technology Stack
- **Python:** 3.11
- **Embeddings:** SentenceTransformers (all-MiniLM-L6-v2)
- **OS:** Windows 11, but cross-platform
- **Packages:** torch, numpy, requests, streamlit, psutil, sentence-transformers

---

## For Quick Understanding

### Best Starting Points (in order)
1. **This file** (you're reading it) - 5 min
2. **MANUAL_TOC.md** - Browse topics - 2 min
3. **Run `py main.py --status`** - See your system - 10 sec
4. **Specific topic?** Use `py main.py --rag search "topic"` - instant

### Don't Start With
- ❌ Full AIOS_MANUAL.md (too long, 35k lines)
- ❌ Reading all core files (unnecessary)
- ❌ Architecture deep-dives (unless needed)

### Do Start With
- ✅ This file (AIOS_QUICK_CONTEXT.md)
- ✅ MANUAL_TOC.md (table of contents)
- ✅ `--status` and `--ping` commands
- ✅ Specific sections via RAG search

---

## Core Components (30-Second Version)

### Essential Cores
1. **main_core** - Audit system (V3 Sovereign, 20 features)
2. **luna_core** - AI personality
3. **carma_core** - Memory with integrity checks
4. **rag_core** - Manual Oracle (searchable docs)
5. **support_core** - System health
6. **utils_core** - Utilities

### Supporting Cores
7. **dream_core** - Background optimization
8. **fractal_core** - Advanced caching
9. **data_core** - Data management
10. **streamlit_core** - Web UI
11-19. *Others* (backup, enterprise, game, marketplace, music, privacy, template)

---

## What AI Assistants Need to Know

### When Helping With AIOS

**DO:**
- ✅ Use `py main.py --rag search "topic"` to find relevant docs
- ✅ Check `MANUAL_TOC.md` for section navigation
- ✅ Run `--status` to see current system state
- ✅ Ask user which core they're working on
- ✅ Follow the `*_core/*.py` pattern

**DON'T:**
- ❌ Try to read entire AIOS_MANUAL.md (too long)
- ❌ Assume file locations without checking
- ❌ Break the *_core pattern
- ❌ Skip the audit after changes
- ❌ Forget to activate .venv (but main.py auto-activates now!)

### Common Tasks

**"I want to modify a core"**
1. Check which core: `py main.py --ping --health`
2. Find relevant docs: `py main.py --rag search "core name"`
3. Edit the `*_core.py` file
4. Run audit: `py main.py --audit --v3`

**"I want to update the manual"**
1. Edit `AIOS_MANUAL.md`
2. Run: `py scripts/update_manual_complete.py`
3. Test: `py main.py --rag search "test"`
4. Commit all three files (manual, TOC, RAG DB)

**"I want to understand how X works"**
1. Search: `py main.py --rag search "X"`
2. Navigate: Check MANUAL_TOC.md for line numbers
3. Read specific section in AIOS_MANUAL.md

---

## Context for Different Scenarios

### New Feature Development
**Give AI this context:**
```
I'm adding a feature to AIOS. Relevant context:
- Core: [core_name]
- Feature: [description]
- Relevant docs: `py main.py --rag search "[feature topic]"`
```

### Debugging
**Give AI this context:**
```
AIOS issue: [description]
System status: `py main.py --status`
Error: [paste error]
Relevant core: [core_name]
```

### Documentation Update
**Give AI this context:**
```
Updating AIOS docs
Section: [topic] (see MANUAL_TOC.md line X)
Changes: [description]
After editing, run: `py scripts/update_manual_complete.py`
```

---

## Token-Efficient Context Templates

### Minimal Context (100 tokens)
```
AIOS: Modular AI OS, 19 cores, main.py bootstrap
Current: V3 audit, local embeddings (11.5ms), auto-venv
Docs: AIOS_MANUAL.md (35k lines) + MANUAL_TOC.md (nav)
Task: [your specific task]
```

### Standard Context (200 tokens)
```
AIOS (AI Operating System):
- 19 *_core plugins (Luna/CARMA/Dream/Audit/RAG)
- main.py: auto-discovers cores, auto-activates .venv
- Audit: V3 Sovereign (20 features, 8.9s)
- RAG: Manual Oracle with SentenceTransformers (11.5ms)
- Docs: AIOS_MANUAL.md (35k lines), use MANUAL_TOC.md or RAG search
- Python 3.11, Windows 11, local embeddings
Full context: docs/AIOS_QUICK_CONTEXT.md
Task: [your specific task]
```

### Detailed Context (500 tokens)
```
[Copy the "Copy-Paste This For New Chats" section above]
+ Current working on: [specific area]
+ Recent changes: [if any]
+ Goal: [what you want to accomplish]
```

---

## RAG Search Examples (Teach AI to Use This)

The Manual Oracle is your best friend for context:

```bash
# General topics
py main.py --rag search "how does CARMA work"
py main.py --rag search "audit system features"
py main.py --rag search "Luna personality"

# Specific features
py main.py --rag search "embedder optimization"
py main.py --rag search "standards enforcement"
py main.py --rag search "integrity verification"

# Architecture
py main.py --rag search "core structure"
py main.py --rag search "handle_command pattern"
py main.py --rag search "auto-venv activation"
```

Results in **11.5ms** with relevance scores!

---

## File Size Reference

**When AI asks "Can I read X?":**

| File | Size | AI Should |
|------|------|-----------|
| AIOS_QUICK_CONTEXT.md | ~10 KB | ✅ Read entirely |
| MANUAL_TOC.md | ~50 KB | ✅ Read entirely |
| main.py | ~30 KB | ✅ Read if needed |
| *_core.py files | 5-50 KB | ✅ Read specific ones |
| AIOS_MANUAL.md | 870 KB | ❌ Use RAG search instead |
| oracle_index.json | 571 KB | ❌ Don't read, use RAG |

---

## Update Frequency

**How often these change:**
- AIOS_QUICK_CONTEXT.md: After major features (monthly)
- AIOS_MANUAL.md: Often (weekly)
- MANUAL_TOC.md: Auto-updates with manual
- oracle_index.json: Auto-updates with manual
- Core files: Frequently (daily during dev)

**Always fresh:** RAG search (reflects latest manual)

---

## Getting Started Checklist

For a new AI assistant helping with AIOS:

- [ ] Read this file (AIOS_QUICK_CONTEXT.md)
- [ ] Scan MANUAL_TOC.md to see available topics
- [ ] Run `py main.py --status` to see current state
- [ ] Run `py main.py --ping --health` to see cores
- [ ] Test RAG: `py main.py --rag search "test"`
- [ ] Understand pattern: `*_core/*.py` with `handle_command()`
- [ ] Know the workflow: edit → audit → commit

**Time:** 10 minutes to full context

---

## Emergency Quick Reference

**AI stuck? Try these:**

1. **System info:** `py main.py --status`
2. **Find docs:** `py main.py --rag search "topic"`
3. **Check health:** `py main.py --audit --v3`
4. **List cores:** `py main.py --ping`
5. **Help:** `py main.py --help`

**Documentation:**
- Quick: MANUAL_TOC.md
- Search: RAG (`py main.py --rag search`)
- Full: AIOS_MANUAL.md (if really needed)
- Context: This file

---

**Last Updated:** 2025-10-15
**AIOS Version:** V3 Sovereign (20 features)
**Python:** 3.11
**Lines:** AIOS_MANUAL.md (35,569), main.py (586)

