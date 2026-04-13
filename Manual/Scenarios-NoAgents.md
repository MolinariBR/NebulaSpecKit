# Cenários sem Agentes

Este manual cobre apenas o delta de execução sem agentes.
O fluxo comum de cenários está em [Scenarios-Base.md](Scenarios-Base.md).

## Leitura Obrigatória

1. [Scenarios-Base.md](Scenarios-Base.md)
2. [NoAgents.md](NoAgents.md)
3. [../Workflows/README.md](../Workflows/README.md)

## Delta sem Agentes

1. O time humano assume explicitamente os papéis de escopo, produto, sistema, execução e qualidade.
2. Cada passo deve referenciar pelo menos um workflow e as skills relevantes.
3. O contexto de execução deve ser sempre em Docs:
- Docs/plan.md
- Docs/tasks.md
- Docs/control.md

## Mapeamento Rápido de Cenários

1. Novo produto interno
- Workflows/initial-setup.md
- Workflows/new-screen.md

2. Integração externa
- Workflows/new-integration.md

3. Mudança de UI
- Workflows/ui-change.md

4. Hotfix urgente
- Workflows/hotfix.md

## Checklist Manual Por Task

1. Objetivo da task definido.
2. Workflow selecionado e seguido.
3. Skills consultadas e registradas.
4. Arquivos oficiais de Docs atualizados.
5. Evidências do Quality Gate anexadas.
6. Hash do commit registrado.
7. Riscos e pendências atualizados no control.
