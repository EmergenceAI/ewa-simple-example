# Emergence Web Agent: Python Usage

An example of how to invoke the [Emergence Web Automation API][1] from Python.

[1]: https://www.emergence.ai/web-automation-api

## Steps to run

This example uses the [uv tool][2] for Python project management. Install uv first.

[2]: https://github.com/astral-sh/uv

To create the virtual environment and install all dependencies:

```bash
uv sync
```

You will need an API key, which you can get from https://dashboard.emergence.ai/. 

Create a file called `.env` in the same directory as this repository, and copy the api key in it. It should look like:

```
EMERGENCE_API_KEY="<your API key>"
```

And finally run the example with

```bash
uv run python emergence_web_agent.py
```
