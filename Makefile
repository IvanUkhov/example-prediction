all:

%:
	python -m prediction.main --action $@ --config configs/$@.json

.PHONY: all
