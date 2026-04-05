# de-github-copilot

Guia operacional para configurar e executar o Nébula no GitHub Copilot com agentes, workflows, skills e governança auditável por task.

## Objetivo

Padronizar o uso do GitHub Copilot como runtime de execução sem quebrar as regras canônicas do framework.

## Escopo

1. Setup de agentes nativos do Copilot.
2. Mapeamento de caminhos físicos e arquivos obrigatórios.
3. Fluxo de execução no chat com e sem agentes.
4. Validação mínima para fechamento de task.

## Fontes analisadas

### Núcleo do framework

- `README.md`
- `GUIDE.md`
- `Docs/README.md`

### Guias e READMEs dos pilares

- `Manual/00README.md`, `Manual/01GUIDE.md`
- `Skills/00README.md`, `Skills/01GUIDE.md`
- `Workflows/00README.md`, `Workflows/01GUIDE.md`
- `Quality/00README.md`, `Quality/01GUIDE.md`
- `Templates/Full/00README.md`, `Templates/Full/01GUIDE.md`
- `Templates/Quick/00README.md`, `Templates/Quick/01GUIDE.md`
- `agents/00README.md`, `agents/01GUIDE.md`
- `agents/behavior/00README.md`, `agents/behavior/01GUIDE.md`

### Manuais de criação de agentes

- `Manual/15CREATE-AGENT-BASELINE.md`
- `Manual/07CREATE-AGENT-GITHUB-COPILOT.md`

### Documentação web relacionada

- `NebulaWeb/content/docs/ide-github-copilot.md`
- `NebulaWeb/content/docs/agent-platforms-overview.md`
- `NebulaWeb/content/docs/agents.md`
- `NebulaWeb/content/docs/workflows.md`
- `NebulaWeb/content/docs/quality-gate.md`
- `NebulaWeb/content/docs/commands-baseline.md`
- `NebulaWeb/content/docs/commands-agents.md`

## Regra de ouro

1. O contrato canônico dos agentes está em `agents/`.
2. O Copilot é adaptador nativo de runtime.
3. Em conflito, prevalece `agents/` e os guias do framework.

> [!IMPORTANT]
> Nunca mover regras de método para dentro do runtime e tratá-las como fonte de verdade.

## Invariantes que não mudam

1. `Docs/` é saída oficial do projeto.
2. `Templates/` é modelo, não entrega final.
3. `Prototype/` é exclusivo para protótipos HTML.
4. Primeira task: `bootstrap_estrutural`.
5. Após bootstrap: apenas edição de arquivos existentes.
6. Exatamente 1 commit por task.
7. Task só fecha com Quality Gate aprovado.

## Arquitetura de uso no Copilot

| Camada | Local | Responsabilidade |
|---|---|---|
| Contrato canônico | `agents/` | Papéis, contexto obrigatório e handoff |
| Runtime do Copilot | `.github/agents/` | Materialização dos agentes no VS Code |
| Execução oficial | `Docs/` | Plano, tasks, controle e artefatos do projeto |
| Validação | `Quality/` | Critérios do gate e políticas de qualidade |
| Evidência visual | `Prototype/` | Protótipos HTML para validação de interface |

## Setup técnico no VS Code

### Pré-requisitos

1. VS Code atualizado.
2. Extensão GitHub Copilot instalada e autenticada.
3. Repositório aberto na raiz correta do projeto.

### Estrutura nativa do Copilot

```bash
cd /home/mau/molinari/Framework
mkdir -p .github/agents
```

### Arquivo de agente mínimo

Crie um arquivo por papel em `.github/agents/*.agent.md`.

```md
---
name: ExecutionAgent
description: "Use when executing tasks with workflow and quality evidence"
tools: ["search", "editFiles", "runCommands"]
---

# ExecutionAgent

Load:
- ../../GUIDE.md
- ../../Skills/01GUIDE.md
- ../../Workflows/01GUIDE.md
- ../../Quality/01GUIDE.md
- ../../Templates/Full/01GUIDE.md
- ../../Docs/plan.md
- ../../Docs/tasks.md
- ../../Docs/control.md
```

### Sincronização obrigatória com o canônico

1. Validar consistência com `agents/00README.md`.
2. Validar uso correto com `agents/01GUIDE.md`.
3. Validar papel escolhido contra `agents/02CATALOG.md`.

## Contexto obrigatório por chamada

### Base

```text
- GUIDE.md
- Skills/01GUIDE.md
- Workflows/01GUIDE.md
- Quality/01GUIDE.md
- Templates/Full/01GUIDE.md
```

### Especialidade

```text
- agents/<role>-agent.md
```

### Execução (quando houver task)

```text
- Docs/plan.md
- Docs/tasks.md
- Docs/control.md
```

## Prompt base canônico no Copilot Chat

```text
Atue como <AgentName>.
Objetivo: <objetivo da task>
Workflow: Workflows/<workflow>.md

Carregue contexto base:
- GUIDE.md
- Skills/01GUIDE.md
- Workflows/01GUIDE.md
- Quality/01GUIDE.md
- Templates/Full/01GUIDE.md

Carregue contexto especializado conforme agents/<role>-agent.md.
Carregue contexto de execução: Docs/plan.md, Docs/tasks.md e Docs/control.md.

Aplique governança:
- bootstrap apenas na primeira task
- modo edição após bootstrap
- 1 commit por task
- Quality Gate obrigatório

Saída obrigatória:
1) plano
2) execução
3) evidências
4) riscos e pendências
```

## Fluxo recomendado de operação

1. Escolher o modo: com agentes ou sem agentes.
2. Selecionar 1 workflow principal da demanda.
3. Selecionar o agente da etapa (quando aplicável).
4. Executar no Copilot Chat com contexto explícito.
5. Atualizar `Docs/tasks.md` e `Docs/control.md`.
6. Aplicar Quality Gate antes de concluir.

## Exemplos práticos de chamada

### Execução com agente

```text
Atue como ExecutionAgent.
Objetivo: Executar a TASK-023 sem quebrar contrato.
Workflow: Workflows/new-feature.md
Contexto: Docs/plan.md, Docs/tasks.md, Docs/control.md, Docs/contract.yaml
Saída: plano, execução, evidências e atualização do controle.
```

### Execução sem agente

```text
Modo sem agentes.
Objetivo: Corrigir bug com reprodução e validação.
Workflow: Workflows/bug-fix.md
Skills: Skills/logs.md e Skills/tests.md
Contexto: Docs/tasks.md, Docs/control.md
Saída: diagnóstico, correção, evidências e gate.
```

### Mudança com impacto visual

```text
Objetivo: Ajustar UI com impacto em jornada.
Workflow: Workflows/ui-change.md
Skills: Skills/ui-ux.md e Skills/flow.md
Atualizar: Docs/pages.md, Docs/flow.md, Docs/design-system.md e Docs/control.md
Exigir: evidência em Prototype/ e aprovação no Quality Gate.
```

## Checklist de validação no Copilot

1. Agente aparece no seletor do Copilot Chat.
2. Workflow principal está explícito no prompt.
3. Contexto de `Docs/` foi carregado.
4. Task foi atualizada com evidências.
5. `Docs/control.md` reflete o estado real.
6. Gate aprovado antes de concluir.

## Problemas comuns e correção

### Agente não aparece no Copilot Chat

1. Verificar pasta `.github/agents`.
2. Verificar extensão `*.agent.md`.
3. Verificar frontmatter YAML válido.

### Resposta genérica e sem rastreabilidade

1. Declarar workflow explicitamente.
2. Declarar contexto de `Docs/`.
3. Declarar formato de saída obrigatório.

### Task fechada sem evidência

1. Reabrir task em `Docs/tasks.md`.
2. Registrar evidências faltantes.
3. Atualizar `Docs/control.md`.
4. Submeter novamente ao Quality Gate.

## Antipadrões críticos

1. Tratar `.github/agents` como fonte de verdade do método.
2. Omitir `Docs/` no contexto de execução.
3. Fechar task sem gate aprovado.
4. Usar `Templates/` como saída final.
5. Misturar múltiplos objetivos não relacionados no mesmo prompt.

## Comandos úteis

```bash
cd /home/mau/molinari/Framework

# listar agentes canônicos
ls agents

# listar runtime de agentes do Copilot
ls .github/agents

# revisar READMEs e GUIDEs do framework
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort

# revisar estado oficial de execução
ls Docs
```

## Referências

### Internas

1. `Manual/15CREATE-AGENT-BASELINE.md`
2. `Manual/07CREATE-AGENT-GITHUB-COPILOT.md`
3. `agents/00README.md`
4. `agents/01GUIDE.md`
5. `agents/02CATALOG.md`
6. `NebulaWeb/content/docs/ide-github-copilot.md`

### Externas

1. https://code.visualstudio.com/docs/copilot/customization/custom-agents
2. https://code.visualstudio.com/docs/copilot/customization/custom-instructions
