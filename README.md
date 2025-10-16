# AIOS_clean – Adaptive Intelligence Operating System
## A fully sandboxed AI environment with biologically inspired cognitive architecture
### v5.1: Linguistic Calculus + Three-Layer Evaluation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Tests](https://img.shields.io/badge/tests-see%20report-brightgreen.svg)](./V1_TESTING_COMPLETE.md)
[![Coverage](https://img.shields.io/badge/coverage-see%20report-brightgreen.svg)](./AIOS_ENGINEERING_VALIDATION.md)
[![Code Quality: A+](https://img.shields.io/badge/code%20quality-A%2B-success.svg)](./AIOS_ENGINEERING_VALIDATION.md)
[![Architecture: Modular](https://img.shields.io/badge/architecture-modular-informational.svg)](./docs/WHY_AIOS.md)

**Created by Travis Miner | Open Source (MIT License) | v5.1.0**

**A sandboxed AI operating environment modeled on biological cognition - featuring OS-level isolation, biologically inspired cognitive architecture, STM/LTM memory consolidation, soul fragments (persona modes), autonomous heartbeat, and verified self-modification.**

**V5.1 adds:** biological **consciousness_core** (soul/heart/hemispheres), **Mirror** semantic reflection, **Linguistic Calculus** (interrogative operators), and **Three-Layer Evaluation** (Internal Auditor, External Auditor GPT, Internal Arbiter).

**📄 Executive Summary:** [`AIOS_EXECUTIVE_SUMMARY.md`](./AIOS_EXECUTIVE_SUMMARY.md) - Complete overview  
**🆕 v5 Status:** [`AIOS_V5_FINAL_STATUS.md`](./AIOS_V5_FINAL_STATUS.md) - Biological fusion details

---

## 🚀 Quick Start for AI Assistants

**New to AIOS?** Give new AI conversations this context:

1. **Executive Summary (10 min):** Read [`AIOS_EXECUTIVE_SUMMARY.md`](./AIOS_EXECUTIVE_SUMMARY.md) - Complete condensed overview
2. **Super Quick (30 sec):** Read [`SYSTEM_CARD.md`](./SYSTEM_CARD.md)
3. **Quick Context (5 min):** Read [`docs/AIOS_QUICK_CONTEXT.md`](./docs/AIOS_QUICK_CONTEXT.md)
4. **Navigation (browse):** Check [`MANUAL_TOC.md`](./MANUAL_TOC.md)
5. **Full Manual (~37k lines, ≈660 pages):** [`AIOS_MANUAL.md`](./AIOS_MANUAL.md) - Use RAG search instead!

**Best Practice:** Use `py main.py --rag search "topic"` for instant doc lookup (~12 ms on test hardware).

---

## What is AIOS?

**AIOS (Adaptive Intelligence Operating System)** is an operating system designed specifically for AI components. Unlike traditional AI systems (ChatGPT, AutoGPT, LangChain), AIOS provides:

- **OS-Level Sandbox:** NTFS ACLs, separate user (AIOSAUDITOR), verified self-modification
- **Hot-Swappable Cores:** Modular components (~20 cores total) - personality, memory, quality, storage
- **Local-First & Privacy:** Local models (Qwen/Llama) by default, **optional** cloud backends, no data leaves your machine
- **Self-Healing:** Automatic code quality with RAG-powered context (1,752 manual sections)
- **Adaptive Cognitive Architecture:** Biologically inspired personality system with soul fragments (persona modes)

> *Philosophy: "Whatever you want it to do."*

Just like Windows doesn't "do" anything until you install applications, AIOS is a kernel + pluggable AI cores. Use all cores, pick just one for your project, or create your own.

### Why I Built This

I built AIOS because I needed an AI system that actually respects how neurodivergent minds work - modular, swappable, with clear boundaries and honest metrics. No monolithic black boxes. No cloud dependencies that feel like surveillance. Just local, verifiable, modular intelligence I can trust.

The biological consciousness model came from studying how my own brain works - STM/LTM consolidation during "dream" cycles, different personality fragments for different contexts, autonomous background processing. AIOS is what I wish existed when I started this journey.

## 🆕 New Features (V5.1 – Biological Consciousness & Three-Layer Evaluation)

### **Three-Layer Evaluation Architecture**
- **Internal Auditor (V3 Sovereign):** Local audit system with full tool access, modify-only fixes with verified promotion
- **External Auditor GPT:** Cloud-based design-time audit using OpenAI knowledge, advisory-only, no file creation
- **Internal Arbiter:** Runtime response quality assessment, karma tracking, efficiency metrics

> Note: "V3 Sovereign Audit" refers to the internal auditor engine version. The overall evaluation architecture is V5.1.

**Self-Healing System**
- **LLM-Powered Fixes:** Local instruct model used by internal auditor (configurable)
- **Sandbox Safety:** Modify-only changes with automatic rollback
- **Dream Integration:** Healing during system sleep cycles
- **Backup Integration:** Seamless restore on failed fixes

**Linguistic Calculus (V5.1)**
- **Six Operators:** Why/How/What/Where/When/Who for graph-based reasoning
- **Rewrite Rules:** Algebraic compression (Why+Why→How, Why+How→What)
- **Mirror Integration:** Semantic reflection with compression_index tracking
- **Arbiter Tracking:** Stores depth/gain metrics for quality assessment

### **Full Automation Suite**
- **Daily Audit** (9 AM) - System health monitoring
- **Dependency Check** (6 AM) - Security scanning
- **Dream Consolidation** (7 AM) - Memory optimization
- **Weekly Backup** (8 AM) - Data protection
- **Performance Monitor** (10 AM) - Metrics tracking
- **Luna Summary** (11 AM) - Activity reports
- **Pre-commit Hooks** - Every commit audited

### **Documentation**
- **Comprehensive Manual** - Complete user guide (~37k lines)
- **Separate TOC** - Quick navigation with line numbers
- **Organized Docs** - Structured documentation index

---

## Quick Start

### Option 1: Setup Wizard (Recommended)

```powershell
.\setup.ps1
```

The wizard will:
1. Create Python virtual environment
2. Install all dependencies
3. Verify LM Studio connection
4. Launch Streamlit UI automatically

### Option 2: Manual Setup

```powershell
# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements-production.txt

# Launch Streamlit UI (simple dashboard)
streamlit run streamlit_app.py

# Or use full dashboard
streamlit run streamlit_core/streamlit_app.py

# Or use CLI mode
python main.py
```

---

## Requirements

- **Python:** 3.11 or higher
- **LM Studio:** Running on localhost:1234 (or configure alternative endpoint)
- **Model:** Any chat-capable LLM (recommended: Dolphin-Mistral-24B, Llama-3-70B)
- **RAM:** 8 GB minimum (16 GB recommended for large models)
- **OS:** Windows 10/11, Linux, macOS

---

## Core Features

### Luna AI Personality System

Luna adapts her communication style based on Big Five personality traits:

- **Openness:** Creative vs practical responses
- **Conscientiousness:** Detailed vs concise answers
- **Extraversion:** Warm vs reserved tone
- **Agreeableness:** Supportive vs analytical stance
- **Neuroticism:** Stability and consistency

Trait weights adapt based on conversation context and user preferences.

### CARMA Fractal Memory

Hierarchical memory system that:
- Stores conversation fragments with semantic embeddings
- Automatically consolidates related memories
- Retrieves relevant context during conversations
- Learns long-term patterns from interactions
- **Semantic compression:** Consolidates redundant meaning across memory fragments

**Compression Architecture (Clarification):**

**Semantic memory, not prompt shrinking.** CARMA compresses meaning; LUNA's token limits are a separate, optional runtime optimization.

AIOS has two independent mechanisms:

**1) Semantic Compression (Required)** – `carma_core/core/compressor.py`
- Consolidates redundant **meaning** across fragments (concept extraction, similarity, temporal/hierarchical grouping)
- No references to tokens, budgets, or LUNA
- Disabling LUNA's token system does **not** change CARMA behavior
- **Example:** "Quantum computers use superposition" + "Qubits exist in multiple states" + "Measurement collapses superposition" → ONE consolidated concept

**2) Token Budgeting (Optional, Generation Only)** – `luna_core/core/response_generator.py`
- Sets `max_tokens` tiers (e.g., LOW=200; MODERATE/CRITICAL=80) to control verbosity
- Affects **response length**, not memory semantics or CARMA compression
- **Example:** Luna generates "Quantum computers use superposition" (5 tokens) instead of verbose explanation (20+ tokens)

**Key point:** AIOS reduces *information redundancy*, not just *string length*. Semantic compression persists even with token budgets disabled.

### Existential Budget System

Luna operates under token economy constraints:
- **Token Pool:** Generational budget for responses
- **Karma System:** Quality-based advancement mechanism
- **AIIQ (Generation):** Evolutionary lifecycle tracking
- **Resource Awareness:** Self-regulates token usage

### Intelligent Orchestration

- **Adaptive Routing:** A/B testing between model backends
- **Cost Tracking:** Monitor and optimize LLM expenses
- **Canary Deployments:** Safe feature rollouts
- **Health Monitoring:** System status and diagnostics
- **Resilience Policies:** Retry logic, timeouts, circuit breakers

---

## Architecture

AIOS is built on a modular core ecosystem (~20 cores total). Featured cores:

| Core | Purpose | Key Features |
|------|---------|--------------|
| **luna_core** | AI personality & conversation | Trait classification, response generation, arbiter assessment |
| **carma_core** | Memory & learning | Fractal cache, analytics, consolidation, mycelium network |
| **dream_core** | Background processing | Meditation cycles, memory consolidation, cost optimization |
| **data_core** | Data management | Pipeline, database, cleanup, statistics |
| **support_core** | Infrastructure | Logging, security, health checks, embeddings, config |
| **utils_core** | Utilities | Resilience, monitoring, validation, bridges (Rust/PowerShell) |
| **enterprise_core** | Production features | QEC integration, standards checking |
| **rag_core** | Retrieval systems | Simple RAG implementation |
| **streamlit_core** | Web interface | Streamlit UI components |
| **backup_core** | Backup & recovery | System backup, archive management |

**Plus emerging cores:** fractal_core (optimization), template_core (templating), privacy_core, marketplace_core, music_core, game_core, consciousness_core (biological cognition)

---

## AIOS_clean — Canonical Baseline

**AIOS_clean** is the canonical Adaptive Intelligence Operating System baseline.

All derivative builds (e.g., `AIOS_clean_Sovereign`, `AIOS_clean_Marketplace`) inherit validated architecture and can modify non-core systems.

**Naming convention:**
- `AIOS_clean` - Canonical baseline (this repo)
- `AIOS_clean_<Focus>` - Specialized derivatives
- Maintains traceability to verified lineage

This framing defines a taxonomy for the AIOS ecosystem - like Hugging Face for models, but for operating systems.

---

## Validation & Quality

AIOS has undergone comprehensive testing and validation:

### Test Results

- ✅ **Comprehensive pytest suite PASS** (see reports for details, 100% critical paths)
- ✅ **134 Python files validated** (syntax + imports)
- ✅ **35/36 JSON configs valid** (97%)
- ✅ **23 root scripts validated** (100%)
- ✅ **Zero critical errors, warnings, or placeholder code**

### Industry Standards Compliance

AIOS meets all six critical factors for legitimate AI-assisted development:

1. ✅ **Human Oversight** - Systematic code review, zero blind acceptance
2. ✅ **Code Comprehension** - All modules documented, zero black boxes
3. ✅ **Testing Rigor** - Multi-phase validation (syntax → import → functional)
4. ✅ **Security Validation** - PII redaction, JSON validation, import security
5. ✅ **Maintainability** - Modular architecture, comprehensive logging
6. ✅ **Production Readiness** - Health checks, monitoring, resilience policies

**Third-party validation:** 9.4/10 composite score for development methodology

### Documentation

- **[V1_TESTING_COMPLETE.md](./V1_TESTING_COMPLETE.md)** - Comprehensive test results and quality metrics
- **[AIOS_ENGINEERING_VALIDATION.md](./AIOS_ENGINEERING_VALIDATION.md)** - Industry standards compliance report
- **[AIOS_TECHNICAL_VALIDATION_REPORT.md](./AIOS_TECHNICAL_VALIDATION_REPORT.md)** - Formal academic validation with meta-assessment

---

## Usage Examples

### Basic Conversation

```python
from luna_core.luna_chat import chat_with_luna

# Start conversation
response = chat_with_luna("Tell me about quantum computing")
print(response)
```

### Personality Configuration

```python
from luna_core.systems.luna_trait_classifier import LunaTraitClassifier

classifier = LunaTraitClassifier()
traits = classifier.classify_traits("I want a creative, detailed explanation")
# Returns: {'openness': 0.9, 'conscientiousness': 0.8, ...}
```

### Memory Operations

```python
from carma_core.fractal_mycelium_cache import FractalMyceliumCache

cache = FractalMyceliumCache()
cache.store("quantum_computing", "Quantum computers use superposition...")

# Later retrieval
results = cache.search("quantum physics")
# Returns relevant stored fragments
```

### Semantic Compression Demo

```python
from carma_core.core.compressor import CARMAMemoryCompressor

compressor = CARMAMemoryCompressor()

# Three paraphrases of same concept
fragments = [
    {'content': 'Quantum computers use superposition', 'timestamp': 1},
    {'content': 'Qubits exist in multiple states simultaneously', 'timestamp': 2},
    {'content': 'Measurement collapses quantum superposition', 'timestamp': 3}
]

result = compressor.compress_memory(fragments, algorithm='semantic')

print(f"Fragments: {len(fragments)} → {len(result['compressed_fragments'])}")
print(f"Compression: {result['compression_ratio']:.1%}")
# Output: Fragments: 3 → 1-2 (consolidated by meaning, not token count)
#         Compression: 33-66% (information redundancy removed)
```

### Cost Tracking

```python
from utils_core.monitoring.cost_tracker import CostTracker

tracker = CostTracker()
summary = tracker.get_session_summary()
print(f"Total tokens: {summary['total_tokens']}")
print(f"Estimated cost: ${summary['total_cost_usd']:.4f}")
```

---

## Configuration

### LM Studio Setup

1. Download and install [LM Studio](https://lmstudio.ai/)
2. Load a chat model (Mistral, Llama, etc.)
3. Start local server (Settings → Local Server → Start)
4. Default endpoint: `http://localhost:1234/v1`

### AIOS Configuration

Edit `data_core/config/aios_config.json`:

```json
{
  "lm_studio": {
    "endpoint": "http://localhost:1234/v1",
    "model": "dolphin-mistral-24b",
    "temperature": 0.7,
    "max_tokens": 2000
  },
  "luna": {
    "default_personality": "balanced",
    "token_pool": 64000,
    "karma_threshold": 1000
  },
  "carma": {
    "cache_size_mb": 500,
    "consolidation_interval_hours": 24
  }
}
```

---

## Development

### Running Tests

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run all functional tests
pytest archive_dev_core/dev_core/tests/unit/ -v

# Run specific core tests
pytest archive_dev_core/dev_core/tests/unit/test_luna_core_functional_pytest.py
pytest archive_dev_core/dev_core/tests/unit/test_carma_core_functional_pytest.py

# Run integration tests
pytest archive_dev_core/dev_core/tests/integration/ -v
```

### Code Quality

```powershell
# Validate syntax
python -c "import ast; ast.parse(open('luna_core/luna_chat.py', encoding='utf-8').read())"

# Check file standards
python enterprise_core/aios_standards_checker.py

# Run benchmarks
python archive_dev_core/dev_core/tests/benchmark/benchmark_layers.py
```

### Rust Modules (Optional)

If cargo is available:

```powershell
# Test Rust modules
cd luna_core/rust_luna && cargo test
cd carma_core/rust_carma && cargo test
cd utils_core/rust_utils && cargo test
```

---

## Project Philosophy

AIOS embodies **responsible AI-assisted development:**

> *"The real innovation comes from maintaining deep understanding while embracing AI's capabilities... true engineering excellence isn't about velocity – it's about building systems you can understand, maintain, and evolve."*

### Development Methodology

- **Human-AI Collaboration:** Human architect defines vision, AI assists implementation
- **Rigorous Validation:** Zero-tolerance for errors, comprehensive testing
- **Modular Design:** Clear boundaries, isolated concerns, testable components
- **Production Focus:** Beyond prototype - built for real-world deployment

See [archive_dev_core/vibecodeing.md](./archive_dev_core/vibecodeing.md) for research on AI-assisted development practices.

---

## Roadmap

### Current (v1.0.0)
- ✅ Luna personality system operational
- ✅ CARMA memory fully functional
- ✅ Fractal optimization policies
- ✅ Streamlit UI
- ✅ Production validation complete

### Next (v1.1.0)
- [ ] Rust module performance optimization
- [ ] Multi-LLM backend support (OpenAI, Claude, Ollama)
- [ ] Advanced memory graph visualization
- [ ] Mobile-responsive UI
- [ ] CI/CD pipeline with automated testing

### Future (v2.0.0)
- [ ] Self-improving architecture (bounded mutation)
- [ ] Multi-agent collaboration
- [ ] Advanced security audit compliance
- [ ] Load balancing and horizontal scaling

---

## Performance

**Benchmarks (on test hardware):**

| Operation | Latency | Notes |
|-----------|---------|-------|
| Luna response (cached) | ~50ms | CARMA cache hit |
| Luna response (uncached) | ~2000ms | LLM inference + CARMA search |
| Memory search | ~100ms | Semantic similarity search |
| Memory consolidation | ~5000ms | Background processing |
| Pytest suite | 1.05s | Full regression test |

**Resource usage:**
- Memory: ~500 MB (Python) + model memory (LM Studio)
- Disk: ~50 MB (code) + variable (conversation storage)
- CPU: Minimal (I/O bound, waiting for LLM)

---

## Security

AIOS implements multiple security layers:

- **PII Redaction:** Automatic detection and redaction of emails, phones, sensitive data
- **JSON Validation:** Schema validation prevents injection attacks
- **Import Security:** All imports validated before execution
- **Secure Logging:** Sanitized outputs, no secrets in logs, import validation, schema checks
- **Access Control:** Designed for SOC 2 / ISO 27001 compliance extension

**Security guarantees:** No secrets in logs, import validation on all dynamic loads, schema checks on all JSON configs.

See [AIOS_TECHNICAL_VALIDATION_REPORT.md](./AIOS_TECHNICAL_VALIDATION_REPORT.md) Section 4.1 for complete security validation details.

---

## Contributing

AIOS is currently a single-maintainer project. Contributions welcome via:

1. **Issues:** Report bugs or suggest features
2. **Pull Requests:** Code improvements (must pass pytest suite)
3. **Documentation:** Improve guides and examples
4. **Testing:** Add test coverage for new features

**Before contributing:**
- Read validation docs to understand quality standards
- Run `pytest` to ensure tests pass
- Follow modular architecture (add to appropriate core)
- Document all changes

---

## Credits

**Created and Owned by:** Travis Miner  
**Development:** Human-AI collaborative methodology (Travis Miner + Kia/Cursor AI Assistant)

**Methodology:** Human-AI pair programming with rigorous validation

**Validated by:** 
- Technical testing (comprehensive pytest suite)
- Human comprehension assessment (9.5/10 theoretical understanding)
- Third-party AI evaluation (ChatGPT-4: 9.4/10 composite score)

**Built with:**
- Python 3.11
- Rust (performance-critical modules)
- Streamlit (UI)
- LM Studio / Ollama (LLM inference)
- pytest (testing framework)

---

## Verification & Testing

AIOS has comprehensive test coverage and proof of modular architecture:

### Test Suites
- **[Unit Tests](./archive_dev_core/dev_core/tests/unit/)** - Comprehensive functional tests across all cores (see reports)
- **[Integration Tests](./test_modular_integration_full.py)** - 6-level modular integration (Raw LLM → Luna → CARMA → Full)
- **[Compression Tests](./test_compression_architecture_verification.py)** - 11 tests proving semantic ≠ token compression

### Verification Documentation
- **[Modular Verification](./docs/MODULAR_VERIFICATION.md)** - Test matrix proving layer independence
- **[Luna Budget Demo](./docs/LUNA_BUDGET_DEMO.md)** - Token budget ON vs OFF comparison
- **[Quick Reference](./VALIDATION_QUICK_REFERENCE.md)** - Defense cheat sheet for technical challenges

### Validation Reports
- **[V1 Testing Complete](./V1_TESTING_COMPLETE.md)** - Comprehensive test suite PASS, see report for details
- **[Engineering Validation](./AIOS_ENGINEERING_VALIDATION.md)** - Industry standards compliance (6/6 factors)
- **[Technical Validation](./AIOS_TECHNICAL_VALIDATION_REPORT.md)** - Academic validation with meta-assessment (9.4/10)

### Research Foundation
- **[Vibe Coding Research](./archive_dev_core/vibecodeing.md)** - Industry context for AI-assisted development
- **[Future Enhancements](./FUTURE_ENHANCEMENTS.md)** - Roadmap for v1.1+ improvements

**Key Achievement:** AIOS demonstrates that AI-assisted development can achieve production quality (9.4/10 professional standard) when combined with rigorous engineering discipline.

---

## License

**MIT License** - Free to use, modify, and distribute.  
**Copyright © 2025 Travis Miner** - All rights reserved for original work; MIT terms for distribution.

See [LICENSE](./LICENSE) file for full terms.

**This is open source** - Download, fork, modify as you wish. Attribution appreciated but not required for commercial use.

**Summary:** Free to use, modify, and distribute. No warranty provided.

---

## Support

### Documentation
- **Quick Start:** This README
- **Installation Guide:** [README_INSTALL.md](./README_INSTALL.md)
- **Testing Docs:** [V1_TESTING_COMPLETE.md](./V1_TESTING_COMPLETE.md)
- **Validation Reports:** [AIOS_ENGINEERING_VALIDATION.md](./AIOS_ENGINEERING_VALIDATION.md)
- **Troubleshooting:** See "Troubleshooting" section above

### Common Issues

**Q: LM Studio won't connect**  
A: Verify server is running at http://localhost:1234/v1/models

**Q: Import errors**  
A: Activate venv: `.\venv\Scripts\Activate.ps1` and reinstall requirements

**Q: Slow responses**  
A: Use smaller model (Q4 quantization) or reduce max_tokens

**Q: Tests failing**  
A: Ensure venv is activated and pytest is installed: `pip install pytest`

### Contact

- **Repository:** https://github.com/Nemeca99/AIOS
- **Issues:** https://github.com/Nemeca99/AIOS/issues

---

## Acknowledgments

**Theoretical Foundations:**
- Big Five personality model (academic psychology)
- Fractal compression theory (mathematics)
- Control theory and epistemic grounding (systems engineering)

**Tools & Frameworks:**
- Python Software Foundation
- Rust programming language
- Streamlit framework
- pytest testing framework
- LM Studio (local LLM inference)

**Special Thanks:**
- The AI research community for advancing LLM capabilities
- Open source contributors whose libraries power AIOS
- Early testers and feedback providers

---

## Status

**Version:** 1.0.0  
**Status:** Production Ready  
**Last Updated:** October 14, 2025  
**Validation:** Complete (comprehensive test suite, 9.4/10 methodology score - see validation reports)

**Next Milestone:** v1.1.0 (Multi-LLM support, Rust optimization, CI/CD pipeline)

---

*Built for adaptive intelligence. Designed for conversation. Validated for production.*
