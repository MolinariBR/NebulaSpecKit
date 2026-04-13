# Workflows

Índice e guia oficial de uso dos workflows do framework.

## Papel deste pilar

Orquestrar a sequência de execução por tipo de mudança, com rastreabilidade e encerramento governado por Quality Gate.

## Escopo deste guia

1. Este guia define regras específicas de sequenciamento por workflow.
2. Regras globais do framework ficam em [../Guide-Started.md](../Guide-Started.md).
3. A execução operacional deve usar artefatos oficiais em `Docs/`.

## Leitura recomendada

1. [../Guide-Started.md](../Guide-Started.md)
2. [../Docs/plan.md](../Docs/plan.md)
3. [../Docs/tasks.md](../Docs/tasks.md)
4. Workflow específico da demanda

## Estrutura da pasta

1. `README.md`: regras de uso e catálogo de workflows.
2. `*.md`: um arquivo por workflow.

## Catálogo de workflows

1. [bootstrap-structure.md](bootstrap-structure.md)
2. [initial-setup.md](initial-setup.md)
3. [new-feature.md](new-feature.md)
4. [bug-fix.md](bug-fix.md)
5. [new-screen.md](new-screen.md)
6. [new-integration.md](new-integration.md)
7. [contract-change.md](contract-change.md)
8. [ui-change.md](ui-change.md)
9. [module-refactoring.md](module-refactoring.md)
10. [hotfix.md](hotfix.md)
11. [release.md](release.md)

## Regras específicas

1. Cada task deve selecionar 1 workflow principal.
2. A sequência do workflow deve ser executada sem pular etapa obrigatória.
3. Todo workflow deve iniciar com leitura dos artefatos em `Docs/` relevantes para a demanda.
4. Todo workflow deve mapear impacto e dependências antes da execução.
5. Todo workflow deve encerrar com Quality Gate aprovado, seguindo [../Quality/validation-rules.md](../Quality/validation-rules.md).
6. Em task com política `bootstrap_estrutural`, a criação de arquivos é permitida.
7. Em task com política `edição`, apenas arquivos existentes podem ser alterados.

## Regra de precedência

1. Contrato vigente em [../Docs/contract.yaml](../Docs/contract.yaml).
2. Documento-fonte do domínio em `Docs/`.
3. Planejamento e execução em [../Docs/plan.md](../Docs/plan.md) e [../Docs/tasks.md](../Docs/tasks.md).
4. Implementação atual.

## Checklist de encerramento

1. Atualizar [../Docs/control.md](../Docs/control.md).
2. Atualizar [../Docs/plan.md](../Docs/plan.md) quando houver mudança de milestone, ordem ou dependência macro.
3. Atualizar [../Docs/tasks.md](../Docs/tasks.md) com hash do commit, arquivos tocados, status do Quality Gate e evidências.

## Fechamento mínimo

1. Quality Gate aprovado em [../Quality/validation-rules.md](../Quality/validation-rules.md).
2. Atualização de [../Docs/control.md](../Docs/control.md).
3. Registro de evidências e commit em [../Docs/tasks.md](../Docs/tasks.md).
