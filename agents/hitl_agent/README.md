# hitl_agent

## Finalidade

O `hitl_agent` é um agente experimental voltado à validação de fluxos de aprovação humana no Google ADK.

Seu objetivo principal é demonstrar o padrão de Human-in-the-Loop para operações potencialmente sensíveis, com ênfase em:

- interceptação de chamadas de tool antes da execução;
- solicitação de confirmação humana para ações críticas;
- bloqueio determinístico de execução até aprovação;
- tratamento explícito de aprovação e rejeição.

## Comportamento do agente

O agente assume o papel de um administrador de banco de dados.

Durante a conversa, o agente:

- responde a pedidos relacionados a operações de banco;
- pode acionar a tool `delete_database`;
- submete a execução dessa tool a uma etapa obrigatória de confirmação humana;
- retorna erro controlado quando a ação é rejeitada ou ainda não foi aprovada.

## Tool sensível

O agente expõe a tool:

- `delete_database(table_name: str)`

Essa tool é simulada e retorna uma mensagem de sucesso após a aprovação, mas foi desenhada para representar uma operação destrutiva.

## Fluxo de aprovação

O agente usa `before_tool_callback` para interceptar tools sensíveis. Quando `delete_database` é chamada:

1. se ainda não houver confirmação, o agente solicita aprovação humana;
2. se a ação for rejeitada, a execução é cancelada;
3. se a ação for aprovada, a execução segue normalmente.

Esse fluxo permite testar o comportamento determinístico de confirmação no ADK.

## Modelo

O agente utiliza `gemini-2.5-flash`.

## Variáveis de ambiente

Consulte o arquivo [.env.example](/Users/amorelliaoyan/projects/personal/lab/lab-agent/agents/hitl_agent/.env.example).

Variável esperada:

```dotenv
GOOGLE_API_KEY=
```

## Execução

O agente pode ser executado via ADK Web a partir da raiz do projeto:

```bash
adk web agents
```

Depois, selecione `hitl_agent`.

## Observação formal

Este agente deve ser tratado como um artefato experimental para avaliação de Human-in-the-Loop no ADK. Sua finalidade principal é validar confirmação humana para tools sensíveis e observar o comportamento do runtime diante de ações críticas.
