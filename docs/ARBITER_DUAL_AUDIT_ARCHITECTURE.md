# AIOS Auditor + Arbiter Architecture

**Status:** Production  
**Version:** AIOS v5.0  
**Date:** October 16, 2025

---

## Overview

AIOS employs a **three-layer evaluation system** with complementary quality gates:

1. **Internal Auditor (`main_core/audit_core/`)** - Local audit system with full tool access
2. **External Auditor GPT (ChatGPT Custom)** - Cloud-based mirror of internal auditor, leverages OpenAI knowledge/speed
3. **Internal Arbiter (`luna_core/systems/luna_arbiter_system.py`)** - Runtime response assessment

**These are distinct systems with different roles:**
- **Audit System (internal + external)** validates code quality, architecture, and system design
- **Arbiter (internal only)** assesses individual Luna responses and manages karma

**External Auditor GPT is a mirror:**
- Contains same knowledge as internal auditor (AIOS manual, docs, executive summary)
- Uses OpenAI's servers for speed and broader knowledge base
- Cannot execute tool calls like internal auditor
- Provides code suggestions and architectural guidance

This architecture provides **pre-implementation validation**, **runtime assessment**, and **cloud-accelerated analysis** across the entire system lifecycle.

---

## Internal Auditor: audit_core

### Identification

**Location:** `main_core/audit_core/`  
**Type:** Local Python system with full tool access  
**Key Module:** `audit_v3_sovereign.py`  
**Role:** Code quality assurance, architecture validation, self-healing  
**Created by:** Travis Miner ("The Architect")

### Purpose

The Internal Auditor (audit_core) is the **primary quality assurance system** that:

- Runs static analysis on all cores
- Validates code quality and standards compliance
- Performs differential audits (what changed)
- Manages quarantine for failing modules
- Generates SARIF reports and dashboards
- Self-heals during dream cycles
- **Has full tool access** to read/write files, run commands, analyze code

See `AIOS_MANUAL.md` §2.6 for complete audit system documentation.

---

## External Auditor: AIOS Auditor GPT

### Identification

**Name:** AIOS Auditor  
**Type:** Custom GPT (Cloud-Based Mirror)  
**Platform:** ChatGPT  
**Role:** Architectural validation leveraging OpenAI's knowledge and speed  
**Created by:** Travis Miner ("The Architect")

### Relationship to Internal Auditor

**External Auditor GPT is a cloud-based mirror of the internal audit_core system:**

- **Knowledge Base:** Uploaded AIOS manual, docs, executive summary, major files
- **Purpose:** Same evaluation criteria as internal auditor, but cloud-accelerated
- **Advantage:** Leverages OpenAI's servers for speed + broader knowledge base
- **Limitation:** Cannot execute tool calls (no file writes, no command execution)
- **Use Case:** Pre-implementation design validation, architectural guidance, code suggestions

**Think of it as:** Internal auditor's "brain in the cloud" - same judgment, faster inference, but no hands.

### Critical Knowledge Base Files

**The External Auditor GPT's knowledge comes from three PROTECTED canonical documents:**

1. **`AIOS_MANUAL.md`** - Complete system documentation (~37,000 lines)
   - All core modules, architecture, usage guides
   - Single source of truth for how AIOS works
   - **CRITICAL:** Must be updated with every major feature addition

2. **`AIOS_EXECUTIVE_SUMMARY.md`** - High-level overview
   - Architecture summary, key capabilities, design philosophy
   - What executives/architects need to know
   - **CRITICAL:** Must reflect current system state accurately

3. **`MANUAL_TOC.md`** - Table of contents
   - Navigation structure for AIOS_MANUAL.md
   - Section references with line numbers
   - **CRITICAL:** Must stay in sync with manual structure

**Protection Level:** Presidential (highest priority for accuracy and integrity)

**Update Policy:** These files MUST be updated whenever:
- New cores are added
- Major features are integrated (like lingua calc, mirror, etc.)
- Architecture changes occur
- API interfaces change
- Configuration options are added/modified

**Why this matters for External Auditor GPT:**
- The GPT can only evaluate based on what's in these files
- Outdated docs = inaccurate architectural guidance
- Travis must re-upload these files to the GPT after major updates
- The GPT's judgment quality depends entirely on document accuracy

### Purpose

The External Auditor GPT **evaluates AIOS architecture and designs** based on uploaded context:

- Verify **architectural alignment** with the biological consciousness model
- Score designs for **technical feasibility**, **consciousness integration**, **performance impact**, and **documentation coherence**
- Maintain **fidelity to the AIOS manuals** (v5.0 canonical)
- Provide impartial feedback while respecting the Architect's final authority

### Evaluation Dimensions

The External Auditor scores proposals on 5 dimensions (0.0 - 5.0 scale):

1. **Architectural Alignment** - Fits biological consciousness model (§3.19)
2. **Technical Feasibility** - Syntactically valid, dependency-safe
3. **Consciousness Integration** - Enhances mirror/soul/heart triad
4. **Performance Impact** - Resource overhead acceptable
5. **Documentation Coherence** - Matches AIOS_MANUAL.md standards

**Composite Score ≥ 4.5** = Approved for implementation  
**Composite Score < 4.5** = Requires revision

### Philosophy

> "While Luna *speaks*, CARMA *remembers*, Dreamer *imagines*, the Auditor *validates* and Arbiter *verifies*."

The External Auditor serves as a **mirror of judgment**—a synthetic conscience that checks architectural designs dispassionately and reports with metrics, not moods.

**Key Distinction:**
- **Auditor** = Validates system architecture (external GPT)
- **Arbiter** = Assesses Luna's responses (internal system)

---

## Internal Arbiter: LunaArbiterSystem

### Identification

**Module:** `luna_core/systems/luna_arbiter_system.py`  
**Class:** `LunaArbiterSystem`  
**Role:** Runtime response quality assessment  
**Integration:** Full AIOS core pipeline

### Purpose

The Internal Arbiter operates **after every Luna response** to:

- Generate **gold standard** reference responses via LM Studio
- Calculate **utility scores** (quality vs. efficiency)
- Award/penalize **karma** based on response quality
- Store **lessons** in CFIA-managed cache
- Track **linguistic calculus features** (depth, gain) - *V5 integration*

### Key Methods

```python
def assess_response(
    user_prompt: str, 
    luna_response: str,
    tte_used: int, 
    max_tte: int,
    rvc_grade: str = None,
    emergence_zone_system = None,
    context_fragments: List[str] = None,
    lingua_calc_context: Dict = None  # V5: NEW
) -> ArbiterAssessment
```

### CFIA Integration

The Internal Arbiter uses the **Cognitive File Integrity Audit (CFIA)** system for generational memory management:

- Lessons stored with **lingua_calc_depth** and **lingua_calc_gain** (V5)
- Karma pool tracks across generations
- Memory forking/merging for identity continuity

### Rust Acceleration

When available, `aios_luna_rust` provides fast Arbiter assessment:
- 10x faster utility scoring
- Parallel gold standard generation
- Falls back to Python gracefully

---

## Three-Layer Evaluation System

### Layer 1: Local Code Audit (Internal Auditor - audit_core)

**When:** On-demand (`py main.py --audit --v3`) or automated (dream cycles)  
**Input:** Codebase, changed files, all cores  
**Output:** Audit scores, SARIF reports, quarantine decisions, dashboards  
**Authority:** Executive (can fix code, quarantine modules)  
**System:** `main_core/audit_core/audit_v3_sovereign.py`

**Example Flow:**
1. Run `py main.py --audit --v3`
2. Internal auditor scans all cores
3. Static analysis, standards checks, differential audits
4. Generates reports, identifies issues
5. Can auto-fix during dream cycle self-healing

### Layer 2: Cloud Design Validation (External Auditor GPT)

**When:** Before implementing new features/cores  
**Input:** Proposal, design doc, code sketch  
**Output:** 5-dimension score + composite verdict  
**Authority:** Advisory (Architect decides)  
**System:** AIOS Auditor GPT (ChatGPT Custom - mirror of audit_core knowledge)

**Example Flow:**
1. Architect drafts "Linguistic Calculus Integration" plan
2. Sends to External Auditor GPT (has AIOS manual context)
3. GPT evaluates against uploaded docs + OpenAI knowledge
4. Receives 4.9/5.0 composite score with detailed breakdown
5. Proceeds with implementation

### Layer 3: Runtime Response Assessment (Internal Arbiter)

**When:** After every Luna response  
**Input:** User prompt, Luna's response, token usage  
**Output:** Utility score, karma delta, gold standard, lesson  
**Authority:** Executive (affects karma pool, age progression)  
**System:** LunaArbiterSystem (Internal Python module)

**Example Flow:**
1. User asks "Why does heat cause expansion?"
2. Luna responds with 150 tokens
3. Internal Arbiter generates gold standard (LM Studio)
4. Scores quality gap, awards karma
5. Stores lesson with `lingua_calc_depth=2, gain=0.3`

---

## Integration Points

### 1. Logs Export for External Analysis

The Internal Arbiter can export logs for External Auditor meta-analysis:

**File:** `data_core/ArbiterCache/arbiter_export.json`

```json
{
  "export_timestamp": "2025-10-16T03:35:00Z",
  "generation": 42,
  "karma_pool": 156.7,
  "lessons": [
    {
      "prompt": "Why does heat cause expansion?",
      "utility_score": 0.85,
      "karma_delta": 2.5,
      "lingua_calc_depth": 2,
      "lingua_calc_gain": 0.3,
      "timestamp": "2025-10-16T03:30:15Z"
    }
  ],
  "summary": {
    "total_lessons": 347,
    "avg_utility": 0.78,
    "avg_depth": 1.8,
    "avg_gain": 0.24
  }
}
```

### 2. Cross-Reference in Manual

Both Auditor and Arbiter reference the same canonical documentation:
- `AIOS_MANUAL.md` - System architecture
- `STANDARDS_MANIFEST.md` - Code quality standards
- `consciousness_core/docs/` - Biological consciousness model

### 3. Shared Terminology

Both Auditor and Arbiter use consistent metrics:
- **Utility Score** - Response quality measure (0.0 - 1.0)
- **Karma** - Existential currency (tracked across generations)
- **Compression Index** - Mirror reflection depth (mechanism/cause ratio)
- **Depth Score** - Linguistic calculus reasoning depth
- **Gain** - Compression improvement from rewrite rules

---

## Why This Architecture Works

### Separation of Concerns

| Aspect | Internal Auditor | External Auditor GPT | Internal Arbiter |
|--------|------------------|----------------------|------------------|
| **Scope** | Code quality, architecture | Design validation | Response quality |
| **Speed** | Medium (local) | Fast (cloud) | Fast (local) |
| **Tool Access** | Full (read/write/execute) | None (advisory only) | Full (LM Studio calls) |
| **Authority** | Executive (can fix code) | Advisory (suggests) | Executive (awards karma) |
| **Knowledge Source** | Local codebase | Uploaded docs + OpenAI | Runtime responses |
| **Persistence** | File-based reports | Stateless | CFIA-backed lessons |

### Complementary Coverage

- **Internal Auditor** validates code quality and architecture locally (with tool access)
- **External Auditor GPT** validates designs pre-implementation (cloud-accelerated, no tools)
- **Internal Arbiter** assesses response quality during runtime
- Together they form a **complete quality gate across all stages**

### Human-AI Collaboration

- **Internal Auditor** runs autonomously (on-demand or during dream cycles)
- **External Auditor GPT** serves as cloud-based **thinking partner** for Travis
- **Internal Arbiter** operates autonomously during Luna conversations
- All three feed back into **system evolution** (manual updates, rule refinement, karma tuning)

---

## Usage Guidelines

### For Architects/Developers

**Before implementing a feature:**
1. Draft the design doc
2. Submit to External Auditor GPT
3. Review scores and feedback
4. Iterate if composite < 4.5
5. Implement when approved
6. **Update canonical docs** (see below)
7. Monitor Internal Arbiter during testing

**After implementing a feature:**
1. Update `AIOS_MANUAL.md` with new feature documentation
2. Update `AIOS_EXECUTIVE_SUMMARY.md` if architecture changed
3. Update `MANUAL_TOC.md` if new sections were added
4. Re-upload updated docs to External Auditor GPT
5. Verify GPT has latest context by asking about the new feature

**During runtime monitoring:**
1. Check `arbiter_export.json` weekly
2. Look for declining utility scores
3. Review lessons with low `lingua_calc_depth`
4. Use External Auditor to diagnose patterns
5. Update prompts/systems as needed

### Maintaining the Canonical Documentation

**THE THREE PROTECTED FILES:**

| File | Purpose | Update Trigger | Priority |
|------|---------|----------------|----------|
| `AIOS_MANUAL.md` | Complete system docs | Any feature/core change | CRITICAL |
| `AIOS_EXECUTIVE_SUMMARY.md` | High-level architecture | Major architecture change | CRITICAL |
| `MANUAL_TOC.md` | Navigation structure | New sections in manual | CRITICAL |

**Update Checklist (after every major change):**

- [ ] Update `AIOS_MANUAL.md` with:
  - New feature documentation
  - Usage examples
  - Configuration options
  - Integration points
  - Architecture diagrams (if applicable)

- [ ] Update `AIOS_EXECUTIVE_SUMMARY.md` with:
  - High-level capability changes
  - Architecture shifts
  - New core additions
  - Updated statistics (line counts, module counts)

- [ ] Update `MANUAL_TOC.md` with:
  - New section references
  - Line number updates
  - Subsection additions

- [ ] Verify consistency:
  - All three files align
  - No contradictions
  - References are valid

- [ ] Re-upload to External Auditor GPT:
  - Upload all three updated files
  - Test GPT's knowledge of new features
  - Confirm it can evaluate designs correctly

**Example: Lingua Calc Integration**

After integrating lingua calc, these updates were needed:
- ✅ `LINGUA_CALC_INTEGRATION_COMPLETE.md` created (summary doc)
- ⚠️ `AIOS_MANUAL.md` needs section on lingua calc in Luna core
- ⚠️ `AIOS_EXECUTIVE_SUMMARY.md` needs V5 lingua calc mention
- ⚠️ `MANUAL_TOC.md` needs lingua calc section reference
- ⚠️ External Auditor GPT needs re-upload with updated context

**Protection Policy:**

These files are **PROTECTED** - changes must be:
1. Intentional and reviewed
2. Accurate and complete
3. Consistent across all three files
4. Immediately synchronized to External Auditor GPT

**Think of them as:** The constitution of AIOS. Everything else derives from these.

### For Luna (Internal Use)

The Internal Arbiter runs automatically:
- Every response is assessed
- Karma is adjusted in real-time
- Lessons are stored with calc features
- No manual intervention needed

**Exception:** Emergence Zones bypass penalties (curiosity-driven exploration protected).

---

## Future Enhancements

### Planned (v5.1)

- [ ] Bidirectional feedback: Internal Arbiter summarizes patterns for External Auditor review
- [ ] External Auditor API integration (direct ChatGPT GPT calls from AIOS)
- [ ] Auditor + Arbiter consensus protocol (both must approve major changes)
- [ ] Mirror compression index as third verification layer

### Experimental (v6.0)

- [ ] Multi-auditor ensemble (3+ external evaluators with voting)
- [ ] Adversarial auditor (deliberately challenges designs)
- [ ] Self-modifying evaluation rubrics (learns what "good" means over time)

---

## References

- **Internal Auditor (audit_core):** `main_core/audit_core/audit_v3_sovereign.py`
- **Internal Arbiter:** `luna_core/systems/luna_arbiter_system.py`
- **CFIA System:** `luna_core/systems/luna_cfia_system.py`
- **Linguistic Calculus:** `luna_core/core/luna_lingua_calc.py`
- **Mirror Reflection:** `consciousness_core/biological/mirror.py`
- **AIOS Manual:** `AIOS_MANUAL.md` §2.6 (Audit System - full audit_core docs) and §3.19 (Consciousness)

---

**Created by:** Travis Miner  
**Purpose:** Three-layer evaluation system for biological AI operating system  
**Philosophy:**  
- **Internal Auditor** validates code locally (with tools)
- **External Auditor GPT** validates design in the cloud (with OpenAI knowledge)
- **Internal Arbiter** verifies execution at runtime (with karma)
- Together: Never assume correctness, validate at every layer

