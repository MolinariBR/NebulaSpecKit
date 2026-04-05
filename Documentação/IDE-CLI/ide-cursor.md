# ide-cursor

Guia operacional para configurar e executar o Nébula no Cursor com regras nativas, contexto canônico e fechamento auditável por task.

## Objetivo

Padronizar o uso do Cursor como runtime de execução sem violar contrato de agentes, workflows e governança do framework.

## Escopo

1. Delta nativo do Cursor (`.cursor/rules` e `AGENTS.md`).
2. Contexto obrigatório para chamadas com e sem agentes.
3. Fluxo de operação por task com rastreabilidade.
4. Critérios mínimos de validação antes do fechamento.

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

### Documentação da pasta `agents/`

- `agents/02CATALOG.md`
- `agents/scope-agent.md`
- `agents/product-agent.md`
- `agents/system-agent.md`
- `agents/execution-agent.md`
- `agents/quality-agent.md`
- `agents/release-agent.md`
- `agents/recovery-agent.md`

### Manuais de criação de agentes

- `Manual/15CREATE-AGENT-BASELINE.md`
- `Manual/08CREATE-AGENT-CURSOR.md`

### Documento web atual

- `NebulaWeb/content/docs/ide-cursor.md`

## Regra de ouro

1. `agents/` é a fonte de verdade dos papéis.
2. Cursor é adaptador de runtime.
3. Em conflito, prevalece o contrato canônico do framework.

> [!IMPORTANT]
> Rules e `AGENTS.md` no Cursor não substituem `agents/00README.md` e `agents/01GUIDE.md`.

## Invariantes de operação

1. `Docs/` é destino oficial de execução.
2. `Templates/` é modelo de preenchimento.
3. `Prototype/` é exclusivo para protótipos HTML.
4. Primeira task: `bootstrap_estrutural`.
5. Após bootstrap: apenas edição de arquivos existentes.
6. Exatamente 1 commit por task concluída.
7. Task só fecha com Quality Gate aprovado.

## Delta nativo do Cursor

### Componentes de runtime

1. Rules em `.cursor/rules/` (`.md` ou `.mdc`).
2. `AGENTS.md` na raiz como camada adicional de instruções.
3. Criação rápida de rule via `/create-rule`.

### Organização recomendada

```text
.cursor/
  rules/
    scope-agent.mdc
    product-agent.mdc
    system-agent.mdc
    execution-agent.mdc
    quality-agent.mdc
    release-agent.mdc
    recovery-agent.mdc
AGENTS.md
```

## Arquitetura de uso no Cursor

| Camada | Local | Responsabilidade |
|---|---|---|
| Contrato canônico | `agents/` | Papéis, contexto e handoff |
| Runtime Cursor | `.cursor/rules/` | Gatilhos e comportamento por contexto |
| Camada transversal | `AGENTS.md` | Guardrails gerais do projeto |
| Execução oficial | `Docs/` | Plan, tasks, control e artefatos |
| Qualidade | `Quality/` | Gate e políticas de validação |

## Setup técnico

### 1) Preparar estrutura

```bash
cd /home/mau/molinari/Framework
mkdir -p .cursor/rules
```

### 2) Criar rule por papel

Arquivo exemplo: `.cursor/rules/quality-agent.mdc`

```md
---
description: "Use when validating Quality Gate before task closure"
alwaysApply: false
---

# Nébula Quality Rule

Load:
- GUIDE.md
- Skills/01GUIDE.md
- Workflows/01GUIDE.md
- Quality/01GUIDE.md
- Quality/gate.md
- Docs/tasks.md
- Docs/control.md
```

### 3) Ajustar `AGENTS.md`

1. Centralize regras transversais (governança, precedência e saída mínima).
2. Evite duplicar regras longas já definidas em `agents/` e `Manual/15`.

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

## Prompt base canônico no Cursor

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

1. Escolher modo: com agentes ou sem agentes.
2. Selecionar 1 workflow principal.
3. Selecionar agente da etapa (quando aplicável).
4. Executar no chat com contexto explícito de `Docs/`.
5. Atualizar `Docs/tasks.md` e `Docs/control.md`.
6. Aplicar Quality Gate antes de concluir.

## Exemplos práticos no chat

### Com agente

```text
Atue como ExecutionAgent.
Objetivo: Executar TASK-031 com rastreabilidade completa.
Workflow: Workflows/bug-fix.md
Contexto: Docs/plan.md, Docs/tasks.md, Docs/control.md
Saída: plano, execução, evidências e atualização dos artefatos.
```

### Com agente + skill + workflow

```text
Atue como SystemAgent.
Objetivo: Evoluir integração externa sem quebrar contrato.
Workflow: Workflows/new-integration.md
Skills: Skills/contracts.md, Skills/integration.md, Skills/curl.md
Contexto: Docs/architecture.md, Docs/contract.yaml, Docs/control.md
Saída: contrato atualizado, validação e riscos residuais.
```

### Sem agente

```text
Modo sem agentes.
Objetivo: Ajustar fluxo de UI com impacto em navegação.
Workflow: Workflows/ui-change.md
Skills: Skills/ui-ux.md e Skills/flow.md
Atualizar: Docs/pages.md, Docs/flow.md, Docs/tasks.md e Docs/control.md
Fechar: apenas com Quality Gate aprovado.
```

## Checklist de validação no Cursor

1. Rule correta foi ativada para o contexto.
2. `AGENTS.md` está coerente com as Rules.
3. Workflow principal está explícito no comando.
4. Contexto de `Docs/` está explícito.
5. Evidências registradas em `Docs/tasks.md`.
6. Estado real atualizado em `Docs/control.md`.
7. Gate aprovado antes do fechamento.

## Problemas comuns e correção

### Rules genéricas demais

1. Refinar `description` e gatilho da rule.
2. Separar rules por papel e cenário.

### Conflito entre Rules e `AGENTS.md`

1. Manter `AGENTS.md` apenas com guardrails transversais.
2. Mover especialização para `.cursor/rules`.

### Saída sem rastreabilidade

1. Exigir contexto de execução (`Docs/plan.md`, `Docs/tasks.md`, `Docs/control.md`).
2. Exigir saída em quatro blocos: plano, execução, evidências e pendências.

## Antipadrões críticos

1. Tratar `.cursor/rules` como nova fonte de verdade do método.
2. Executar task sem workflow principal.
3. Omitir contexto de `Docs/` nas chamadas.
4. Fechar task sem Quality Gate.
5. Usar `Templates/` como entrega final.

## Comandos úteis

```bash
cd /home/mau/molinari/Framework

# inventário de regras do Cursor
find .cursor/rules -maxdepth 2 -type f 2>/dev/null | sort

# revisar contrato canônico dos agentes
ls agents

# revisar base de método e guias
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort

# revisar artefatos oficiais de execução
ls Docs
```

## Referências

### Internas

1. `Manual/15CREATE-AGENT-BASELINE.md`
2. `Manual/08CREATE-AGENT-CURSOR.md`
3. `agents/00README.md`
4. `agents/01GUIDE.md`
5. `agents/02CATALOG.md`
6. `NebulaWeb/content/docs/ide-cursor.md`

### Externas

1. https://cursor.com/docs/rules
2. https://cursor.com/docs/rules#agentsmd
