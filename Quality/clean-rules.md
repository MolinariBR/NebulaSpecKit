# Clean Rules

## Objetivo

Definir regras comportamentais de escrita e evolucao de codigo para manter:

1. clareza;
2. foco de responsabilidade;
3. previsibilidade;
4. baixo custo de manutencao.

Este arquivo define as regras comportamentais de escrita e evolucao de codigo do projeto.

## Escopo

Aplica-se a:

1. codigo novo;
2. codigo editado;
3. codigo refatorado;
4. output de IA;
5. revisao tecnica.

## Regra de ownership

1. Regras comportamentais vivem aqui.
2. Thresholds numericos vivem em `metrics.md`.
3. Regras de estrutura de arquivo vivem em `structure-rules.md`.
4. Fluxo de implementacao vive em `execution-policy.md`.
5. Checklist formal de revisao vive em `review-checklist.md`.

## Principios operacionais

1. Clareza sobre cleverness.
2. Responsabilidade unica por unidade.
3. Contratos previsiveis.
4. Side effects visiveis.
5. Fronteiras explicitas.
6. Evolucao incremental e revisavel.

## Regras nucleares

### 1) Nomeacao por intencao

1. Nome deve explicar papel e contexto.
2. Evitar nome generico (`data`, `utils`, `manager`, `item`).
3. Usar vocabulario de dominio quando possivel.

### 2) Funcao com foco claro

1. Uma funcao pode ter varios passos, mas um proposito central.
2. Evitar mistura de validacao, regra de negocio, persistencia e logging na mesma funcao.
3. Se o fluxo nao couber em uma frase clara, refatorar.

### 3) Separacao entre regra e detalhe tecnico

1. Nao misturar decisao de negocio com detalhe de framework/provider.
2. Traduzir semantica externa na borda.
3. Manter regra de negocio compreensivel sem dependencia de infraestrutura.

### 4) Fluxo explicito

1. Preferir passos nomeados e decisoes visiveis.
2. Evitar compressao excessiva de logica em uma linha.
3. Priorizar guard clauses e early return para reduzir nesting.

### 5) Estado explicito

1. Evitar acoplamento de flags implicitas.
2. Preferir estados nomeados/modelados.
3. Evitar combinacoes booleanas que simulam maquina de estado sem declaracao.

### 6) Contrato previsivel

1. Entradas e saidas devem ser estaveis.
2. Evitar retorno inconsistente sem modelagem explicita.
3. Mudanca de contrato deve ser intencional e rastreavel.

### 7) Side effects visiveis

1. Nao esconder side effect em unidade aparentemente pura.
2. Tornar operacoes externas identificaveis.
3. Isolar interacoes externas quando possivel.

### 8) Erro claro e acionavel

1. Falhar cedo quando adequado.
2. Mensagem de erro deve ter contexto util.
3. Nao mascarar erro com retorno vago.

### 9) Duplicacao de significado

1. Evitar duplicar regra de negocio em varios pontos.
2. Nao abstrair cedo demais.
3. Preferir pequena repeticao local a abstracao ruim.

### 10) Comentario com funcao real

1. Comentario deve explicar contexto nao-obvio.
2. Nao narrar o obvio.
3. Nao usar comentario para compensar nomeacao ruim.

### 11) Testabilidade como restricao de design

1. Dependencias explicitas para facilitar teste.
2. Separar logica deterministica de integracao quando necessario.
3. Nao piorar testabilidade para reduzir poucas linhas.

### 12) Preservacao de legibilidade local

1. Toda mudanca deve preservar ou melhorar legibilidade da area tocada.
2. Codigo que funciona, mas piora leitura, nao e considerado bom resultado.

## Naming guidance rapido

1. Variaveis: nome por papel contextual, sem abreviacao opaca.
2. Funcoes: verbo + objeto de dominio, indicando acao real.
3. Booleanos: prefixo semantico (`is/has/can/should`) com significado verificavel.
4. Classes: nome por responsabilidade, evitando sufixo generico de status.
5. Constantes: maiusculas para valor imutavel global e nome sem ambiguidade.

## Red flags comportamentais

Revisar imediatamente quando houver:

1. naming generico;
2. excesso de verbos por funcao;
3. mistura de regra e infraestrutura;
4. side effect oculto;
5. contrato inconsistente;
6. abstracao sem ganho semantico;
7. queda de legibilidade apos a mudanca.

## Triggers operacionais de revisao

1. Funcao deixa de caber em resumo de uma frase.
2. Arquivo recebe responsabilidades cruzadas na mesma task.
3. Diff cresce com muitos edits nao relacionados ao alvo.
4. Contrato ou erro muda sem registro explicito.

## Anti-patterns alvo

1. helper dumping sem semantica;
2. abstracao prematura por conveniencia;
3. side effect oculto em fluxo aparentemente puro;
4. mistura de regra de negocio com detalhe de framework.

## Regras para IA

AI deve:

1. preservar fronteiras e ownership local;
2. explicitar incerteza em vez de inventar estrutura;
3. priorizar clareza local antes de abstrair.

AI nao deve:

1. ampliar escopo sem necessidade;
2. introduzir helper generico sem contrato;
3. modificar area nao relacionada.

Output de IA e incompleto quando houver:

1. regressao de legibilidade;
2. contrato menos previsivel;
3. side effect novo sem visibilidade.

## Regras para revisores humanos

1. Basear feedback em risco estrutural, nao preferencia pessoal.
2. Sinalizar obrigatoriamente mudanca de contrato, fronteira e side effect.
3. Escalar para `Changes Requested` quando houver risco composto alto.

## Enforcement orientativo

1. Advisory: ajuste de naming, fluxo e scanabilidade.
2. Warning: repeticao de red flag ou degradacao recorrente de clareza.
3. Blocking: side effect oculto, mistura de camadas sensivel, contrato inconsistente sem modelagem.

## Integracao operacional

1. `execution-policy.md` define quando e como aplicar estas regras durante implementacao.
2. `review-checklist.md` verifica estas regras em code review.
3. `metrics.md` mede sinais objetivos de degradacao estrutural.
4. `validation-rules.md` decide fechamento de task com base em evidencias.

## Checklist curto operacional

1. Naming: nomes explicam intencao e contexto.
2. Responsabilidade: unidade tem papel unico e claro.
3. Fronteiras: regra de negocio separada de detalhe tecnico.
4. Legibilidade: fluxo principal segue facil de localizar.
5. Previsibilidade: contrato e erros seguem comportamento explicito.
6. Manutencao: mudanca reduz ou controla risco estrutural.

## Regra final

Codigo limpo operacional e aquele que continua compreensivel, previsivel e seguro para evoluir apos a mudanca, nao apenas no momento da entrega.

