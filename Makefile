.PHONY: help setup install data figures tests lint format docs docs-serve arxiv clean

help:  ## Afficher l'aide
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup:  ## Installation complète de l'environnement
	uv sync --extra dev
	pre-commit install
	@echo "✅ Environnement prêt"

install:  ## Installer le package en mode éditable
	uv pip install -e ".[dev]"

data:  ## Construire le dataset maître via DVC
	dvc repro build_master

data-all:  ## Pipeline complète des données
	dvc repro

figures:  ## Générer les 4 figures signature
	uv run python figures/fig1_map.py
	uv run python figures/fig2_scatter_ips_sigma.py
	uv run python figures/fig3_network_louvain.py
	uv run python figures/fig4_trajectories_changepoints.py
	@echo "✅ Figures générées dans figures/output/"

tests:  ## Lancer tous les tests
	uv run pytest -v

tests-fast:  ## Tests rapides
	uv run pytest -v -x --no-cov

lint:  ## Vérification qualité code
	uv run ruff check src/ tests/
	uv run black --check src/ tests/

format:  ## Formatage automatique
	uv run ruff check --fix src/ tests/
	uv run black src/ tests/

docs:  ## Générer la documentation
	uv run mkdocs build

docs-serve:  ## Servir la documentation localement
	uv run mkdocs serve

arxiv:  ## Compiler le paper arXiv
	cd paper_arxiv && $(MAKE) pdf

clean:  ## Nettoyer les fichiers générés
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache htmlcov .coverage

clean-figures:  ## Supprimer les figures générées
	rm -rf figures/output/*

run-all:  ## Pipeline complète
	dvc repro
	make figures
	make tests
	@echo "✅ Pipeline complète terminée"
