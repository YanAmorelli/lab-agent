import os
import logging
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint

from agents.agent import lab_agent

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)
# Seguindo issue do ADK para suprimir log desnecessário: https://github.com/google/adk-python/issues/2200
logging.getLogger("google_adk.google.adk.tools.base_authenticated_tool").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

ag_ui_sample = ADKAgent(
    adk_agent=lab_agent,
    app_name="ag_ui_sample",
    user_id="user",
    session_timeout_seconds=3600,
    use_in_memory_services=True
)

app = FastAPI(title="ADK Middleware Sample Agent")
add_adk_fastapi_endpoint(app, ag_ui_sample, path="/")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)