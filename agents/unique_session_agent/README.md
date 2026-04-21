# unique_session_agent

## Finalidade

O `unique_session_agent` é um agente experimental construído para validar e observar o comportamento de compactação de contexto em conversas longas no Google ADK.

Seu propósito principal não é servir como um agente de produção, mas como um ambiente controlado para testes de:

- compactação de eventos de conversa;
- persistência de resumos no histórico da sessão;
- continuidade de contexto após múltiplos ciclos de compactação;
- interação entre o agente principal e o `LlmEventSummarizer`.

## Comportamento do agente

O agente assume o papel de um assistente de turismo. Essa persona foi escolhida para favorecer diálogos multi-turno com continuidade de contexto, como planejamento de viagens, refinamento de roteiros, ajustes de prioridades, mudanças de destino e organização prática da experiência do viajante.

Durante a conversa, o agente:

- ajuda a planejar viagens, roteiros e prioridades de passeio;
- organiza informações como destino, duração, orçamento e preferências;
- mantém um estilo de resposta apropriado para sessões contínuas e refinamento progressivo do planejamento;
- aciona a ferramenta `transfer_to_human` quando identifica conteúdo grave, urgente ou potencialmente perigoso.

Esse desenho permite testar a compactação em um cenário realista de conversa prolongada, sem depender de interações artificiais ou comandos puramente técnicos.

## Configuração de modelo

O agente suporta resolução de modelo por variável de ambiente, com fallback automático.

Ordem de resolução:

1. Se `UNIQUE_SESSION_AGENT_MODEL` estiver definida, o agente utiliza `Gemini(...)` com o valor informado.
2. Se a variável não estiver definida, o agente utiliza `gemma4:e4b` via Ollama com `LiteLlm(model="ollama_chat/gemma4:e4b")`.

A mesma política é aplicada ao modelo principal do agente e ao `LlmEventSummarizer`, para manter consistência durante os testes de compactação.

## Variáveis de ambiente

Consulte o arquivo [.env.example](/Users/amorelliaoyan/projects/personal/lab/lab-agent/agents/unique_session_agent/.env.example).

Exemplo com Gemini:

```dotenv
UNIQUE_SESSION_AGENT_MODEL=gemini-2.5-flash
GOOGLE_API_KEY=seu_google_api_key
```

Exemplo com fallback Ollama:

```dotenv
OLLAMA_API_BASE=http://localhost:11434
```

## Execução

Com o ambiente configurado, o agente pode ser executado via ADK Web a partir da raiz do projeto:

```bash
adk web agents
```

Depois, selecione `unique_session_agent`.

## Observação formal

Este agente deve ser tratado como um artefato de teste para avaliação de compactação de conversa e comportamento de sessão no ADK. Embora possua uma persona conversacional funcional, sua finalidade principal é instrumental e experimental.
