# Create Agents In Windsurf

## Escopo Deste Documento

Este manual cobre apenas o delta nativo do Windsurf.
O padrão comum de governança, contexto e validação esta em [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md).

## Leitura Obrigatória

1. [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md)
2. [../agents/README.md](../agents/README.md)
3. [02AGENTS.md](02AGENTS.md)

## Implementação Nativa No Windsurf

1. Customizacao principal via Rules em `.windsurf/rules`.
2. `AGENTS.md` funciona como memoria/rule compativel.
3. Skills em `.windsurf/skills/<name>/SKILL.md`.
4. Workflows em `.windsurf/workflows/*.md`, invocados manualmente por `/name`.

## Setup Rápido

1. Criar `.windsurf/rules`.
2. Criar uma rule por papel com trigger adequado.
3. Opcional: criar `AGENTS.md` na raiz para regras always-on.
4. Opcional: criar skills e workflows de suporte.

## Exemplo Mínimo

Arquivo: `.windsurf/rules/Nébula-quality-rule.md`

```md
---
trigger: model_decision
description: Use when validating Quality Gate before task closure
---

# Nébula Quality Rule

Load:
- @/GUIDE.md
- @/Quality/README.md
- @/Quality/validation-rules.md
- @/Docs/tasks.md
```

## Validação Específica Do Windsurf

1. Rule ativa com trigger correto.
2. AGENTS.md sem conflito com rules específicas.
3. Workflows invocados por slash command.

## Referências Externas

1. https://docs.windsurf.com/windsurf/cascade/memories
2. https://docs.windsurf.com/windsurf/cascade/workflows
3. https://docs.windsurf.com/windsurf/cascade/skills
4. https://docs.windsurf.com/windsurf/cascade/agents-md
