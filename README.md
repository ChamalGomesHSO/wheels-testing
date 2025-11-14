# Wheels Testing Repository

This repository is a test environment for validating pre-built Python wheel files. It provides a boilerplate workflow for testing wheel installation and basic functionality across different platforms and architectures.

## Purpose

The primary purpose of this repository is to:
- Upload pre-generated Python wheel files
- Test if the wheels install correctly on various platforms
- Verify basic functionality of the installed packages

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── test_wheels.yaml    # GitHub Actions workflow for testing wheels
├── libs/
│   └── zxing-cpp/              # Test library configurations
│       ├── pyproject.toml      # Project dependencies and wheel source
│       └── tests/              # Test files for the library
├── wheels/                      # Directory containing pre-built wheel files
└── README.md                    # This file
```

## How It Works

### Workflow Overview

The repository contains a GitHub Actions workflow (`test_wheels.yaml`) that:

1. **Runs on multiple platforms**: Ubuntu (x86_64, ARM64), macOS (x86_64, ARM64)
2. **Selects appropriate wheels**: Each platform uses the corresponding pre-built wheel file
3. **Installs dependencies**: Uses `uv` package manager for fast, reliable installations
4. **Updates configuration**: Dynamically modifies `pyproject.toml` to point to the correct wheel
5. **Runs tests**: Executes pytest to validate the installed package works correctly

### Example: zxing-cpp

The repository currently includes an example configuration for testing `zxing-cpp` wheels:

- **Wheels**: Pre-built wheel files for Python 3.14 on different platforms
- **Tests**: Basic import and version checks
- **Workflow**: Automated testing on Ubuntu, macOS (both x86_64 and ARM64)

## Usage

### Adding New Wheels to Test

1. Place your pre-built wheel files in the `wheels/` directory
2. Create a new test library configuration in `libs/<library-name>/`
3. Add a `pyproject.toml` with dependencies
4. Create test files in `libs/<library-name>/tests/`
5. Update the workflow to include your library

### Running Tests Manually

The workflow is configured to run via `workflow_dispatch`, meaning you can trigger it manually from the GitHub Actions tab.

### Using This as a Template

This repository serves as a boilerplate for testing wheels from other projects (e.g., zxing-cpp). You can:

1. Fork or copy this repository structure
2. Replace the wheel files with your own
3. Update the test library configuration
4. Modify the workflow to match your requirements

## Requirements

- Python 3.14 (or modify `.python-version` and configurations for other versions)
- `uv` package manager (installed automatically by the workflow)
- `pytest` for running tests
- `tomli` and `tomli-w` for TOML file manipulation

## License

This is a test repository. Check individual wheel packages for their respective licenses.
