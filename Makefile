
.PHONY: install run

install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

run:
	@echo "Starting the application..."
	@adk web adk-example/agent.py
