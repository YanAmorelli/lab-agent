# callback_agent

## Finalidade

O `callback_agent` é um agente experimental voltado à avaliação de callbacks do Google ADK durante o ciclo de execução de tools e respostas do modelo.

Seu objetivo principal é servir como ambiente de teste para:

- execução de tools conectadas por MCP;
- captura de argumentos e respostas de tools após a execução;
- persistência temporária de ações no estado da sessão;
- observabilidade do fluxo do agente por meio de callbacks.

## Comportamento do agente

O agente assume o papel de um agente de laboratório, com perfil generalista para testes e exploração controlada de funcionalidades.

Durante a conversa, o agente:

- responde perguntas gerais;
- pode consultar documentação e contexto técnico via `context7`;
- registra em callbacks as tools utilizadas e seus respectivos parâmetros e resultados;
- consolida essas informações no estado da sessão para inspeção posterior.

## Callbacks

O agente utiliza dois callbacks principais:

- `after_tool_callback`: registra a tool executada, seus argumentos e sua resposta;
- `after_model_callback`: consolida no estado da sessão as ações registradas durante a execução.

Essa estrutura permite validar como o ADK expõe pontos de extensão no fluxo do agente e como esses eventos podem ser rastreados.

## Tools

Atualmente o agente utiliza:

- `context7`, conectado via MCP por `uvx context7-mcp-python`

## Modelo

O agente utiliza `gemini-2.5-flash`.

## Variáveis de ambiente

Consulte o arquivo [.env.example](/Users/amorelliaoyan/projects/personal/lab/lab-agent/agents/callback_agent/.env.example).

Variável esperada:

```dotenv
GOOGLE_API_KEY=
```

## Execução

O agente pode ser executado via ADK Web a partir da raiz do projeto:

```bash
adk web agents
```

Depois, selecione `callback_agent`.

## Observação formal

Este agente deve ser tratado como um artefato experimental para avaliação de callbacks e rastreamento de tools no ADK. Sua função principal é demonstrar e validar extensibilidade do runtime, e não servir como agente final de produção.
