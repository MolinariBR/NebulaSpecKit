# Metrics

## Objetivo

Definir thresholds objetivos de qualidade estrutural para apoiar:

1. implementacao;
2. revisao;
3. quality gate;
4. controle de risco de manutencao.

Este arquivo define os thresholds e sinais de risco estrutural usados em implementacao, revisao e gate.

## Regra de ownership

Todos os thresholds numericos devem existir apenas aqui.
Outros arquivos devem referenciar `metrics.md`, sem duplicar tabelas.

## Bandas de interpretacao

1. Ideal: faixa recomendada.
2. Toleravel: aceitavel com observacao.
3. Maximo: limite operacional; exige justificativa.
4. Critico: risco estrutural alto; exige acao imediata.

## Principios de avaliacao

1. Metricas sao sinais operacionais, nao dogma.
2. Coesao semantica vale mais que reducao cega de tamanho.
3. Acumulo de alertas aumenta risco estrutural.
4. Faixa critica exige acao, contencao ou excecao explicita.
5. Excecao sem nome e rastreabilidade e invalida.

## Metricas nucleares

| Metrica                           | Ideal                      | Toleravel | Maximo  | Critico |
|-----------------------------------|----------------------------|-----------|---------|---------|
| Linhas por arquivo                | <=150                      | 151-250   | 251-400 |    >400 |
| Caracteres por linha              | <=88                       | 89-100    | 101-120 |    >120 |
| Imports por arquivo               | 3-12                       | 13-20     | 21-30   |     >30 |
| Estruturas primarias por arquivo  | 1                          | 2         | 3       |     >=4 |
| Funcoes por arquivo               | 1-7                        | 8-12      | 13-20   |     >20 |
| Exports por arquivo               | 1 principal + 2 secundarios| <=5       | 6-8     |      >8 |
| Linhas por funcao                 | 5-20                       | 21-35     | 36-50   |     >50 |
| Parametros por funcao             | 0-2                        | 3         | 4       |     >=5 |
| Profundidade de nesting           | 0-2                        | 3         | 4       |     >=5 |
| Branches por funcao               | <=3                        | 4-5       | 6-8     |      >8 |
| Linhas por classe                 | <=120                      | 121-200   | 201-300 |    >300 |
| Metodos por classe                | 1-7                        | 8-12      | 13-20   |     >20 |
| Propriedades por classe           | <=5                        | 6-8       | 9-12    |     >12 |
| Metodos publicos por classe       | 1-5                        | 6-8       | 9-12    |     >12 |

## Metricas de risco semantico

### Contrato de retorno

1. Ideal: forma de retorno estavel e previsivel.
2. Toleravel: pequena variacao controlada por tipo/estado explicito.
3. Maximo: variacao frequente, mas documentada.
4. Critico: retorno inconsistente e nao modelado.

### Side effects ocultos

1. Ideal: side effects explicitos e esperados.
2. Toleravel: side effect identificado, mas com visibilidade parcial.
3. Maximo: multiplos side effects descobriveis apenas por leitura profunda.
4. Critico: side effect oculto em unidade aparentemente pura.

### Mistura de camadas

1. Ideal: sem mistura de dominio/aplicacao/infra.
2. Toleravel: acoplamento pontual e justificavel.
3. Maximo: mistura recorrente em modulo sensivel.
4. Critico: violacao estrutural com impacto de manutencao.

### Densidade de responsabilidade por funcao

1. Ideal: uma responsabilidade clara.
2. Toleravel: uma principal com suporte estritamente relacionado.
3. Maximo: duas responsabilidades visiveis.
4. Critico: tres ou mais responsabilidades no mesmo corpo.

## Metricas de legibilidade

### Densidade de comentarios

1. Ideal: comentarios pontuais para contexto nao-obvio.
2. Toleravel: comentarios adicionais sem mascarar problema de design.
3. Maximo: comentario excessivo para explicar codigo confuso.
4. Critico: dependencia de comentario para entender fluxo basico.

### Scanabilidade

Um arquivo e scanavel quando o revisor encontra rapido:

1. imports;
2. contratos;
3. fluxo principal;
4. side effects;
5. exports.

## Modelo de risco composto

Classificacao sugerida:

1. Healthy:
- sem metrica critica;
- no maximo 2 metricas em toleravel.

2. Attention:
- maximo 1 metrica em maximo;
- varias em toleravel.

3. Limit:
- 2 ou mais metricas em maximo;
- risco crescente de quebra de coesao.

4. Critical:
- qualquer metrica em critico sem justificativa;
- ou combinacao de maximo + side effects ocultos + mistura de camadas.

## Padroes compostos de alerta

1. Arquivo amplo demais: linhas altas + imports altos + exports altos.
2. Fluxo dificil de manter: funcao longa + nesting alto + branches altos.
3. Decaimento de fronteira: mistura de camadas + side effect oculto.

## Excecoes permitidas

Aceitaveis quando justificadas:

1. codigo gerado;
2. migrations;
3. snapshots;
4. schemas gerados;
5. mapas estaticos declarativos;
6. compatibility shim;
7. contencao temporaria de legado em refatoracao controlada.

Mesmo em excecao, manter:

1. identificacao clara;
2. naming coerente;
3. escopo contido;
4. rastreabilidade na task.

## Enforcement recomendado

1. Advisory:
- melhorias em faixa ideal e scanabilidade.

2. Warning:
- repeticao de toleravel;
- entrada em maximo.

3. Blocking:
- qualquer critico sem justificativa;
- side effect oculto em contexto sensivel;
- mistura de camadas em modulo critico.

## Integracao operacional

1. `validation-rules.md` usa maximo/critico como criterio de bloqueio tecnico.
2. `review-checklist.md` usa `metrics.md` como tabela unica de referencia.
3. `execution-policy.md` referencia estas bandas para decidir split/refactor/justificativa.

Uso por perfil:

1. Dev: detectar drift cedo e corrigir antes do review.
2. Reviewer: justificar feedback por threshold e risco composto.
3. AI agent: gerar/refatorar mirando ideal-toleravel e evitar maximo sem justificativa.
4. Gate/arquitetura: bloquear critico recorrente e monitorar reincidencia por modulo.

## Regra final

Metrica so e valida quando protege clareza, coesao, previsibilidade de contrato e fronteira arquitetural.

