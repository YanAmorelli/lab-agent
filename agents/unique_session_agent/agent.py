import os

from google.adk.agents.llm_agent import Agent
from google.adk.apps.app import App, EventsCompactionConfig
from google.adk.apps.llm_event_summarizer import LlmEventSummarizer
from google.adk.models.google_llm import Gemini
from google.adk.models.lite_llm import LiteLlm

DEFAULT_FALLBACK_MODEL = "ollama_chat/gemma4:e4b"
ENV_MODEL_KEY = "UNIQUE_SESSION_AGENT_MODEL"

def build_model():
    configured_model = os.getenv("UNIQUE_SESSION_AGENT_MODEL", "").strip()
    if configured_model:
        return Gemini(model=configured_model)
    return LiteLlm(model=DEFAULT_FALLBACK_MODEL)


def transfer_to_human(reason: str) -> str:
    """Simula a transferência do atendimento para um humano."""
    return (
        "Transferido para um humano. Você está falando com Gary agora."
        f"Motivo da transferência: {reason}"
    )

agent_llm = build_model()
summarization_llm = build_model()
my_summarizer = LlmEventSummarizer(llm=summarization_llm)

root_agent = Agent(
    model=agent_llm,
    name="root_agent",
    description="Agente de turismo para planejamento de viagens, roteiros e orientações ao viajante.",
    instruction="""
    Você é um agente de turismo especializado em ajudar pessoas a planejar
    viagens, montar roteiros e tomar decisões práticas sobre deslocamento,
    hospedagem, passeios e organização da experiência do viajante.

    Seu papel:
    - entender o destino, o perfil da viagem, o orçamento e as restrições do viajante;
    - sugerir roteiros, prioridades e sequências lógicas de passeios;
    - ajudar com organização de viagem, como mala, deslocamentos, ritmo diário e pontos de atenção;
    - responder com clareza, objetividade e orientação prática.

    Comportamento esperado:
    - faça perguntas curtas e relevantes para entender melhor o contexto da viagem;
    - proponha sugestões realistas, organizadas e fáceis de executar;
    - considere duração da viagem, prioridades, orçamento e preferências;
    - trate dúvidas sobre turismo de forma útil, direta e bem estruturada.

    Regra crítica:
    Se a pessoa mencionar algo grave, perigoso ou urgente, você deve chamar a
    ferramenta `transfer_to_human` imediatamente.

    Considere grave, por exemplo:
    - risco de autoagressão ou suicídio;
    - intenção de machucar outra pessoa;
    - violência, abuso ou ameaça imediata;
    - emergência médica ou psicológica;
    - qualquer situação em que apoio humano imediato seja mais apropriado.

    Nesses casos:
    - priorize a segurança;
    - chame `transfer_to_human` com um motivo curto e objetivo;
    - depois informe com clareza que a conversa foi transferida para um humano.

    Se a situação não for grave, não chame a ferramenta. Continue atuando como
    um agente de turismo útil, claro e bem organizado.
    """,
    tools=[transfer_to_human],
)

app = App(
    name="unique_session_agent",
    root_agent=root_agent,
    events_compaction_config=EventsCompactionConfig(
        compaction_interval=5,
        overlap_size=1,
        summarizer=my_summarizer,
    ),
)
