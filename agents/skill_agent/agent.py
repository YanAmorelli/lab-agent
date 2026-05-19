import logging
import os
import pathlib

from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import skill_toolset
from google.adk.skills import load_skill_from_dir
from google.adk.a2a.utils.agent_to_a2a import to_a2a

from .tools import mcps

DEFAULT_FALLBACK_MODEL = "ollama_chat/gemma4:e4b"
ENV_MODEL_KEY = "SKILL_AGENT_MODEL"
ENV_A2A_PORT_KEY = "SKILL_AGENT_A2A_PORT"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)
logger = logging.getLogger(__name__)


def build_model():
    configured_model = os.getenv(ENV_MODEL_KEY, "").strip()
    if configured_model:
        return Gemini(model=configured_model)
    return LiteLlm(model=DEFAULT_FALLBACK_MODEL)


def get_a2a_port():
    return int(os.getenv(ENV_A2A_PORT_KEY, "8001"))


agent_llm = build_model()

write_code = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "write-code"
)

my_skill_toolset = skill_toolset.SkillToolset(
    skills=[write_code]
)

dev_agent = LlmAgent(
    name = "dev_agent",
    model = agent_llm,
    description = "Agente desenvolvedor de software",
    instruction = f"""Você é um desenvolvedor de software especialista em desenho de soluções e arquitetura. Faz tudo sempre de maneira muito simples.
    O seu objetivo é entender o que o usuário quer construir, entender o contexto e construir tudo que seja necessário.
    Você é um agente equilibrado e tem um pensamento robusto, porém, consegue explicar e chegar nas respostas facilmente. 
    """,
    tools=[
        my_skill_toolset,
        mcps.context7,
        mcps.github_mcp,
    ],
    generate_content_config=types.GenerateContentConfig(
        temperature=0.5,
    ),
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True
        )
    ),
)
root_agent = dev_agent

a2a_app = to_a2a(root_agent, port=get_a2a_port())
