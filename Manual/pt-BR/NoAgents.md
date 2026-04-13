# Execução sem Agentes

Este manual cobre apenas o delta de execução sem agentes.
O fluxo comum de execução está em [Execution.md](Execution.md).

## Leitura obrigatória

1. [Execution.md](Execution.md)
2. [../Templates/Full/README.md](../../Templates/Full/README.md)
3. [../Workflows/README.md](../../Workflows/README.md)

## Delta do Modo sem Agentes

1. O papel de orquestração é do responsável técnico humano.
2. A atribuição de etapas é feita manualmente por membros do time.
3. O controle de handoff é explicitado em `Docs/control.md`.
4. Revisões de qualidade são conduzidas pelo time antes do fechamento.

## Operação Mínima Recomendada

1. Escolher 1 workflow principal em `Workflows/`.
2. Selecionar templates Full ou Quick conforme profundidade.
3. Editar os artefatos oficiais em `Docs/`.
4. Validar com [../Quality/validation-rules.md](../../Quality/validation-rules.md).
5. Registrar evidências e commit da task em `Docs/tasks.md` e `Docs/control.md`.

## Checklist Específico do Modo sem Agentes

1. Responsável técnico da task definido.
2. Workflow principal definido e seguido.
3. Docs editados com rastreabilidade de mudança.
4. Validação de qualidade aprovada antes do fechamento.
5. Commit único da task registrado em Docs/control.md.
