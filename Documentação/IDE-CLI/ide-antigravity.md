# ide-antigravity

Guia operacional para configurar e executar o Nébula no Antigravity com Rules, Skills e Workflows, mantendo rastreabilidade e governança por task.

## Objetivo

Padronizar o uso do Antigravity como runtime sem quebrar o contrato canônico de agentes do framework.

## Escopo

1. Delta nativo do Antigravity.
2. Estrutura física recomendada do runtime.
3. Contexto obrigatório para execução.
4. Fluxo de operação com validação de fechamento.

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
- `Manual/09CREATE-AGENT-ANTIGRAVITY.md`

### Documento web atual

- `NebulaWeb/content/docs/ide-antigravity.md`

## Regra de ouro

1. `agents/` é a fonte de verdade dos papéis.
2. Antigravity é adaptador de runtime.
3. Em conflito, prevalece o contrato canônico do framework.

> [!IMPORTANT]
> Não existe um arquivo nativo único de agente no Antigravity; a composição é feita por Rules, Skills e Workflows.

## Invariantes de governança

1. `Docs/` é saída oficial do projeto.
2. `Templates/` é modelo, nunca entrega final.
3. `Prototype/` é exclusivo para protótipos HTML.
4. Primeira task: `bootstrap_estrutural`.
5. Após bootstrap: apenas edição de arquivos existentes.
6. Exatamente 1 commit por task concluída.
7. Task só fecha com Quality Gate aprovado.

## Delta nativo do Antigravity

### Componentes de runtime

1. Rules em `.agents/rules/`.
2. Skills em `.agents/skills/<nome>/SKILL.md`.
3. Workflows acionados por slash command (`/workflow-name`).
4. Uso de `@mentions` para carregar contexto canônico.

### Estrutura recomendada

```text
.agents/
  rules/
    nebula-governance.md
    nebula-quality.md
  skills/
    execution/
      SKILL.md
    quality/
      SKILL.md
```

## Arquitetura de uso no Antigravity

| Camada | Local | Responsabilidade |
|---|---|---|
| Contrato canônico | `agents/` | Papéis, contexto e handoff |
| Runtime Antigravity | `.agents/rules/` | Guardrails e regras transversais |
| Especialização | `.agents/skills/` | Capacidades por domínio recorrente |
| Orquestração | Slash workflows | Sequência de execução por demanda |
| Execução oficial | `Docs/` | Plan, tasks, control e artefatos oficiais |

## Setup técnico

### 1) Preparar estrutura

```bash
cd /home/mau/molinari/Framework
mkdir -p .agents/rules .agents/skills
```

### 2) Criar rule de governança

Arquivo exemplo: `.agents/rules/nebula-governance.md`

```md
# Nébula Governance Rule

Aplicar:
- bootstrap na primeira task
- modo edição após bootstrap
- 1 commit por task
- Quality Gate obrigatório

Carregar:
- @/GUIDE.md
- @/Workflows/01GUIDE.md
- @/Quality/01GUIDE.md
- @/Docs/plan.md
- @/Docs/tasks.md
- @/Docs/control.md
```

### 3) Criar skills de apoio (quando necessário)

1. Criar skill reutilizável por domínio recorrente.
2. Priorizar skills que acelerem operação sem duplicar regra canônica.

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

## Prompt base canônico no Antigravity

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

1. Selecionar modo: com agentes ou sem agentes.
2. Selecionar 1 workflow principal da demanda.
3. Definir agente responsável por etapa (quando aplicável).
4. Acionar workflow por slash e complementar com contexto explícito.
5. Atualizar `Docs/tasks.md` e `Docs/control.md`.
6. Aplicar Quality Gate antes de fechar.

## Exemplos práticos

### Execução com agente

```text
Executar workflow new-screen com ProductAgent.
Usar skills: ui-ux e flow.
Atualizar Docs/pages.md, Docs/flow.md, Docs/tasks.md e Docs/control.md.
```

### Validação de qualidade

```text
Acionar QualityAgent para validar Quality Gate da TASK-042.
Exigir evidências em Docs/tasks.md e atualização de status em Docs/control.md.
```

### Integração técnica

```text
Executar workflow new-integration com SystemAgent.
Skills: contracts, integration e curl.
Atualizar Docs/architecture.md, Docs/contract.yaml e Docs/control.md.
```

## Checklist de validação no Antigravity

1. Rule correta está ativa no workspace.
2. Skill carregou com estrutura válida.
3. Workflow foi acionado explicitamente.
4. Contexto de `Docs/` foi carregado.
5. Evidências foram registradas em `Docs/tasks.md`.
6. Estado real foi atualizado em `Docs/control.md`.
7. Gate aprovado antes do fechamento.

## Problemas comuns e correção

### Rules sem foco

1. Separar rules por responsabilidade.
2. Deixar regras transversais em um arquivo próprio.

### Skill sem contexto suficiente

1. Declarar fontes em `Docs/`.
2. Associar skill ao workflow principal da demanda.

### Fechamento sem rastreabilidade

1. Reabrir task.
2. Registrar evidências em `Docs/tasks.md`.
3. Atualizar `Docs/control.md`.
4. Submeter novamente ao Quality Gate.

## Antipadrões críticos

1. Tratar runtime do Antigravity como fonte de verdade do método.
2. Executar task sem workflow principal.
3. Omitir contexto de `Docs/` na chamada.
4. Fechar task sem Quality Gate.
5. Usar `Templates/` como saída final.

## Comandos úteis

```bash
cd /home/mau/molinari/Framework

# listar runtime do Antigravity
find .agents -maxdepth 3 -type f 2>/dev/null | sort

# revisar contrato canônico de agentes
ls agents

# revisar base de método
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort

# revisar artefatos oficiais de execução
ls Docs
```

## Referências

### Internas

1. `Manual/15CREATE-AGENT-BASELINE.md`
2. `Manual/09CREATE-AGENT-ANTIGRAVITY.md`
3. `agents/00README.md`
4. `agents/01GUIDE.md`
5. `agents/02CATALOG.md`
6. `NebulaWeb/content/docs/ide-antigravity.md`

### Externas

1. https://antigravity.google/docs/rules-workflows
2. https://antigravity.google/docs/skills
3. https://antigravity.google/docs/agent-modes-settings
