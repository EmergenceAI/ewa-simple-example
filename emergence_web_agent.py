import time
from dotenv import load_dotenv
import os
import requests
from typing import Tuple
import json

load_dotenv()
EMERGENCE_API_KEY = os.getenv("EMERGENCE_API_KEY")


def create_workflow(prompt: str) -> str:
    """
    Creates a workflow by sending a request to the Emergence Web Agent with the given prompt.
    Args:
        prompt (str): The prompt given to the web automation agent.
    Returns:
        str: The ID of the created workflow.
    """
    payload = {"prompt": prompt}
    headers = {"apikey": EMERGENCE_API_KEY, "Content-Type": "application/json"}
    url = "https://api.emergence.ai/v0/orchestrators/em-web-automation/workflows"
    response = requests.request("POST", url, json=payload, headers=headers)
    workflowId = response.json()["workflowId"]
    print(f"Workflow ID: {workflowId}")
    return workflowId


def get_workflow_status(workflowId: str) -> Tuple[str, str]:
    """
    Gets the status of a workflow by sending a request to the Emergence Web Agent with the given workflow ID.
    Args:
        workflowId (str): The ID of the workflow to get the status of.
    Returns:
        (str, str): Tuple of (status, result) where status is the status of the workflow and result is the result of the workflow.
    """
    headers = {"apikey": EMERGENCE_API_KEY}
    url = "https://api.emergence.ai/v0/orchestrators/em-web-automation/workflows"
    response = requests.request("GET", f"{url}/{workflowId}", headers=headers)
    response_json = response.json()
    status = response_json["data"]["status"]
    print(f"Workflow Status: {status}")
    result = ""
    if status == "SUCCESS":
        result = response_json["data"]["output"]["result"]
        # Print out the plan that was used to generate the result.
        plan_steps = response_json["data"]["steps"]
        print("Plan Steps:")
        print(json.dumps(plan_steps, indent=4))

    return status, result


def main():
    prompt = "What is the state of venture capital for AI in 2024?"
    workflowId = create_workflow(prompt)

    status, result = get_workflow_status(workflowId)
    while status in ["IN_PROGRESS", "QUEUED", "PLANNING"]:
        time.sleep(10)
        status, result = get_workflow_status(workflowId)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
