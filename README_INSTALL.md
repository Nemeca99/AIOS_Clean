# AIOS Installation Guide

**Version:** 1.0.0  
**Last Updated:** October 13, 2025

---

## System Requirements

- **Python:** 3.11 or higher
- **OS:** Windows 10/11, macOS, Linux
- **RAM:** 8 GB minimum (16 GB recommended)
- **Storage:** 2 GB for AIOS + space for models
- **LM Studio:** Required for AI model inference

---

## Quick Start

### 1. Extract AIOS

```powershell
# Extract the ZIP
Expand-Archive AIOS_Install.zip -DestinationPath AIOS
cd AIOS
```

### 2. Run Setup Wizard

```powershell
.\setup.ps1
```

The wizard will:
- Check Python version
- Create virtual environment
- Install dependencies
- Configure LM Studio connection
- Initialize data directories
- Run smoke test
- Launch Streamlit UI

### 3. Use AIOS

Browser opens to `http://localhost:8501`

Chat with Luna using natural language.

---

## Manual Installation (Advanced)

### 1. Install Dependencies

```powershell
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.\.venv\Scripts\Activate.ps1

# Install packages
pip install -r requirements.txt
```

### 2. Configure LM Studio

1. Download and install LM Studio from lmstudio.ai
2. Load a model (recommended: Dolphin-Mistral-24B)
3. Enable local server (localhost:1234)
4. Verify: http://localhost:1234/v1/models

### 3. Initialize AIOS

```powershell
# Test imports
python -c "from luna_core.core.luna_core import Luna; print('OK')"

# Launch Streamlit
streamlit run streamlit_app.py

# Or use CLI
python main.py
```

---

## LM Studio Setup

### Recommended Models

**Primary Model (Required):**
- Model: cognitivecomputations/Dolphin-Mistral-24B-Venice-Edition
- Quantization: Q5_K_M
- VRAM: ~5-6 GB

**Draft Model (Optional, for speed):**
- Model: alamios/Mistral-Small-3.1-DRAFT-0.5B  
- Quantization: BF16
- VRAM: ~500 MB

### Configuration

In LM Studio:
1. Load models
2. Server → Enable
3. Port: 1234 (default)
4. CORS: Enable (for local access)

---

## First Run

### Streamlit UI

```powershell
streamlit run streamlit_app.py
```

Opens browser to chat interface.

**Features:**
- Personality trait selection (Big 5)
- Real-time chat with Luna
- Memory persistence (CARMA)
- Token economy visualization

### CLI Mode

```powershell
python main.py
```

Text-based interaction.

---

## Troubleshooting

### Import Errors

**Problem:** `ModuleNotFoundError`

**Solution:**
```powershell
# Ensure venv is activated
.\.venv\Scripts\Activate.ps1

# Reinstall dependencies
pip install -r requirements.txt
```

### LM Studio Connection Failed

**Problem:** `Connection refused` or `404`

**Solution:**
1. Open LM Studio
2. Load a model
3. Enable local server (localhost:1234)
4. Check http://localhost:1234/v1/models in browser

### Streamlit Won't Start

**Problem:** `streamlit: command not found`

**Solution:**
```powershell
# Install streamlit explicitly
pip install streamlit

# Or reinstall all deps
pip install -r requirements.txt
```

### Out of Memory

**Problem:** System crashes or freezes

**Solution:**
1. Use smaller model (Q4 quantization)
2. Reduce context window in config
3. Close other applications
4. Upgrade RAM if possible

---

## Configuration

### config/aios_config.json

Edit this file to customize:

```json
{
  "lm_studio": {
    "endpoint": "http://localhost:1234",
    "model": "your-model-name"
  },
  "luna": {
    "default_trait": "openness",
    "token_pool": 64000
  }
}
```

---

## Updating

### Get Latest Version

1. Download new AIOS_Install.zip
2. Extract to new folder
3. Copy `data_core/` from old installation (preserves memories)
4. Run `.\setup.ps1`

---

## Uninstalling

```powershell
# Deactivate venv (if active)
deactivate

# Delete folder
cd ..
Remove-Item -Recurse -Force AIOS
```

---

## Support

For issues or questions, see the documentation in your installation folder.

---

## License

See LICENSE file in installation directory.

---

*Thank you for using AIOS. Enjoy chatting with Luna!*

