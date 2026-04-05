# Create Agents In OpenCode

## Escopo Deste Documento

Este manual cobre apenas o delta nativo do OpenCode.
O padrão comum de governança, contexto e validação está em [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md).

## Leitura Obrigatória

1. [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md)
2. [../agents/00README.md](../agents/00README.md)
3. [../agents/02CATALOG.md](../agents/02CATALOG.md)

## Implementação Nativa No OpenCode

1. Agentes custom podem ser definidos em `opencode.json` (chave `agent`).
2. Tambem podem ser definidos em `.opencode/agents/*.md`.
3. O projeto usa regras em `AGENTS.md` (ou `CLAUDE.md` por compatibilidade).
4. Skills ficam em `.opencode/skills/<name>/SKILL.md`.
5. Commands ficam em `.opencode/commands/*.md` e podem fixar agente.

## Setup Rápido

1. Criar agente via `opencode agent create` ou arquivo markdown.
2. Validar com `opencode agent list`.
3. Criar AGENTS.md (ou usar `/init`) para guardrails.
4. Opcional: fixar agente por comando em `.opencode/commands`.

## Exemplo Mínimo

Arquivo: `.opencode/agents/quality-agent.md`

```md
---
description: Validate Quality Gate before task closure.
mode: subagent
---

Load:
- @/GUIDE.md
- @/Quality/01GUIDE.md
- @/Quality/gate.md
- @/Docs/tasks.md
```

## Validação Específica Do OpenCode

1. Agente aparece em `opencode agent list`.
2. Invocacao por `@quality-agent` funciona.
3. Regras de AGENTS.md entram em contexto do projeto.

## Referências Externas

1. https://opencode.ai/docs/pt-br/agents
2. https://opencode.ai/docs/pt-br/rules
3. https://opencode.ai/docs/pt-br/skills
4. https://opencode.ai/docs/pt-br/commands
5. https://opencode.ai/docs/pt-br/config
