# a2a_agent

## Finalidade

O `a2a_agent` é um proxy A2A para o `skill_agent`.

Ele não recria as skills, tools ou instruções do agente de desenvolvimento. Em vez disso, consome o agent card exposto pelo `skill_agent` e usa essa URL para criar um `RemoteA2aAgent`, que encaminha as chamadas para o agente remoto usando o protocolo Agent2Agent.

## Como funciona

O fluxo esperado é:

1. O `skill_agent` é iniciado como serviço A2A.
2. O ADK gera automaticamente o agent card do `skill_agent`.
3. O `a2a_agent` lê a URL desse agent card por variável de ambiente.
4. O `RemoteA2aAgent` usa o card para descobrir como conversar com o agente remoto.

Na prática, o `a2a_agent` funciona como uma fachada local para um agente publicado em outro processo ou serviço.

## Sobre A2A

O Agent2Agent Protocol é um padrão aberto para comunicação e colaboração entre agentes de IA. Ele é útil quando agentes precisam se comunicar através da rede, quando são mantidos por times diferentes, quando usam frameworks diferentes ou quando a integração precisa de um contrato formal.

No ADK, um agente pode ser exposto como um servidor A2A, e outro agente pode consumi-lo por meio de `RemoteA2aAgent`. O agent card descreve o agente remoto e permite a descoberta das capacidades necessárias para a comunicação.

Referências:

- [Introdução a A2A no ADK](https://adk.dev/a2a/intro/)
- [Documentação oficial do A2A Protocol](https://a2a-protocol.org/latest/)

## Variáveis de ambiente

Consulte o arquivo [.env.example](.env.example).

Variáveis esperadas:

```dotenv
A2A_AGENT_NAME=skill_agent_proxy
A2A_AGENT_DESCRIPTION=Proxy A2A para o skill_agent
A2A_AGENT_CARD_URL=http://localhost:8001/.well-known/agent-card.json
```

`A2A_AGENT_CARD_URL` deve apontar para o agent card gerado pelo `skill_agent`.

## Execução

Primeiro, execute o `skill_agent` como serviço A2A e confirme que o agent card está disponível na URL configurada.

Depois, execute o ADK Web a partir da raiz do projeto:

```bash
adk web agents
```

Selecione `a2a_agent`.

## Segurança e configuração

Não versione arquivos `.env` com valores reais. Use apenas `.env.example` para documentar as variáveis necessárias.

URLs, portas e nomes usados pelo proxy devem ser configurados por variáveis de ambiente para evitar hardcodes no código.
