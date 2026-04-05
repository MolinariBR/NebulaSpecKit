# Quality

Índice da pasta de qualidade do framework.

## Objetivo

Definir padrões técnicos obrigatórios para garantir fidelidade de produção, reduzir falso positivo de teste e elevar previsibilidade de entrega.

## Estrutura da pasta

1. `01GUIDE.md`: regras globais, escopo e precedência do pilar.
2. `realistic-tests.md`: política de testes com ambiente próximo de produção.
3. `anti-mock.md`: regra anti-mock/stub/placeholder com exceção controlada.
4. `code-style.md`: limites de tamanho e legibilidade de código.
5. `dependencies.md`: política de versões e compatibilidade.
6. `gate.md`: gate obrigatório para fechamento de task.

## Ordem recomendada de leitura

1. `01GUIDE.md`
2. `realistic-tests.md`
3. `anti-mock.md`
4. `code-style.md` e `dependencies.md`
5. `gate.md`

## Regra operacional

1. Quality Gate é obrigatório para concluir task.
2. Evidências devem ser registradas em `Docs/tasks.md`.
3. Sem evidência, task permanece aberta.

## Relação com o Manual

1. Baseline de componentes: `Manual/18COMPONENTS-BASELINE.md`.
2. Delta do pilar de qualidade: `Manual/21COMPONENTS-QUALITY.md`.
