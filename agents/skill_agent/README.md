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

## Modelo

O agente utiliza `gemini-2.5-flash`.

## Variáveis de ambiente

Consulte o arquivo [.env.example](/Users/amorelliaoyan/projects/personal/lab/lab-agent/agents/skill_agent/.env.example).

Variáveis esperadas:

```dotenv
GOOGLE_API_KEY=
GITHUB_PAT=
```

## Execução

O agente pode ser executado via ADK Web a partir da raiz do projeto:

```bash
adk web agents
```

Depois, selecione `skill_agent`.

## Observação formal

Este agente deve ser tratado como um artefato experimental para avaliação de skills e composição de ferramentas no ADK. Sua função principal é demonstrar como um agente pode combinar skill local, documentação externa e integrações MCP em um fluxo orientado a desenvolvimento de software.
