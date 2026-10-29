PY := .venv/bin/python

.PHONY: setup test validate metrics sources status report check

setup:
	python3 -m venv .venv
	$(PY) -m pip install -q -e ".[dev]"

test:
	$(PY) -m pytest

validate:
	$(PY) -m ubr validate

metrics:
	$(PY) -m ubr metrics

sources:
	$(PY) -m ubr sources verify

status:
	$(PY) -m ubr status

report:
	$(PY) -m ubr report

check: test validate metrics
