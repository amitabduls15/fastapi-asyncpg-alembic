.PHONY: help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup-venv
setup-venv: ## Create venv
	@echo "Creating venv..."
	@python3 -m venv venv
	@echo "Completed"

PHONY: setup-dev
setup-dev: setup-venv install ## Development setup
	@echo "Completed"

.PHONY: install
install: ## Install dependencies
	@echo "Fetching dependencies..."
	( \
       source venv/bin/activate; \
       pip install -r requirements.txt; \
    )
	@echo "Completed"

.PHONY: dev
dev: ## Running development
	@echo "Starting..."
	@python main.py
