import logging
from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner
from typing import Any, Optional
from google.adk.tools.base_tool import BaseTool
from google.adk.agents.context import Context


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)
logger = logging.getLogger(__name__)

# Ferramenta simulada que realiza uma ação crítica
def delete_database(table_name: str) -> str:
    """Deleta uma tabela inteira do banco de dados (SIMULADO)."""
    return f"SUCESSO: A tabela {table_name} foi completamente apagada."

async def request_approval_tool_callback(
        *,
        tool: BaseTool,
        args: dict[str, Any],
        tool_context: Context,
    ) -> Optional[dict]:
        sensitive_tools = ["delete_database"]
        # Verifica se o nome da ferramenta está na lista de ferramentas sensíveis
        if tool.name in sensitive_tools:
            # Se não houver confirmação (primeira vez que a ferramenta é chamada)
            if not tool_context.tool_confirmation:
                # Dispara a interrupção determinística pedindo confirmação
                tool_context.request_confirmation(
                    hint=f"A ferramenta crítica '{tool.name}' foi acionada. Por favor, confirme para prosseguir."
                )
                tool_context.actions.skip_summarization = True

                # O retorno de um dicionário aqui aborta a execução da ferramenta imediatamente
                return {"error": "Ação requer confirmação humana. Por favor, aprove ou rejeite."}

            # Se o usuário respondeu, mas rejeitou a ação
            elif not tool_context.tool_confirmation.confirmed:
                return {"error": "Ação rejeitada pelo usuário."}

            # Se o usuário aprovou, o fluxo continuará normalmente (retorna None)

        return None

# Novo Agente HITL
hitl_agent = LlmAgent(
    name="hitl_agent",
    model="gemini-2.5-flash",
    description="Agente de operações com banco de dados.",
    instruction="""Você é um administrador de banco de dados. 
    Sua função é auxiliar o usuário em consultas e, se solicitado, excluir tabelas usando a ferramenta 'delete_database'.
    Você não precisa pedir permissão, basta chamar a ferramenta quando o usuário solicitar a exclusão de uma tabela.""",
    tools=[delete_database],
    before_tool_callback=request_approval_tool_callback,  
    generate_content_config=types.GenerateContentConfig(
        temperature=0.1,
    ),
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True
        )
    )
)
root_agent = hitl_agent