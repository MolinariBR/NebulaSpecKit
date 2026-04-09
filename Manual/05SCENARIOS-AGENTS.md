# Cenários com Agentes

Este manual cobre apenas o delta de execução com agentes.
O fluxo comum de cenários está em [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md).

## Leitura Obrigatória

1. [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md)
2. [02AGENTS.md](02AGENTS.md)
3. [../agents/02CATALOG.md](../agents/02CATALOG.md)

## Delta Com Agentes

1. Toda etapa do cenário deve ter dono explícito por agente.
2. Cada handoff deve registrar entrada, saída e risco residual.
3. O QualityAgent valida fechamento em todos os cenários.
4. O contexto de execução deve ser sempre em Docs:
- Docs/plan.md
- Docs/tasks.md
- Docs/control.md

## Mapeamento Rápido de Cenários

1. Nova feature com API e UI
- ScopeAgent -> ProductAgent -> SystemAgent -> ExecutionAgent -> QualityAgent

2. Bug crítico em produção
- RecoveryAgent -> QualityAgent
- ReleaseAgent opcional para rollout controlado

3. Release planejada
- ReleaseAgent -> QualityAgent

4. Refatoração de módulo
- ExecutionAgent -> QualityAgent

## Prompt Inicial Canônico

```text
Use o agente: <AgentName>
Objetivo: <objetivo da task>
Workflow: Workflows/<workflow>.md

Carregue contexto base:
- GUIDE.md
- Skills/README.md
- Workflows/README.md
- Quality/README.md
- Templates/Full/README.md

Carregue contexto especializado conforme agents/<role>-agent.md.
Carregue contexto de execução em Docs/plan.md, Docs/tasks.md e Docs/control.md.

Aplique governança:
- bootstrap apenas na primeira task
- edit-only após bootstrap
- 1 commit por task
- Quality Gate obrigatório
```

## Checklist de Encerramento do Delta

1. Agente correto foi usado em cada etapa.
2. Handoff entre agentes ficou registrado.
3. Quality Gate foi aprovado antes do fechamento.
4. Commit por task foi registrado no control.
