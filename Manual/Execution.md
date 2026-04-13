# Execution Baseline

Este manual define o fluxo comum de execução do Framework Nébula para qualquer modo de trabalho.

Use este documento como base obrigatória antes de:
- [Agents.md](Agents.md)
- [NoAgents.md](NoAgents.md)

## Regra de Ouro

1. Templates em `Templates/` são modelo.
2. Artefatos oficiais do projeto são editados em `Docs/`.
3. Protótipos HTML ficam em `Docs/Prototype/`.

## Sequência comum de execução

1. Definir objetivo, escopo e restrições da task.
2. Selecionar 1 workflow principal em `Workflows/`.
3. Definir skills de suporte técnico em `Skills/`.
4. Editar os artefatos oficiais de `Docs/` da demanda.
5. Executar o trabalho técnico (com ou sem agente).
6. Aplicar Quality Gate e registrar evidências.
7. Encerrar a task com rastreabilidade em `Docs/control.md`.

## Artefatos mínimos por task

1. [../Docs/plan.md](../Docs/plan.md)
2. [../Docs/tasks.md](../Docs/tasks.md)
3. [../Docs/control.md](../Docs/control.md)

## Governança obrigatória

1. Bootstrap estrutural apenas na primeira task.
2. Após bootstrap, apenas edição de arquivos existentes.
3. Exatamente 1 commit por task concluída.
4. Quality Gate obrigatório antes de fechar task.

## Evidências mínimas de fechamento

1. Docs oficiais atualizados.
2. Quality Gate aprovado.
3. Hash do commit da task.
4. Riscos e pendências registrados.

## Checklist baseline

1. Workflow principal definido.
2. Skills de suporte definidos.
3. Docs da demanda editados.
4. Gate de qualidade aprovado.
5. Commit e control atualizados.

## Referências

1. [../Guide-Started.md](../Guide-Started.md)
2. [../Docs/README.md](../Docs/README.md)
3. [../Workflows/README.md](../Workflows/README.md)
4. [../Quality/validation-rules.md](../Quality/validation-rules.md)
