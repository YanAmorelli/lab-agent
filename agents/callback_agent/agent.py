import logging

from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner

from .hooks.track_actions import track_tools_callback, track_actions_callback
from .tools import mcps

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)
logger = logging.getLogger(__name__)

lab_agent = LlmAgent(
    name = "lab_agent",
    model = "gemini-2.5-flash",
    description = "Agente de laboratório.",
    instruction = f"""Você é um agente de laboratório, o seu objetivo é testar funcionalidades, tools e responder
    perguntas. Você é um agente equilibrado e tem um pensamento robusto, porém, consegue explicar e chegar nas 
    respostas facilmente. 
    Você hoje pode:
        - Buscar informações de um repositório do github através da tool 'read_context';
        - Buscar novas documentações e informações sobre desenvolvimento de software;
        - Responder perguntas sobre conhecimento geral.
    """,
    tools=[mcps.context7],
    generate_content_config=types.GenerateContentConfig(
        temperature=None,
        max_output_tokens=None,        
    ),
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True
        )
    ),
    after_tool_callback=track_tools_callback,
    after_model_callback=track_actions_callback
)
root_agent = lab_agent