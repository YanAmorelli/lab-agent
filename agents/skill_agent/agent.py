import logging
import pathlib

from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner
from google.adk.tools import skill_toolset
from google.adk.skills import load_skill_from_dir

from .tools import mcps

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)
logger = logging.getLogger(__name__)

write_code = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "write-code"
)

my_skill_toolset = skill_toolset.SkillToolset(
    skills=[write_code]
)

dev_agent = LlmAgent(
    name = "dev_agent",
    model = "gemini-2.5-flash",
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