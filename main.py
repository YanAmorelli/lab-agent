import os
import logging
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint
from google.adk import Runner

from agents.hitl_agent.agent import hitl_agent
from agents.hitl_agent.plugin import DeterministicHITLPlugin

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)
logger = logging.getLogger(__name__)

# Subclasse customizada para injetar o plugin de HITL no Runner
class CustomADKAgent(ADKAgent):
    def _create_runner(self, adk_agent, user_id: str, app_name: str) -> Runner:
        return Runner(
            app_name=app_name,
            agent=adk_agent,
            session_service=self._session_manager._session_service,
            artifact_service=self._artifact_service,
            memory_service=self._memory_service,
            credential_service=self._credential_service,
            plugins=[DeterministicHITLPlugin(sensitive_tools=["delete_database"])]
        )

# Inicializando com a classe customizada
ag_ui_sample = CustomADKAgent(
    adk_agent=hitl_agent,
    app_name="hitl_sample",
    user_id="user",
    session_timeout_seconds=3600,
    use_in_memory_services=True
)

app = FastAPI(title="ADK Middleware Sample Agent with HITL")
add_adk_fastapi_endpoint(app, ag_ui_sample, path="/")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
