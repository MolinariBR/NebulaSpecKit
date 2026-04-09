# Guia de Workflows

Guia oficial de uso dos workflows por tipo de demanda.

## Escopo deste guia

1. Este guia define regras específicas de sequenciamento por workflow.
2. Regras globais do framework ficam em [../GUIDE.md](../GUIDE.md).
3. Baseline operacional de execução fica em [../Manual/17EXECUTION-BASELINE.md](../Manual/17EXECUTION-BASELINE.md).

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
