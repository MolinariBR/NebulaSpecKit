# Create Agents In Antigravity

## Escopo Deste Documento

Este manual cobre apenas o delta nativo do Antigravity.
O padrão comum de governança, contexto e validação esta em [Baseline.md](Baseline.md).

## Leitura Obrigatória

1. [Baseline.md](Baseline.md)
2. [../agents/README.md](../../../agents/README.md)
3. [Agents.md](../Agents.md)

## Implementação Nativa No Antigravity

1. Não existe arquivo nativo único de agente por papel.
2. A customizacao e feita por Rules, Workflows e Skills.
3. Rules de projeto ficam em `.agents/rules`.
4. Skills de projeto ficam em `.agents/skills/<name>/SKILL.md`.
5. Workflows são invocados por slash command (`/workflow-name`).

## Setup Rápido

1. Criar `.agents/rules` e `.agents/skills` no projeto.
2. Criar rule por especialidade.
3. Criar skill reutilizável para cenários recorrentes.
4. Usar @mentions para carregar arquivos canônicos.

## Exemplo Mínimo

Arquivo: `.agents/rules/Nébula-quality-rule.md`

```md
# Nébula Quality Rule

Aplicar:
- bootstrap na primeira task
- edit-only após bootstrap
- 1 commit por task
- Quality Gate obrigatório

Carregar:
- @/Guide-Started.md
- @/Quality/README.md
- @/Quality/validation-rules.md
- @/Docs/tasks.md
```

## Validação Específica Do Antigravity

1. Rule ativa no workspace.
2. Skill carregando com frontmatter YAML válido.
3. Workflow invocado por slash sem erro.

## Referências Externas

1. https://antigravity.google/docs/rules-workflows
2. https://antigravity.google/docs/skills
3. https://antigravity.google/docs/agent-modes-settings
