# Execução com Agentes

Este manual cobre apenas o delta de execução com agentes.
O fluxo comum de execução está em [Execution.md](Execution.md).

## Leitura obrigatória

1. [Execution.md](Execution.md)
2. [../agents/README.md](../../agents/README.md)
3. [Baseline.md](CreateAgents/Baseline.md)

## Delta do Modo com Agentes

1. Selecionar o agente principal conforme o objetivo da task.
2. Carregar contexto base e contexto de especialidade do agente.
3. Declarar o formato de saída esperado antes da execução.
4. Quando necessário, fazer handoff para agente complementar.

## Escolha Rápida de Agente

1. Scope: descoberta e escopo.
2. Product: produto, fluxo e protótipo.
3. System: arquitetura, contrato e estrutura.
4. Execution: plan, tasks, control e implementação.
5. Quality: gate de qualidade e validação.
6. Release: entrega e estabilização.
7. Recovery: incidente e hotfix.

## Matriz de Papéis

| Agente | Chamar quando | Entrega esperada | Handoff comum |
| --- | --- | --- | --- |
| Scope | Pedido vago, descoberta inicial, definição de limite | escopo aprovado, objetivos mensuráveis, backlog inicial | Product, System, Execution |
| Product | Nova tela, mudança de UX/UI, necessidade de protótipo | user stories, páginas e fluxo claros para execução | System, Execution, Quality |
| System | Mudança de contrato, integração externa, decisão arquitetural | arquitetura/estrutura atualizadas, contrato consistente, riscos técnicos | Execution, Quality |
| Execution | Implementação, bug fix, refatoração, evolução de módulo | tasks com evidências, progresso em control, entrega rastreável | Quality, Release |
| Quality | Fechamento de task, dúvida de cobertura ou fidelidade | decisão de gate, evidências, bloqueios objetivos | Execution, Release |
| Release | Escopo aprovado no gate e pronto para deploy/release | release com checklist, monitoramento e rollback validado | Recovery, Execution |
| Recovery | Incidente em produção, hotfix emergencial | correção validada, estabilização, causa raiz e prevenção | Quality, Release |

## Regra de Handoff Entre Agentes

Todo handoff deve registrar:

1. O que foi concluído.
2. O que ficou pendente.
3. Qual agente deve assumir.
4. Quais arquivos devem ser carregados no próximo ciclo.

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
