.PHONY: all paper clean check artifact-check site-check tree

all: check paper

paper:
	@echo "Checking for LaTeX compilation tools..."
	@if command -v latexmk >/dev/null 2>&1; then \
		echo "Compiling paper using latexmk..."; \
		cd paper && latexmk -pdf main.tex; \
	elif command -v pdflatex >/dev/null 2>&1; then \
		echo "latexmk not found. Attempting compile using pdflatex and bibtex..."; \
		cd paper && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex; \
	else \
		echo "Error: Neither latexmk nor pdflatex was found in PATH."; \
		echo "Please install a LaTeX distribution (e.g., TeX Live or MiKTeX)."; \
		exit 1; \
	fi

clean:
	@echo "Cleaning LaTeX temporary build files..."
	@cd paper && rm -f *.aux *.log *.out *.toc *.synctex.gz *.fdb_latexmk *.fls *.bbl *.blg *.run.xml *.pdf

check:
	@echo "=== Verifying Repository Layout ==="
	@for dir in paper paper/sections paper/figures paper/tables artifact artifact/tasks artifact/baselines artifact/decapod-runs artifact/scripts artifact/results docs .github .github/ISSUE_TEMPLATE; do \
		if [ -d "$$dir" ]; then \
			echo "[OK]  $$dir/"; \
		else \
			echo "[ERR] Missing directory: $$dir/"; \
		fi \
	done
	@echo "\n=== Checking Tool Dependencies ==="
	@for cmd in latexmk pdflatex bibtex python3 git; do \
		if command -v $$cmd >/dev/null 2>&1; then \
			echo "[OK]  $$cmd is available"; \
		else \
			echo "[WARN] $$cmd is missing"; \
		fi \
	done
	@$(MAKE) artifact-check
	@$(MAKE) site-check

artifact-check:
	@echo "\n=== Validating Research Artifact ==="
	@python3 -B artifact/scripts/validate_artifact.py
	@python3 -B -m unittest discover -s artifact/tests -p 'test_*.py'
	@python3 -c 'import json, pathlib; [json.loads(p.read_text()) for p in pathlib.Path("artifact").rglob("*.json")]; json.loads(pathlib.Path("docs/protocol-manifest.json").read_text()); print("validated JSON syntax")'

site-check:
	@echo "\n=== Validating Static Site ==="
	@python3 -B artifact/scripts/validate_site.py

tree:
	@echo "=== Directory Layout ==="
	@if command -v tree >/dev/null 2>&1; then \
		tree -L 3 -I 'node_modules|.git|.venv|__pycache__'; \
	else \
		python3 -c "import os; \
		def print_tree(path, indent=''): \
			for entry in sorted(os.listdir(path)): \
				if entry.startswith('.') or entry in ['__pycache__', 'node_modules', 'venv', '.venv']: continue; \
				full = os.path.join(path, entry); \
				print(indent + '├── ' + entry); \
				if os.path.isdir(full) and indent.count('│') < 2: \
					print_tree(full, indent + '│   '); \
		print_tree('.')" 2>/dev/null || find . -maxdepth 3 -not -path '*/.*' | sort; \
	fi
