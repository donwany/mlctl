install:
	uv sync
	uv pip install -e .

deploy:
	git init
	git add .
	git commit -m "Initial commit"
	git branch -M main
	git push -u origin main

demo:
	python ./src/mlctl/cli.py model train --name randomforest --dataset data.csv --epochs 10

help:
	@echo "Makefile commands:"
	@echo "  deploy - Initialize git repository and push to main branch"
	@echo "  help   - Show this help message"