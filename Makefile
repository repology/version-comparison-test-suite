all: check

check:
	scripts/check.py version-comparison-tests.txt

json: version-comparison-tests.json

version-comparison-tests.json: version-comparison-tests.txt scripts/convert2json.py
	scripts/convert2json.py version-comparison-tests.txt > version-comparison-tests.json
