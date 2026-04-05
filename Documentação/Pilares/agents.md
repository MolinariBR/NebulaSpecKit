# Agents

Guia operacional consolidado de agentes do Nébula Framework.

## Objetivo

Este documento define como selecionar, chamar e operar agentes de forma rastreável, evitando sobreposição de responsabilidades e mantendo governança de execução.

## Proposta do pilar

Agentes respondem **quem conduz cada tipo de decisão e entrega** no ciclo do projeto.

Eles não substituem:

1. Workflow (sequência de execução)
2. Skills (especialidade técnica)
3. Quality Gate (decisão de fechamento)
4. Artefatos em `Docs/` (fonte de verdade)

> [!IMPORTANT]
> `agents/` é a fonte canônica dos papéis. Configurações por IDE/CLI são adaptadores de runtime e não redefinem o contrato dos agentes.

## Fontes analisadas

### Núcleo do framework

- `README.md`
- `GUIDE.md`
- `Docs/README.md`

### Guides e readmes do framework

- `Manual/00README.md`, `Manual/01GUIDE.md`
- `Skills/00README.md`, `Skills/01GUIDE.md`
- `Workflows/00README.md`, `Workflows/01GUIDE.md`
- `Quality/00README.md`, `Quality/01GUIDE.md`
- `Templates/Full/00README.md`, `Templates/Full/01GUIDE.md`
- `Templates/Quick/00README.md`, `Templates/Quick/01GUIDE.md`
- `agents/00README.md`, `agents/01GUIDE.md`
- `agents/behavior/00README.md`, `agents/behavior/01GUIDE.md`
- `Prototype/00README.md`, `Prototype/01GUIDE.md`
- `NebulaWeb/README.md`

### Documentação de agents

- `agents/02CATALOG.md`
- `agents/scope-agent.md`
- `agents/product-agent.md`
- `agents/system-agent.md`
- `agents/execution-agent.md`
- `agents/quality-agent.md`
- `agents/release-agent.md`
- `agents/recovery-agent.md`

### Documento web atual

- `NebulaWeb/content/docs/agents.md`

## Regras canônicas de execução com agentes

1. Selecionar 1 agente principal por ciclo.
2. Carregar contexto base antes do contexto de especialidade.
3. Em execução de task, carregar também `Docs/plan.md`, `Docs/tasks.md` e `Docs/control.md`.
4. Aplicar governança: bootstrap apenas na primeira task, edit-only nas seguintes.
5. Garantir exatamente 1 commit por task concluída.
6. Exigir Quality Gate aprovado para fechar task.
7. Registrar handoff explícito quando houver troca de agente.

> [!WARNING]
> Troca de agente sem handoff formal quebra rastreabilidade e aumenta risco de retrabalho.

## Matriz de roteamento rápido

| Agente | Quando chamar |
|---|---|
| `ScopeAgent` | Pedido vago, necessidade de definir escopo e objetivos |
| `ProductAgent` | Nova tela, alteração de fluxo ou refinamento de UX |
| `SystemAgent` | Mudança de contrato, arquitetura ou integração |
| `ExecutionAgent` | Implementação, bugfix, refatoração e condução por task |
| `QualityAgent` | Validação de fechamento e decisão de gate |
| `ReleaseAgent` | Deploy, rollout e estabilização pós-entrega |
| `RecoveryAgent` | Incidente crítico e hotfix emergencial |

## Contexto obrigatório em toda chamada

### Contexto base

```text
- GUIDE.md
- Skills/01GUIDE.md
- Workflows/01GUIDE.md
- Quality/01GUIDE.md
- Templates/Full/01GUIDE.md
```

### Contexto de execução (quando houver task)

```text
- Docs/plan.md
- Docs/tasks.md
- Docs/control.md
```

> [!NOTE]
> O contexto de especialidade vem do arquivo `agents/<role>-agent.md` do papel escolhido.

## Catálogo consolidado dos 7 agentes

### ScopeAgent

**Função:** definir problema, escopo e objetivos mensuráveis antes da implementação.

**Especialidade:** discovery, framing e alinhamento de limites.

**Contexto de especialidade:**

```text
- Skills/user-stories.md
- Workflows/initial-setup.md
- Templates/Full/brief.md
```

**Entregas esperadas:** escopo aprovado, objetivos mensuráveis e backlog inicial priorizado.

**Handoff comum:** `ProductAgent`, `SystemAgent`, `ExecutionAgent`.

### ProductAgent

**Função:** transformar necessidades de negócio em fluxo, telas e experiência validável.

**Especialidade:** UX, fluxo funcional e especificação de interface.

**Contexto de especialidade:**

```text
- Skills/ui-ux.md
- Skills/flow.md
- Workflows/new-screen.md
- Templates/Full/pages.md
- Templates/Full/flow.md
```

**Entregas esperadas:** user stories refinadas, páginas/fluxos claros e impactos visuais documentados.

**Handoff comum:** `SystemAgent`, `ExecutionAgent`, `QualityAgent`.

### SystemAgent

**Função:** modelar arquitetura, entidades, contratos e integrações com consistência técnica.

**Especialidade:** modelagem de sistema, fronteiras e contrato.

**Contexto de especialidade:**

```text
- Skills/contracts.md
- Skills/integration.md
- Workflows/contract-change.md
- Templates/Full/contract.yaml
- Templates/Full/architecture.md
```

**Entregas esperadas:** arquitetura atualizada, contrato versionado e riscos técnicos mapeados.

**Handoff comum:** `ExecutionAgent`, `QualityAgent`.

### ExecutionAgent

**Função:** conduzir planejamento e execução por task com rastreabilidade.

**Especialidade:** implementação, refatoração, plano, tasks e controle.

**Contexto de especialidade:**

```text
- Skills/implementation.md
- Skills/refactoring.md
- Workflows/new-feature.md
- Workflows/bug-fix.md
- Templates/Full/plan.md
- Templates/Full/tasks.md
- Templates/Full/control.md
```

**Entregas esperadas:** progresso real em `Docs/tasks.md`, `Docs/control.md` e artefatos técnicos atualizados.

**Handoff comum:** `QualityAgent`, `ReleaseAgent`.

### QualityAgent

**Função:** aprovar ou reprovar fechamento de task com evidências objetivas.

**Especialidade:** testes realistas, anti-mock, verificação de padrão e dependências.

**Contexto de especialidade:**

```text
- Skills/tests.md
- Skills/scripts.md
- Skills/curl.md
- Quality/gate.md
- Quality/realistic-tests.md
- Quality/anti-mock.md
```

**Entregas esperadas:** decisão formal de gate, evidências técnicas e bloqueios quando reprovado.

**Handoff comum:** `ExecutionAgent`, `ReleaseAgent`.

> [!IMPORTANT]
> Nenhuma task deve ser encerrada sem decisão formal do `QualityAgent` no gate.

### ReleaseAgent

**Função:** conduzir deploy e release com checklist, observabilidade e rollback.

**Especialidade:** rollout, monitoramento e estabilização pós-entrega.

**Contexto de especialidade:**

```text
- Skills/deploy.md
- Skills/logs.md
- Workflows/release.md
- Templates/Full/deploy.md
- Templates/Full/control.md
```

**Entregas esperadas:** release executado, evidências de monitoramento e rollback pronto.

**Handoff comum:** `RecoveryAgent`, `ExecutionAgent`.

### RecoveryAgent

**Função:** responder incidentes e executar hotfix com segurança e rastreabilidade.

**Especialidade:** contenção, causa raiz e estabilização.

**Contexto de especialidade:**

```text
- Skills/logs.md
- Skills/tests.md
- Workflows/hotfix.md
- Workflows/bug-fix.md
- Templates/Full/tasks.md
- Templates/Full/control.md
```

**Entregas esperadas:** correção aplicada, estabilização validada e ações preventivas registradas.

**Handoff comum:** `QualityAgent`, `ReleaseAgent`.

## Prompt padrão de chamada

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
Carregue contexto de execução: Docs/plan.md, Docs/tasks.md, Docs/control.md.

Aplique governança:
- bootstrap apenas na primeira task
- edit-only após bootstrap
- 1 commit por task
- Quality Gate obrigatório

Entregue:
1) plano
2) execução
3) evidências
4) riscos e pendências
```

## Protocolo de handoff entre agentes

Todo handoff deve registrar:

1. O que foi concluído no ciclo
2. O que ficou pendente
3. Próximo agente responsável
4. Arquivos mínimos que o próximo agente deve carregar

## Contrato mínimo de um agente

Todo `agents/<role>-agent.md` deve incluir frontmatter YAML com:

```yaml
---
name: <role>-agent
agent_name: <RoleName>Agent
description: "Use when: <critério de escolha em uma linha>"
function: "<responsabilidade principal>"
specialty: "<domínio de especialidade>"
skills:
  - Skills/<skill>.md
workflows:
  - Workflows/<workflow>.md
templates:
  - Templates/Full/<template>.md
quality:
  - Quality/gate.md
context_base:
  - GUIDE.md
  - Skills/01GUIDE.md
  - Workflows/01GUIDE.md
  - Quality/01GUIDE.md
  - Templates/Full/01GUIDE.md
context_specialty:
  - <arquivos específicos do papel>
context_execution:
  - Docs/plan.md
  - Docs/tasks.md
  - Docs/control.md
governance_rules:
  - Bootstrap estrutural na primeira task
  - Apenas edição de arquivos existentes nas tarefas seguintes
  - 1 commit por task
  - Quality Gate obrigatório
---
```

## Antipadrões

1. Chamar agente sem contexto base completo.
2. Trocar de agente sem handoff formal.
3. Fechar task sem gate aprovado.
4. Criar novo papel sem justificar diferença real de responsabilidade.
5. Duplicar regras canônicas de `agents/` dentro de runtime por ferramenta.

> [!CAUTION]
> Se dois agentes disputam a mesma responsabilidade, o contrato está mal definido e precisa ser corrigido antes da execução.

## Comandos úteis

```bash
cd /home/mau/molinari/Framework

# listar documentação de agentes
ls agents

# revisar papéis e catálogos
rg --files agents -g '*.md' | sort

# revisar guias/readmes usados como base
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort
```

## Encerramento

Resumo operacional: workflow define a sequência, skill aprofunda a execução, agente define responsabilidade e handoff, quality decide o fechamento, e `Docs/` mantém o histórico auditável.
