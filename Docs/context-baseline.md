# Context Baseline

## Objetivo

Registrar baseline de contexto carregado no Nébula para medir impacto de
refatorações em linhas e tokens estimados.

## Data da medição

- `2026-04-09`

## Método

1. Métricas usadas:
   - linhas
   - caracteres
   - palavras
2. Estimativa de tokens:
   - `est_tokens_char4`: `caracteres / 4`
   - `est_tokens_word13`: `palavras * 1.3`
3. Observação:
   - `tiktoken` não estava disponível no ambiente local na medição.
   - os valores de token são estimativas operacionais para comparação relativa.

## Escopos medidos

1. `BASE_ANTIGA`:
   - `instructions.md`
   - `GUIDE.md`
   - `Workflows/README.md`
   - `Skills/README.md`
   - `Quality/validation-rules.md`
2. `BASE_NOVA`:
   - `BASE_ANTIGA` + `Docs/commands.md`
3. `QUALITY_STACK`:
   - `Quality/execution-policy.md`
   - `Quality/structure-rules.md`
   - `Quality/clean-rules.md`
   - `Quality/metrics.md`
   - `Quality/review-checklist.md`
   - `Quality/realistic-tests.md`
   - `Quality/anti-mock.md`
   - `Quality/dependencies.md`
4. `BASE_NOVA+QUALITY_STACK`:
   - união dos dois escopos anteriores.

## Resultado

| Escopo | Arquivos | Linhas | Caracteres | Palavras | est_tokens_char4 | est_tokens_word13 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| BASE_ANTIGA | 5 | 767 | 28451 | 3414 | 7113 | 4438 |
| BASE_NOVA | 6 | 818 | 31052 | 3747 | 7763 | 4871 |
| QUALITY_STACK | 8 | 1119 | 35923 | 5044 | 8981 | 6557 |
| BASE_NOVA+QUALITY_STACK | 14 | 1937 | 66975 | 8791 | 16744 | 11428 |

## Leitura rápida

1. `Docs/commands.md` adicionou +51 linhas na base canônica.
2. O custo maior de contexto continua em `QUALITY_STACK`.
3. O baseline atual para execução completa (`BASE_NOVA+QUALITY_STACK`) é de:
   - 1937 linhas
   - 66.975 caracteres
   - token estimado entre 11.428 e 16.744 (faixa heurística)

## Próxima medição

Repetir após cada lote de refatoração relevante e comparar contra este baseline.
