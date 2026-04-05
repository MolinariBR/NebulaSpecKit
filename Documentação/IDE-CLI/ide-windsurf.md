# ide-windsurf

Guia operacional para configurar e executar o Nébula no Windsurf com Rules, Skills e Workflows, mantendo governança e rastreabilidade por task.

## Objetivo

Padronizar o uso do Windsurf como runtime sem romper o contrato canônico do framework.

## Escopo

1. Delta nativo do Windsurf.
2. Estrutura física recomendada.
3. Contexto obrigatório de execução.
4. Fluxo com validação de fechamento.

## Fontes analisadas

### Núcleo do framework

- `README.md`
- `GUIDE.md`
- `Docs/README.md`

### Guias e READMEs do framework

- `Manual/00README.md`, `Manual/01GUIDE.md`
- `Skills/00README.md`, `Skills/01GUIDE.md`
- `Workflows/00README.md`, `Workflows/01GUIDE.md`
- `Quality/00README.md`, `Quality/01GUIDE.md`
- `Templates/Full/00README.md`, `Templates/Full/01GUIDE.md`
- `Templates/Quick/00README.md`, `Templates/Quick/01GUIDE.md`
- `agents/00README.md`, `agents/01GUIDE.md`
- `agents/behavior/00README.md`, `agents/behavior/01GUIDE.md`
- `Prototype/00README.md`, `Prototype/01GUIDE.md`

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
- `Manual/10CREATE-AGENT-WINDSURF.md`

### Documento web atual

- `NebulaWeb/content/docs/ide-windsurf.md`

## Regra de ouro

1. `agents/` é a fonte de verdade dos papéis.
2. Windsurf é adaptador de runtime.
3. Em conflito, prevalece o contrato canônico do framework.

> [!IMPORTANT]
> As configurações em `.windsurf/` não substituem `agents/00README.md` e `agents/01GUIDE.md`.

## Invariantes de governança

1. `Docs/` é saída oficial do projeto.
2. `Templates/` é modelo de preenchimento.
3. `Prototype/` é exclusivo para protótipos HTML.
4. Primeira task: `bootstrap_estrutural`.
5. Após bootstrap: apenas edição de arquivos existentes.
6. Exatamente 1 commit por task.
7. Task só fecha com Quality Gate aprovado.

## Delta nativo do Windsurf

### Componentes de runtime

1. Rules em `.windsurf/rules/`.
2. `AGENTS.md` como memória/rule compatível.
3. Skills em `.windsurf/skills/<name>/SKILL.md`.
4. Workflows em `.windsurf/workflows/*.md`, acionados por `/name`.

### Estrutura recomendada

```text
.windsurf/
  rules/
    scope-agent.md
    execution-agent.md
    quality-agent.md
  skills/
    execution/
      SKILL.md
    quality/
      SKILL.md
  workflows/
    new-feature.md
    bug-fix.md
AGENTS.md
```

## Arquitetura de uso no Windsurf

| Camada | Local | Responsabilidade |
|---|---|---|
| Contrato canônico | `agents/` | Papéis, contexto e handoff |
| Runtime Windsurf | `.windsurf/rules/` | Regras por contexto e trigger |
| Memória transversal | `AGENTS.md` | Guardrails globais do projeto |
| Especialização | `.windsurf/skills/` | Capacidades recorrentes |
| Orquestração | `.windsurf/workflows/` + slash | Sequência operacional por demanda |
| Execução oficial | `Docs/` | Plan, tasks, control e artefatos oficiais |

## Setup técnico

### 1) Preparar estrutura

```bash
cd /home/mau/molinari/Framework
mkdir -p .windsurf/rules .windsurf/skills .windsurf/workflows
```

### 2) Criar rule de qualidade

Arquivo exemplo: `.windsurf/rules/nebula-quality-rule.md`

```md
---
trigger: model_decision
description: Use when validating Quality Gate before task closure
---

# Nébula Quality Rule

Load:
- @/GUIDE.md
- @/Quality/01GUIDE.md
- @/Quality/gate.md
- @/Docs/tasks.md
- @/Docs/control.md
```

### 3) Ajustar `AGENTS.md`

1. Centralizar regras transversais e precedência.
2. Evitar duplicar regras longas que já existem em `agents/` e `Manual/15`.

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

## Prompt base canônico no Windsurf

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
3. Selecionar agente por etapa (quando aplicável).
4. Acionar workflow via slash e complementar com contexto explícito.
5. Atualizar `Docs/tasks.md` e `Docs/control.md`.
6. Aplicar Quality Gate antes do fechamento.

## Exemplos práticos

### Execução de feature

```text
Executar workflow new-feature com ScopeAgent e ExecutionAgent.
Atualizar Docs/plan.md, Docs/tasks.md e Docs/control.md.
Aplicar Quality Gate antes do fechamento.
```

### Resposta a incidente

```text
Usar RecoveryAgent com workflow hotfix.
Registrar causa, mitigação e validação em Docs/tasks.md e Docs/control.md.
```

### Alteração de integração

```text
Executar workflow new-integration com SystemAgent.
Skills: contracts, integration e curl.
Atualizar Docs/architecture.md, Docs/contract.yaml e Docs/control.md.
```

## Checklist de validação no Windsurf

1. Rule ativa com trigger correto.
2. `AGENTS.md` sem conflito com rules específicas.
3. Workflow acionado por slash command.
4. Contexto de `Docs/` explícito na chamada.
5. Evidências registradas em `Docs/tasks.md`.
6. Estado real atualizado em `Docs/control.md`.
7. Gate aprovado antes do fechamento.

## Problemas comuns e correção

### Rules sem trigger adequado

1. Revisar `trigger` por tipo de ação.
2. Separar rules por responsabilidade.

### Conflito entre `AGENTS.md` e rules

1. Deixar `AGENTS.md` com regras transversais.
2. Deixar especializações nas rules e skills.

### Fechamento sem evidência

1. Reabrir task.
2. Registrar evidências em `Docs/tasks.md`.
3. Atualizar `Docs/control.md`.
4. Reaplicar Quality Gate.

## Antipadrões críticos

1. Tratar `.windsurf/` como fonte de verdade do método.
2. Executar task sem workflow principal.
3. Omitir contexto de `Docs/`.
4. Fechar task sem Quality Gate.
5. Usar `Templates/` como saída final.

## Comandos úteis

```bash
cd /home/mau/molinari/Framework

# runtime do Windsurf
find .windsurf -maxdepth 4 -type f 2>/dev/null | sort

# contrato canônico de agentes
ls agents

# base de método e guias
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort

# artefatos oficiais de execução
ls Docs
```

## Referências

### Internas

1. `Manual/15CREATE-AGENT-BASELINE.md`
2. `Manual/10CREATE-AGENT-WINDSURF.md`
3. `agents/00README.md`
4. `agents/01GUIDE.md`
5. `agents/02CATALOG.md`
6. `NebulaWeb/content/docs/ide-windsurf.md`

### Externas

1. https://docs.windsurf.com/windsurf/cascade/memories
2. https://docs.windsurf.com/windsurf/cascade/workflows
3. https://docs.windsurf.com/windsurf/cascade/skills
4. https://docs.windsurf.com/windsurf/cascade/agents-md
