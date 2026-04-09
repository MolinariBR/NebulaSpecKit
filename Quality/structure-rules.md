# Structure Rules

## Objetivo

Definir regras de estrutura de arquivo para manter:

1. leitura rapida;
2. coesao;
3. fronteiras claras;
4. manutencao segura.

Este arquivo define a politica estrutural de arquivos, modulos, contratos e fronteiras do projeto.

## Escopo

Aplica-se a:

1. arquivos de dominio;
2. aplicacao;
3. infraestrutura;
4. interface/componente;
5. scripts mantidos pelo time.

## Regra de ownership

1. Anatomia e organizacao de arquivo vivem aqui.
2. Thresholds numericos vivem em `metrics.md`.
3. Regras comportamentais de escrita vivem em `clean-rules.md`.
4. Fluxo de implementacao vive em `execution-policy.md`.
5. Checklist de revisao vive em `review-checklist.md`.

## Principios estruturais

1. Um arquivo deve ter um centro de responsabilidade claro.
2. O fluxo principal deve ser facil de localizar.
3. A estrutura deve ser previsivel para dev e IA.
4. A superficie publica deve ser pequena e intencional.

## Anatomia recomendada

Ordem sugerida:

1. cabecalho de contexto (opcional);
2. imports/dependencias;
3. constantes locais;
4. contratos/tipos/interfaces/schemas;
5. estrutura principal publica;
6. helpers privados;
7. exports publicos.

Regra de leitura:
- intencao primeiro;
- fluxo principal depois;
- detalhe de suporte por ultimo.

## Regras de identidade de arquivo

1. Nome do arquivo deve refletir responsabilidade principal.
2. Evitar nomes genericos sem contexto (`utils`, `common`, `manager`).
3. Arquivo nao pode virar "container" de logicas sem relacao.

## Regras de imports e dependencias

### Agrupamento recomendado

1. runtime/stdlib;
2. bibliotecas de terceiros;
3. shared infra;
4. dependencias internas de dominio/aplicacao;
5. contratos/tipos;
6. locais relativos.

### Regras

1. Importar apenas o que for usado.
2. Evitar mistura de camadas sem justificativa.
3. Evitar dependencia circular.
4. Evitar espalhar detalhes de infraestrutura em arquivo de dominio.

## Regras de constantes e estruturas locais

1. Manter constante local quando o significado for local.
2. Promover constante somente quando houver reuso semantico real.
3. Evitar "constante fake" usada para ocultar valor sem ganho de clareza.
4. Mapas de decisao devem permanecer legiveis e com chaves sem ambiguidades.

## Regras de contratos e fronteiras

1. Contratos devem ficar proximos do comportamento que organizam.
2. Contrato compartilhado deve ser semanticamente compartilhado.
3. Padrao de retorno deve permanecer estavel.
4. Mudancas de contrato devem ser explicitas e rastreaveis.

## Regras de estrutura principal e helpers

1. Estrutura principal deve dominar o arquivo.
2. Helper deve ser subordinado ao fluxo principal.
3. Helper mais complexo que estrutura principal e sinal de alerta.
4. Evitar helpers genericos sem identidade de dominio.

## Regras de exports

1. Exportar o minimo necessario.
2. Manter internals privados por padrao.
3. Evitar ampliar API publica sem necessidade da task.

## Regras para arquivos de integracao

Aplica-se a gateways, clients, adapters, providers:

1. Fronteira externa deve ficar explicita no arquivo.
2. Semantica externa deve ser traduzida para contrato local.
3. Erros externos devem ser normalizados quando adequado.
4. Evitar vazamento de detalhes de provider para o restante do sistema.

## Regras para modulos utilitarios

1. Evitar arquivo utilitario generico amplo.
2. Se utilitario existir, manter dominio semantico estreito.
3. Nao misturar varios dominios tecnicos no mesmo utilitario.

## Regras universais de estrutura

1. Arquivo deve ter uma razao clara para existir.
2. Fluxo principal deve aparecer antes de detalhe secundario.
3. Side effects nao devem ficar escondidos.
4. Scanabilidade e previsibilidade valem mais que compactacao extrema.
5. Metricas orientam decisao, mas nao substituem significado semantico.

## Regras estruturais por funcao

1. Funcao deve ter responsabilidade principal clara.
2. Nome da funcao deve explicitar acao e contexto.
3. Evitar side effect oculto e retorno imprevisivel.
4. Reduzir parametros, branches e nesting quando houver pressao estrutural.

## Regras estruturais por classe

1. Classe deve representar conceito unico e papel claro.
2. Evitar acumulo de responsabilidades e estado sem controle.
3. Manter API publica pequena e coerente.
4. Classe utilitaria pura exige justificativa semantica.

## Warning signs estruturais

Revisar imediatamente quando houver:

1. responsabilidade principal ambigua;
2. multiplas estruturas primarias sem necessidade;
3. mistura de camadas em arquivo sensivel;
4. side effect escondido em funcao aparentemente simples;
5. excesso de exports sem justificativa;
6. helper com mais complexidade que o fluxo principal.

## Excecoes aceitaveis

1. codigo gerado;
2. migration;
3. schema/snapshot declarativo;
4. entrypoint de framework;
5. shim de compatibilidade;
6. mapa estatico grande com semantica clara.

Mesmo em excecao:

1. manter naming identificavel;
2. manter scanabilidade minima;
3. manter superficie publica controlada quando aplicavel.

## Modelo de revisao estrutural

1. Identidade: centro de responsabilidade e nome coerente.
2. Estrutura: anatomia e ordem interna previsiveis.
3. Dependencias: imports e fronteiras sem vazamento.
4. Coesao: principal domina, helper e subordinado.
5. Previsibilidade: contrato, side effect e exports sob controle.
6. Metricas: consultar `metrics.md` para sinais de pressao.

## Niveis de outcome estrutural

1. Healthy: sem risco estrutural relevante.
2. Attention: sinais iniciais de drift.
3. Limit: pressao estrutural recorrente, exige acao.
4. Critical: risco alto, bloqueio ou refatoracao obrigatoria.

## Interacao com clean rules

1. `structure-rules.md` define forma e organizacao.
2. `clean-rules.md` define comportamento de escrita dentro da forma.
3. Em conflito, prevalece a regra mais restritiva para proteger clareza e fronteira.

## Enforcement padrao

1. Advisory: ajuste de ordem, naming e scanabilidade.
2. Warning: drift de coesao, imports, helpers ou exports.
3. Blocking: quebra de fronteira, side effect oculto ou estrutura critica sem justificativa.

## Integracao operacional

1. `execution-policy.md` aplica estas regras durante implementacao.
2. `clean-rules.md` guia comportamento de escrita dentro desta estrutura.
3. `metrics.md` define limites numericos das estruturas.
4. `review-checklist.md` valida aderencia em revisao.
5. `validation-rules.md` fecha task somente com evidencia suficiente.

## Regra final

Estrutura boa e aquela que permite localizar intencao, fluxo principal, fronteira e risco de mudanca em poucos minutos, sem leitura arqueologica.

