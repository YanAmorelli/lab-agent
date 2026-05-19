import os

from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

ENV_AGENT_CARD_URL_KEY = "A2A_AGENT_CARD_URL"
ENV_AGENT_DESCRIPTION_KEY = "A2A_AGENT_DESCRIPTION"
ENV_AGENT_NAME_KEY = "A2A_AGENT_NAME"


def required_env(key):
    value = os.getenv(key, "").strip()
    if not value:
        raise RuntimeError(f"{key} must be configured with the remote agent card URL")
    return value


root_agent = RemoteA2aAgent(
    name=os.getenv(ENV_AGENT_NAME_KEY, "skill_agent_proxy"),
    description=os.getenv(ENV_AGENT_DESCRIPTION_KEY, "Proxy A2A para o skill_agent"),
    agent_card=required_env(ENV_AGENT_CARD_URL_KEY),
)
