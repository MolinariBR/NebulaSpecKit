# Execução com Agentes

Este manual cobre apenas o delta de execução com agentes.
O fluxo comum de execução está em [17EXECUTION-BASELINE.md](17EXECUTION-BASELINE.md).

## Leitura obrigatória

1. [17EXECUTION-BASELINE.md](17EXECUTION-BASELINE.md)
2. [../agents/00README.md](../agents/00README.md)
3. [../agents/02CATALOG.md](../agents/02CATALOG.md)

## Delta do Modo com Agentes

1. Selecionar o agente principal conforme o objetivo da task.
2. Carregar contexto base e contexto de especialidade do agente.
3. Declarar o formato de saída esperado antes da execução.
4. Quando necessário, fazer handoff para agente complementar.

## Escolha Rápida de Agente

1. ScopeAgent: descoberta e escopo.
2. ProductAgent: produto, fluxo e protótipo.
3. SystemAgent: arquitetura, contrato e estrutura.
4. ExecutionAgent: plan, tasks, control e implementação.
5. QualityAgent: gate de qualidade e validação.
6. ReleaseAgent: entrega e estabilização.
7. RecoveryAgent: incidente e hotfix.

## Prompt Mínimo

```text
Use o agente: <AgentName>
Objetivo: <objetivo>
Workflow: Workflows/<workflow>.md
Contexto de execução: Docs/plan.md, Docs/tasks.md, Docs/control.md
Saída: plano, execução, evidências, riscos e pendências
```

## Checklist Específico do Modo com Agentes

1. Agente principal correto para a demanda.
2. Contexto base e contexto especializado carregados.
3. Handoff definido quando houver dependência entre papéis.
4. Saída da task registrada em Docs/tasks.md e Docs/control.md, quando aplicável.
