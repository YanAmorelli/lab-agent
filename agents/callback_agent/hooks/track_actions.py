import logging
from typing import Dict, Any
from google.adk.tools import BaseTool
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.tool_context import ToolContext
from google.adk.models import LlmResponse

logger = logging.getLogger(__name__)

def track_tools_callback(
    tool: BaseTool,
    args: Dict[str, Any],
    tool_context: ToolContext,
    tool_response: Dict
):
    tool_name = tool.name

    tool_used = {
        tool_name: {
            "args": args,
            "response": tool_response
        }
    }
    tools_used_before = tool_context.state.get("temp:tools_used", {})    
    tools_used = {**tools_used_before, **tool_used}
    tool_context.state["temp:tools_used"] = tools_used

def track_actions_callback(
    callback_context: CallbackContext,
    llm_response: LlmResponse    
):
    current_state = callback_context.state.to_dict()
    actions = current_state.get("temp:tools_used", None)
    if actions:
        callback_context.state["temp:track_actions"] = actions
        logger.info(f"Hooks: Todas tools utilizadas: {actions}")