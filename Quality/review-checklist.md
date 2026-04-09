# Review Checklist

## Objetivo

Padronizar revisao tecnica de mudancas de codigo com foco em:

1. risco estrutural;
2. previsibilidade de contrato;
3. legibilidade;
4. seguranca de evolucao.

Este checklist nao substitui o `validation-rules.md`.
Ele e checklist de revisao; `validation-rules.md` e checklist de fechamento de task.

## Quando usar

Usar em:

1. code review de PR;
2. revisao pre-merge;
3. revisao de output de IA;
4. revisao de refatoracao;
5. revisao de mudanca de contrato.

## Entradas obrigatorias

1. diff da mudanca;
2. contexto da task em `Docs/tasks.md`;
3. `execution-policy.md`;
4. `metrics.md`.

## Regra de ownership

1. criterios de revisao vivem aqui;
2. thresholds numericos vivem em `metrics.md`;
3. validacao operacional de fechamento vive em `validation-rules.md`.

## Checklist de revisao

Marcar cada item como:

1. OK
2. Attention
3. Limit
4. Critical
5. N/A

### 1) Identidade e responsabilidade

1. O arquivo tem centro de responsabilidade claro.
2. O nome do arquivo/unidade reflete o papel real.
3. Nao ha mistura de responsabilidades nao relacionadas.

### 2) Estrutura e leitura

1. Fluxo principal e facil de localizar.
2. Ordem interna esta previsivel.
3. Helpers suportam o fluxo principal, sem competir com ele.

### 3) Fronteiras e dependencias

1. Dependencias condizem com a camada arquitetural.
2. Nao ha vazamento de provider para camadas indevidas.
3. Nao ha aumento injustificado de acoplamento.

### 4) Contratos e previsibilidade

1. Entradas e saidas estao claras.
2. Nao houve mudanca de contrato "disfarcada".
3. Retorno permanece estavel ou explicitamente modelado.

### 5) Side effects

1. Side effects estao explicitos.
2. Unidade aparentemente pura nao esconde efeito colateral.
3. Operacoes externas estao visiveis e contidas.

### 6) Qualidade de implementacao

1. Mudanca manteve escopo da task.
2. Nao houve abstracao prematura.
3. Legibilidade local foi preservada ou melhorada.
4. Mudanca permaneceu review-friendly.

### 7) Testabilidade e seguranca de mudanca

1. Estrutura continua testavel.
2. Dependencias estao explicitas para teste.
3. Mudanca nao aumentou fragilidade de evolucao.

### 8) Metricas (referencia unica em metrics.md)

1. Linhas por arquivo em faixa aceitavel.
2. Linhas por funcao em faixa aceitavel.
3. Parametros por funcao em faixa aceitavel.
4. Nesting e branches em faixa aceitavel.
5. Imports/exports em faixa aceitavel.
6. Risco composto fora de estado critico.

### 9) Naming e semantica

1. Nomes revelam intencao de dominio, sem genericidade vazia.
2. Nomes de funcao/classe/modulo sao coerentes com o papel real.
3. Nao ha abstracao por nome sem contrato claro.

### 10) Qualidade de funcao e classe

1. Funcao preserva responsabilidade principal e fluxo legivel.
2. Classe preserva papel claro, estado intencional e API publica controlada.
3. Nao ha inchaco de unidade por conveniencia local.

### 11) Duplicacao e reutilizacao

1. Nao ha duplicacao relevante de regra de negocio sem justificativa.
2. Extracao de reuse melhora clareza, sem abstracao prematura.
3. Reuso nao introduz acoplamento indevido entre contextos.

### 12) Tratamento de erro

1. Erros sao tratados com intencao e contexto util.
2. Nao ha mascaramento de falha critica.
3. Comportamento de erro externo foi normalizado quando aplicavel.

### 13) Red flags de revisao

1. Crescimento de diff sem relacao com o alvo da task.
2. Mudanca estrutural sem justificativa ou plano.
3. Regressao de scanabilidade apos a alteracao.

## Checklist especifico para output de IA

1. IA preservou fronteiras de responsabilidade.
2. IA evitou helper generico sem semantica.
3. IA nao ampliou escopo sem necessidade.
4. IA manteve side effects visiveis.
5. IA manteve contratos previsiveis.
6. IA nao piorou legibilidade local.

## Resultado da revisao

Classificar outcome final:

1. Approved
2. Approved with Attention
3. Changes Requested
4. Critical

## Regra de bloqueio de revisao

Outcome deve ser, no minimo, `Changes Requested` quando houver:

1. side effect oculto;
2. quebra de fronteira arquitetural sensivel;
3. contrato inconsistente sem modelagem explicita;
4. regressao clara de legibilidade;
5. risco composto em faixa `Critical` sem justificativa.

## Template de saida da revisao

```text
Review Outcome: <Approved | Approved with Attention | Changes Requested | Critical>

Main Findings:
1) <finding> [status: OK/Attention/Limit/Critical]
2) <finding> [status: OK/Attention/Limit/Critical]

Metrics Snapshot (ref: metrics.md):
- File size: <status>
- Function size: <status>
- Nesting/branches: <status>
- Imports/exports: <status>
- Composite risk: <status>

Required Actions:
1) <acao obrigatoria>
2) <acao obrigatoria>

Residual Risks:
1) <risco residual>
```

## Versao curta de prompt para revisao

```text
Revise o diff considerando: responsabilidade, estrutura, dependencias, naming, funcao/classe, contratos, side effects, erro, duplicacao, testabilidade e metricas.
Classifique cada eixo em OK/Attention/Limit/Critical, defina outcome final e liste acoes obrigatorias.
```

## Regra final

Nenhuma revisao deve aprovar mudanca que entregue funcionalidade, mas piore previsibilidade estrutural, contrato, fronteira arquitetural ou risco composto sem justificativa.

