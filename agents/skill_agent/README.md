# skill_agent

## Finalidade

O `skill_agent` é um agente experimental voltado à avaliação do mecanismo de skills no Google ADK, combinado com tools externas para apoio a tarefas de desenvolvimento de software.

Seu objetivo principal é servir como ambiente de teste para:

- carregamento de skills locais a partir do diretório do agente;
- composição de skills com toolsets do ADK;
- uso de documentação técnica atual via MCP;
- suporte a tarefas de desenho de solução e implementação assistida.

## Comportamento do agente

O agente assume o papel de um desenvolvedor de software com foco em solução e arquitetura.

Durante a conversa, o agente:

- busca entender o que o usuário deseja construir;
- utiliza a skill local `write-code` como parte do fluxo de trabalho;
- consulta documentação atual via `context7`;
- pode interagir com o GitHub MCP para contexto adicional e operações relacionadas ao repositório.

## Exposição via A2A

Além de rodar como agente ADK local, o `skill_agent` agora expõe um agent card gerado automaticamente pelo ADK.

Esse agent card descreve o agente e permite que outros agentes o consumam via Agent2Agent Protocol. O `a2a_agent`, por exemplo, usa a URL do agent card para criar um `RemoteA2aAgent` e atuar como proxy para o `skill_agent`.

O A2A é um protocolo aberto para comunicação entre agentes. Ele é mais adequado quando o agente remoto roda como serviço separado, precisa ser consumido por outro processo ou deve manter um contrato claro de interoperabilidade. No ADK, o agente produtor é exposto como serviço A2A, enquanto o consumidor usa o agent card para descobrir e acessar o agente remoto.

Referências:

- [Introdução a A2A no ADK](https://adk.dev/a2a/intro/)
- [Documentação oficial do A2A Protocol](https://a2a-protocol.org/latest/)

## Skill carregada

O agente carrega a skill local:

- `write-code`

Essa skill orienta um fluxo que inclui:

- consulta de documentação atual por `context7`;
- elaboração de código com base nessa documentação;
- uso de recursos do GitHub MCP no processo de desenvolvimento.

## Tools

O agente utiliza:

- `SkillToolset` com a skill `write-code`
- `context7`
- `github_mcp`

O `github_mcp` depende da variável de ambiente `GITHUB_PAT` para autenticação no endpoint configurado.

## Modelo e A2A

Por padrão, o agente usa o fallback configurado no código. Para selecionar um modelo Gemini, defina `SKILL_AGENT_MODEL`.

A porta do serviço A2A é configurada por `SKILL_AGENT_A2A_PORT`.

## Variáveis de ambiente

Consulte o arquivo [.env.example](.env.example).

Variáveis esperadas:

```dotenv
GOOGLE_API_KEY=
GITHUB_PAT=
SKILL_AGENT_MODEL=
SKILL_AGENT_A2A_PORT=8001
```

## Execução

O agente pode ser executado via ADK Web a partir da raiz do projeto:

```bash
adk web agents
```

Depois, selecione `skill_agent`.

Para expor o agent card A2A, execute o agente como serviço A2A na porta definida por `SKILL_AGENT_A2A_PORT`. O `a2a_agent` deve ser configurado com a URL do agent card gerado.

## Segurança e configuração

Não versione arquivos `.env` com valores reais. Use apenas `.env.example` para documentar variáveis.

Secrets como `GOOGLE_API_KEY` e `GITHUB_PAT` devem ficar somente no ambiente local ou no gerenciador de secrets do ambiente de execução.

## Observação formal

Este agente deve ser tratado como um artefato experimental para avaliação de skills e composição de ferramentas no ADK. Sua função principal é demonstrar como um agente pode combinar skill local, documentação externa e integrações MCP em um fluxo orientado a desenvolvimento de software.
