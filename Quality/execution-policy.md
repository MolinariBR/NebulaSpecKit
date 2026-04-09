# Execution Policy

## Objetivo

Definir como implementar mudancas de codigo com escopo controlado, clareza estrutural e seguranca de evolucao.

Este arquivo define o fluxo operacional de implementacao com escopo controlado e evolucao segura.

## Escopo

Aplica-se a:

1. feature;
2. bug fix;
3. refatoracao controlada;
4. integracao;
5. ajuste de contrato;
6. cleanup local necessario para viabilizar a entrega.

Nao se aplica a:

1. reescrita arquitetural ampla sem task explicita;
2. mudanca em massa sem rastreabilidade por task;
3. refatoracao oportunista fora do escopo.

## Regras de escopo

1. Toda implementacao inicia com alvo definido:
- o que muda;
- por que muda;
- onde deve mudar;
- o que nao deve ser tocado.

2. Nao ampliar escopo sem necessidade tecnica direta.

3. Refatoracao local e permitida apenas quando melhora a mudanca alvo.

4. Nao expandir responsabilidade de arquivo/modulo/classe/funcao sem justificativa.

## Analise pre-implementacao

Antes de editar:

1. Classificar tipo de mudanca (feature, bug, refactor, integracao, contrato).
2. Definir ownership da mudanca (unidade dona).
3. Mapear impacto de fronteira:
- dominio;
- fluxo de aplicacao;
- infraestrutura;
- interface;
- contrato de dados.
4. Mapear risco:
- efeito colateral;
- quebra de contrato;
- vazamento de camada;
- aumento de complexidade.

## Modelo de execucao

1. Implementar em passos pequenos e coerentes.
2. Manter o codigo valido a cada passo relevante.
3. Priorizar clareza explicita sobre "cleverness".
4. Preservar legibilidade local na mesma task.

## Regras estruturais minimas

1. Colocar codigo na unidade dona da responsabilidade; criar nova unidade apenas quando a atual perder foco.
2. Toda funcao deve manter intencao unica, fluxo legivel e parametros sob controle.
3. Toda classe deve manter papel claro, estado intencional e superficie publica minima.
4. Todo arquivo/modulo deve ter proposito principal, fluxo visivel e exports intencionais.
5. Toda dependencia nova exige justificativa tecnica, sem vazamento entre camadas e com imports legiveis.

## Regras de design durante implementacao

1. Nomear por intencao e contexto de dominio.
2. Evitar helper generico sem identidade semantica.
3. Manter side effects visiveis.
4. Separar regra de negocio de detalhe tecnico.
5. Preservar previsibilidade de contrato de entrada/saida.
6. Evitar acoplamento cruzado de camadas.

## Regras de evolucao segura

1. Nao esconder mudanca de contrato como ajuste incidental.
2. Nao ampliar superficie publica sem necessidade.
3. Nao piorar testabilidade para economizar linhas.
4. Nao degradar reviewabilidade da area tocada.

## Regras tecnicas complementares

1. Tratamento de erro deve ser intencional, com validacao de fronteira e mensagens acionaveis.
2. Side effect deve ser explicito, rastreavel e separado de logica deterministica quando possivel.
3. Evitar duplicacao de regra de negocio; extrair somente quando a extracao melhora clareza.
4. Refatorar no limite necessario para viabilizar implementacao limpa, incremental e com comportamento preservado.

## Workflow minimo de implementacao

1. Identificar alvo exato da mudanca.
2. Confirmar ownership e fronteiras.
3. Escolher menor caminho coerente.
4. Implementar incrementalmente.
5. Refatorar localmente quando necessario.
6. Revalidar legibilidade, escopo e compatibilidade estrutural.

## Regras de agente e implementador

1. AI e humano devem evitar edits nao relacionados, preservar convencoes e explicitar incertezas.
2. AI deve preferir estrutura explicita a abstracao especulativa.
3. Implementador deve priorizar manutencao de longo prazo sobre conveniencia local.
4. Mudancas devem permanecer review-friendly e rastreaveis por task.

## Red flags operacionais

Reavaliar implementacao quando ocorrer:

1. arquivo cresce sem centro de responsabilidade claro;
2. funcao fica dificil de resumir em uma frase;
3. nova dependencia cruza camada arquitetural;
4. side effect fica opaco;
5. contrato fica menos previsivel;
6. mudanca exige muitos edits nao relacionados;
7. legibilidade local piora apos a mudanca.

## Criterios de conclusao da implementacao

A implementacao so encerra quando:

1. comportamento alvo foi entregue;
2. escopo permaneceu controlado;
3. contratos estao previsiveis;
4. fronteiras arquiteturais foram preservadas;
5. area tocada segue legivel e revisavel;
6. riscos residuais foram explicitados na task.

## Interacao e prioridade entre politicas

Ordem de prevalencia operacional:

1. `execution-policy.md` define o fluxo de implementacao e criterios de encerramento.
2. `metrics.md` define limites numericos, severidade e acao obrigatoria por threshold.
3. `structure-rules.md` define anatomia e contratos estruturais de arquivo/modulo.
4. `clean-rules.md` define higiene de design e legibilidade comportamental.
5. `review-checklist.md` define gate formal de revisao.
6. `validation-rules.md` define estrategia de validacao.

Regra de excecao:

1. Excecao so e valida com justificativa explicita, risco documentado, escopo limitado e plano de reversao/quitacao.
2. Se houver conflito entre politicas, prevalece a regra mais restritiva para seguranca estrutural.

Dependencias desta serie:

1. `metrics.md` para thresholds numericos;
2. `structure-rules.md` para anatomia de arquivo;
3. `clean-rules.md` para regras comportamentais detalhadas;
4. `review-checklist.md` para checklist formal de revisao;
5. `validation-rules.md` para testes realistas, anti-mock e dependencias.

## Regra final

Nenhuma implementacao e considerada concluida se melhorar entrega funcional, mas piorar qualidade estrutural, previsibilidade de contrato ou governanca de risco.

