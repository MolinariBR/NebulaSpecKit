# Create Agents In Claude Code

## Escopo Deste Documento

Este manual cobre apenas o delta nativo do Claude Code.
O padrão comum de governança, contexto e validação está em [Baseline.md](Baseline.md).

## Leitura Obrigatória

1. [Baseline.md](Baseline.md)
2. [../agents/README.md](../../agents/README.md)
3. [Agents.md](../Agents.md)

## Implementação Nativa No Claude Code

1. Subagents ficam em `.claude/agents` (projeto) ou `~/.claude/agents` (global).
2. Criação recomendada via comando `/agents`.
3. Formato: markdown com frontmatter YAML.
4. Claude Code le `CLAUDE.md`; para usar Agents.md, importar com `@Agents.md`.

## Setup Rápido

1. Executar `/agents` e criar o subagent.
2. Definir `name` e `description` no frontmatter.
3. Inserir no corpo links para contexto canônico.
4. Criar `CLAUDE.md` com `@Agents.md` se necessário.

## Exemplo Mínimo

Arquivo: `.claude/agents/quality.md`

```md
---
name: quality
description: Validate Quality Gate before task closure.
---

Load:
- /Guide-Started.md
- /Quality/README.md
- /Quality/validation-rules.md
- /Docs/tasks.md
```

## Validação Específica Do Claude Code

1. Agente visível em `/agents` e em `claude agents`.
2. Contexto aplicado ao invocar `@"quality (agent)"`.
3. CLAUDE.md ativo quando Agents.md for usado por import.

## Referências Externas

1. https://code.claude.com/docs/en/sub-agents
2. https://code.claude.com/docs/en/settings
3. https://code.claude.com/docs/en/memory
4. https://code.claude.com/docs/en/interactive-mode
