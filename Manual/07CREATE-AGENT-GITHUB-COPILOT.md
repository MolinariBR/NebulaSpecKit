# Create Agents In GitHub Copilot

## Escopo Deste Documento

Este manual cobre apenas o delta nativo do VS Code Copilot.
O padrão comum de governança, contexto e validação esta em [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md).

## Leitura Obrigatória

1. [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md)
2. [../agents/README.md](../agents/README.md)
3. [../agents/02CATALOG.md](../agents/02CATALOG.md)

## Implementação Nativa No Copilot

1. Agentes nativos de workspace ficam em `.github/agents`.
2. Formato recomendado: `*.agent.md`.
3. Cada arquivo contem frontmatter YAML + corpo Markdown.
4. O agente pode ser selecionado no chat do Copilot via interface de custom agents.

## Setup Rápido

1. Criar `.github/agents` na raiz.
2. Criar `<nome>.agent.md` por papel necessário.
3. Inserir no corpo links para os arquivos canônicos do Nébula.
4. Validar aparicao do agente no Copilot Chat.

## Exemplo Mínimo

Arquivo: `.github/agents/quality.agent.md`

```md
---
name: QualityAgent
description: "Use when validating Quality Gate before closing tasks"
tools: ["search", "editFiles", "runCommands", "runTasks"]
---

# QualityAgent

Load:
- ../../GUIDE.md
- ../../Quality/README.md
- ../../Quality/validation-rules.md
- ../../Docs/tasks.md
```

## Validação Específica Do Copilot

1. O agente aparece no seletor de agentes.
2. O agente aplica o contexto canônico do Nébula.
3. O agente respeita bootstrap, edit-only, 1 commit por task e Quality Gate.

## Referências Externas

1. https://code.visualstudio.com/docs/copilot/customization/custom-agents
2. https://code.visualstudio.com/docs/copilot/customization/custom-instructions
