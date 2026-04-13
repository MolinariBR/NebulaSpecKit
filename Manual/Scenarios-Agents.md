# Cenários com Agentes

Este manual cobre apenas o delta de execução com agentes.
O fluxo comum de cenários está em [Scenarios-Base.md](Scenarios-Base.md).

## Leitura Obrigatória

1. [Scenarios-Base.md](Scenarios-Base.md)
2. [Agents.md](Agents.md)
3. [Baseline.md](CreateAgents/Baseline.md)

## Delta Com Agentes

1. Toda etapa do cenário deve ter dono explícito por agente.
2. Cada handoff deve registrar entrada, saída e risco residual.
3. O Quality valida fechamento em todos os cenários.
4. O contexto de execução deve ser sempre em Docs:
- Docs/plan.md
- Docs/tasks.md
- Docs/control.md

## Mapeamento Rápido de Cenários

1. Nova feature com API e UI
- Scope -> Product -> System -> Execution -> Quality

2. Bug crítico em produção
- Recovery -> Quality
- Release opcional para rollout controlado

3. Release planejada
- Release -> Quality

4. Refatoração de módulo
- Execution -> Quality

## Prompt Inicial Canônico

```text
Use o agente: <AgentName>
Objetivo: <objetivo da task>
Workflow: Workflows/<workflow>.md

Carregue contexto base:
- Guide-Started.md
- Skills/README.md
- Workflows/README.md
- Quality/README.md
- Templates/Full/README.md

Carregue contexto especializado conforme agents/<role>.md.
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
