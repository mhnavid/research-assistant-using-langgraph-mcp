# Python version used: 3.11.11

setup:
	pip install -r requirements.txt

	@echo "Setup complete. You can now run the project."

run-mcp:
	mcp dev mcp/server.py

test-graph:
	python tests/test_graph.py

