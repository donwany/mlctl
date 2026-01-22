# mlctl CLI

### 1. Project Layout

```text
mlctl/
├── src/
│   └── mlctl/
│       ├── __init__.py
│       └── cli.py
├── pyproject.toml
├── README.md
└── LICENSE
```


---

### 2. `pyproject.toml` (PyPI‑ready)

```toml
[project]
name = "mlctl"
version = "0.1.0"
description = "Machine Learning Platform Control CLI"
readme = "README.md"
requires-python = ">=3.9"
license = { text = "MIT" }
authors = [
    { name = "Theophilus Siameh" }
]

dependencies = [
    "click>=8.1.0"
]

[project.scripts]
mlctl = "mlctl.cli:run"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

```bash
mlctl --help
```

---

### 3. Build & Publish with `uv`

Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate
```

Install locally:

```bash
uv pip install -e .
```

Build the package:

```bash
uv build
```

Publish to **TestPyPI** (recommended first):

```bash
uv publish --repository testpypi
```

Publish to **PyPI** (production):

```bash
uv publish
```

---

### 4. Install from PyPI

```bash
pip install mlctl
mlctl model ls
```

---

## Option B (Legacy – Not Recommended)

This approach uses `setup.py` and `twine`. It is included only for legacy maintenance.

```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```
---


## Install
```bash
pip install pipx
pipx ensurepath

pipx install git+https://github.com/donwany/mlctl.git

# or 
pip install git+https://github.com/donwany/mlctl.git

echo "autoload -U bashcompinit && bashcompinit" >> ~/.zshrc

mlctl --help

```

## Demo

```bash
# deploy model
python mlctl.py model deploy --name randomforest --env prod
# train model
python mlctl.py model train --name randomforest --dataset data.csv --epochs 10
# list model
python mlctl.py model list
# validate data
python mlctl.py data validate --dataset data.csv
# ingest data
python mlctl.py data ingest --format csv --source s3://data
```
