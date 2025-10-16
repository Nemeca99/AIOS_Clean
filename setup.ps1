# AIOS Setup Wizard
# Interactive configuration and initialization
#
# Usage:
#   .\setup.ps1           # Interactive mode
#   .\setup.ps1 -auto     # Automatic mode (all defaults)

param(
    [switch]$auto
)

$ErrorActionPreference = "Stop"

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "AIOS - Adaptive Intelligence Operating System" -ForegroundColor Cyan
Write-Host "Setup Wizard" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check Python
Write-Host "[1/7] Checking Python Environment..." -ForegroundColor Green

$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ERROR: Python not found" -ForegroundColor Red
    Write-Host "  Please install Python 3.11+ from python.org" -ForegroundColor Yellow
    exit 1
}

Write-Host "  $pythonVersion" -ForegroundColor Gray

# Check version is 3.11+
if ($pythonVersion -match "Python 3\.1([1-9]|[0-9]{2})") {
    Write-Host "  Version check: PASS" -ForegroundColor Green
} else {
    Write-Host "  WARNING: Python 3.11+ recommended" -ForegroundColor Yellow
    $continue = Read-Host "  Continue anyway? (y/N)"
    if ($continue -ne "y") {
        exit 1
    }
}

Write-Host ""

# Step 2: Create Virtual Environment
Write-Host "[2/7] Setting Up Virtual Environment..." -ForegroundColor Green

if (Test-Path ".venv") {
    Write-Host "  Virtual environment exists" -ForegroundColor Gray
} else {
    Write-Host "  Creating .venv..." -ForegroundColor Gray
    python -m venv .venv
    Write-Host "  Created .venv" -ForegroundColor Green
}

# Activate venv
Write-Host "  Activating virtual environment..." -ForegroundColor Gray
& .\.venv\Scripts\Activate.ps1

Write-Host ""

# Step 3: Install Dependencies
Write-Host "[3/7] Installing Dependencies..." -ForegroundColor Green

if ($auto.IsPresent) {
    $install = "Y"
} else {
    $install = Read-Host "  Install required packages? (Y/n)"
}

if ($install -eq "" -or $install -eq "Y" -or $install -eq "y") {
    Write-Host "  Installing from requirements.txt..." -ForegroundColor Gray
    python -m pip install --upgrade pip -q
    python -m pip install -r requirements.txt -q
    Write-Host "  Dependencies installed" -ForegroundColor Green
} else {
    Write-Host "  Skipped" -ForegroundColor Yellow
}

Write-Host ""

# Step 4: Configure LM Studio
Write-Host "[4/7] LM Studio Configuration..." -ForegroundColor Green

if ($auto.IsPresent) {
    $lmEndpoint = "localhost:1234"
    Write-Host "  Using default: $lmEndpoint" -ForegroundColor Gray
} else {
    $lmEndpoint = Read-Host "  LM Studio endpoint (default: localhost:1234)"
    if ($lmEndpoint -eq "") {
        $lmEndpoint = "localhost:1234"
    }
}

Write-Host "  Testing connection to $lmEndpoint..." -ForegroundColor Gray

try {
    $response = Invoke-WebRequest -Uri "http://$lmEndpoint/v1/models" -TimeoutSec 5 -ErrorAction Stop
    Write-Host "  Connection: SUCCESS" -ForegroundColor Green
} catch {
    Write-Host "  Connection: FAILED" -ForegroundColor Yellow
    Write-Host "  Make sure LM Studio is running with server enabled" -ForegroundColor Yellow
}

Write-Host ""

# Step 5: Initialize Data Directory
Write-Host "[5/7] Initializing Data Directories..." -ForegroundColor Green

$dataDir = "data_core/FractalCache"
if (-not (Test-Path $dataDir)) {
    New-Item -ItemType Directory -Path $dataDir -Force | Out-Null
    Write-Host "  Created $dataDir" -ForegroundColor Gray
}

$dataDir2 = "data_core/ArbiterCache"
if (-not (Test-Path $dataDir2)) {
    New-Item -ItemType Directory -Path $dataDir2 -Force | Out-Null
    Write-Host "  Created $dataDir2" -ForegroundColor Gray
}

Write-Host "  Data directories ready" -ForegroundColor Green
Write-Host ""

# Step 6: Run Smoke Test
Write-Host "[6/7] Running Smoke Test..." -ForegroundColor Green

Write-Host "  Testing core imports..." -ForegroundColor Gray

$smokeTest = @"
import sys
try:
    from luna_core.core.luna_core import LunaSystem
    from carma_core.carma_core import CARMASystem
    from fractal_core.fractal_core import FractalCore
    print('PASS')
except Exception as e:
    print(f'FAIL: {e}')
    sys.exit(1)
"@

$smokeTest | python
if ($LASTEXITCODE -eq 0) {
    Write-Host "  Smoke test: PASS" -ForegroundColor Green
} else {
    Write-Host "  Smoke test: FAIL" -ForegroundColor Red
    Write-Host "  Check requirements.txt installation" -ForegroundColor Yellow
}

Write-Host ""

# Step 7: Launch Option
Write-Host "[7/7] Launch AIOS..." -ForegroundColor Green

if ($auto.IsPresent) {
    $launch = "n"
    Write-Host "  Auto mode: Skipping launch" -ForegroundColor Gray
    Write-Host "  Run manually: streamlit run streamlit_app.py" -ForegroundColor Gray
} else {
    $launch = Read-Host "  Launch Streamlit UI? (Y/n)"
}

if ($launch -eq "" -or $launch -eq "Y" -or $launch -eq "y") {
    Write-Host ""
    Write-Host "================================================================" -ForegroundColor Cyan
    Write-Host "Launching AIOS Streamlit UI..." -ForegroundColor Cyan
    Write-Host "================================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Open browser to: http://localhost:8501" -ForegroundColor Yellow
    Write-Host "Press Ctrl+C to stop" -ForegroundColor Gray
    Write-Host ""
    
    streamlit run streamlit_app.py
} else {
    Write-Host ""
    Write-Host "================================================================" -ForegroundColor Cyan
    Write-Host "Setup Complete!" -ForegroundColor Green
    Write-Host "================================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "To launch AIOS:" -ForegroundColor Yellow
    Write-Host "  streamlit run streamlit_app.py" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Or use CLI:" -ForegroundColor Yellow
    Write-Host "  python main.py" -ForegroundColor Gray
    Write-Host ""
}

