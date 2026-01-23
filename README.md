## mlctl CLI: Machine Learning Platform Control CLI

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

### 2. Build & Publish with `uv`

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

export PYPI_TOKEN='pypi-'

uv publish --username __token__ --password $PYPI_TOKEN
```


## Install
```bash
pip install pipx

pipx ensurepath

pipx install git+https://github.com/donwany/mlctl.git

# or 
pip install git+https://github.com/donwany/mlctl.git

uv pip install git+https://github.com/donwany/mlctl.git

# argcomplete
echo "autoload -U bashcompinit && bashcompinit" >> ~/.zshrc

```

## Editable Install
```bash
git clone https://github.com/donwany/mlctl.git
cd mlctl
pip install -e .
```

## Versioning via Git Tags
```bash
git tag v0.1.0
git push origin v0.1.0

pip install git+https://github.com/donwany/mlctl.git@v0.1.0

```

## Docker
```bash
# build
docker build -t mlctl .

# run
docker run --rm mlctl
docker run --rm mlctl model list
docker run --rm mlctl model train --name rf --dataset data.csv --epochs 5
docker run --rm mlctl model deploy --name rf --env prod
docker run --rm mlctl data validate --dataset data.csv

docker run --rm \
  -v $(pwd):/data \
  mlctl data ingest --source /data/data.csv

docker run --rm \
  -e MLCTL_ENV=prod \
  -e MLCTL_CONFIG=/config.yml \
  mlctl model deploy --name rf --env prod



```


## Demo: local

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

## Demo: remote
```bash
# help
mlctl --help
# deploy model
mlctl model deploy --name randomforest --env prod
# train model
mlctl model train --name randomforest --dataset data.csv --epochs 10
# list model
mlctl model list
# validate data
mlctl data validate --dataset data.csv
# ingest data
mlctl data ingest --format csv --source s3://data

# Global flags
mlctl --verbose --config config.yml model list
```
