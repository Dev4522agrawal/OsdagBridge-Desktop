# Osdag Bridge
## Overview
This repository contains the source code for Osdag bridge component of [Osdag](https://github.com/osdag-admin/Osdag).
## Technical Stack

- **Framework**: PySide6 (Qt for Python)
- **Language**: Python 3.8+
- **Architecture**: Model-View pattern with modular design

## Project Structure

```
OsdagBridge/
├── docs/
├── examples/
├── ResourceFiles/
├── src/
│   └── osdagbridge/
│       ├── cli/               # Command-line interface
│       ├── core/              # Core logic including analysis, solvers, codes, and components
│       │   ├── bridge_components/ # Reusable bridge components
│       │   └── bridge_types/      # Implementations for specific bridge types
│       └── desktop/           # PySide6 GUI
├── tests/                     # Unit and integration tests
├── tools/                     # Utility scripts
└── web/                       # Django + React web stack
    ├── backend/
    └── frontend/
```
## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/garvit000/osdag_bridge.git
cd osdag_bridge
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Dependencies
```
PySide6>=6.5.0
```
## Usage

### Running the Application

Run as a module from src directory:
```bash
python -m osbridge.template_page
```

Generate a report:

```bash
osdagbridge report project.yaml report.pdf
```

### Desktop Application

```bash
python -m osdagbridge.desktop
```

### Web Application

Backend:

```bash
python web/backend/manage.py runserver
```

Frontend:

```bash
cd web/frontend
npm install
npm start
```

---

## Testing

Run the complete test suite:

```bash
pytest -q
```

Continuous integration runs automatically through GitHub Actions (`.github/workflows/ci.yml`).

---

## Development Guidelines

### Key Code Locations
- Core logic: `src/osdagbridge/core/`
- Codes & standards: `src/osdagbridge/core/utils/codes/`
- Bridge types: `src/osdagbridge/core/bridge_types/`
- Components: `src/osdagbridge/core/bridge_components/`
- CLI: `src/osdagbridge/cli/`
- Desktop GUI: `src/osdagbridge/desktop/`
- Web backend/frontend: `web/`

### Contribution Workflow
1. Fork the repository  
2. Create a feature branch  
3. Ensure all tests pass (`pytest`)  
4. Submit a pull request

---

## Acknowledgements

OsdagBridge is part of the Osdag project, promoting open-source tools for steel design education, research, and practice.

---

## License

This project is licensed under the MIT License.  
See the `LICENSE` file for full details.
