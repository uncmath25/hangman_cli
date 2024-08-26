.PHONY: clean test run

default: run

clean:
	@echo "*** Cleaning repo of unnecessary artifacts... ***"
	rm -rf __pycache__

test: clean
	@echo "*** Testing the project... ***"
	echo "(Not implemented yet...)"

run: test
	@echo "*** Running the Hangman CLI Game.. ***"
	python3 src/run.py
