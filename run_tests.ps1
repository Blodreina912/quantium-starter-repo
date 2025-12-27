# PowerShell script to run the test suite in a CI environment
# This script activates the virtual environment, runs tests, and returns appropriate exit codes

Write-Host "======================================"
Write-Host "Starting Test Suite Execution"
Write-Host "======================================"

# Step 1: Activate the virtual environment
Write-Host "Activating virtual environment..."

$venvPath = "venv\Scripts\Activate.ps1"

if (Test-Path $venvPath) {
    & $venvPath
    Write-Host "✓ Virtual environment activated"
} else {
    Write-Host "ERROR: Virtual environment not found at $venvPath"
    exit 1
}

# Step 2: Run the test suite
Write-Host ""
Write-Host "Running test suite with pytest..."
Write-Host "--------------------------------------"

# Run pytest
pytest test_app.py -v

# Capture the exit code
$testExitCode = $LASTEXITCODE

Write-Host "--------------------------------------"
Write-Host ""

# Step 3: Return appropriate exit code
if ($testExitCode -eq 0) {
    Write-Host "======================================"
    Write-Host "✓ All tests passed successfully!"
    Write-Host "======================================"
    exit 0
} else {
    Write-Host "======================================"
    Write-Host "✗ Tests failed with exit code: $testExitCode"
    Write-Host "======================================"
    exit 1
}