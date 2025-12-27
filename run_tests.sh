#!/bin/bash

# Bash script to run the test suite in a CI environment
# This script activates the virtual environment, runs tests, and returns appropriate exit codes

echo "======================================"
echo "Starting Test Suite Execution"
echo "======================================"

# Step 1: Activate the virtual environment
echo "Activating virtual environment..."

# Check if running on Windows (Git Bash) or Unix-like system
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows (Git Bash)
    source venv/Scripts/activate
else
    # Linux/Mac
    source venv/bin/activate
fi

# Verify virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "ERROR: Failed to activate virtual environment"
    exit 1
fi

echo "✓ Virtual environment activated: $VIRTUAL_ENV"

# Step 2: Run the test suite
echo ""
echo "Running test suite with pytest..."
echo "--------------------------------------"

# Run pytest and capture the exit code
pytest test_app.py -v

# Store the exit code
TEST_EXIT_CODE=$?

echo "--------------------------------------"
echo ""

# Step 3: Return appropriate exit code
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "======================================"
    echo "✓ All tests passed successfully!"
    echo "======================================"
    exit 0
else
    echo "======================================"
    echo "✗ Tests failed with exit code: $TEST_EXIT_CODE"
    echo "======================================"
    exit 1
fi