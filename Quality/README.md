# Quality

Indice oficial do pilar de qualidade.

## Objetivo

Definir e aplicar regras de implementacao, estrutura, revisao, validacao e fechamento de task com evidencias.

## Arquivos oficiais

1. `execution-policy.md`: fluxo de implementacao com controle de escopo.
2. `structure-rules.md`: anatomia e regras estruturais de arquivo/modulo.
3. `clean-rules.md`: regras comportamentais de escrita de codigo.
4. `metrics.md`: thresholds, bandas e risco composto.
5. `review-checklist.md`: checklist de revisao tecnica.
6. `realistic-tests.md`: regras de testes com fidelidade de producao.
7. `anti-mock.md`: regra anti-mock com excecao controlada.
8. `dependencies.md`: compatibilidade e lockfile.
9. `validation-rules.md`: gate obrigatorio para fechamento de task.

## Ordem recomendada de leitura

1. `README.md`
2. `execution-policy.md`
3. `structure-rules.md`
4. `clean-rules.md`
5. `metrics.md`
6. `review-checklist.md`
7. `realistic-tests.md`
8. `anti-mock.md`
9. `dependencies.md`
10. `validation-rules.md`

## Regra operacional

1. Nenhuma task fecha sem `validation-rules.md` aprovado.
2. Evidencias devem ser registradas em `Docs/tasks.md`.
3. Sem evidencia, task permanece aberta.

## Relacao com o Manual

1. Baseline: `Manual/18COMPONENTS-BASELINE.md`.
2. Delta de qualidade: `Manual/21COMPONENTS-QUALITY.md`.
