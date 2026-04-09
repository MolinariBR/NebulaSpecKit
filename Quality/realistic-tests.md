# Realistic Tests

## Objetivo

Definir validacao de testes com fidelidade de producao e evidencia reproduzivel.

## Regras gerais

1. Priorizar componentes reais e infraestrutura realista.
2. Evitar simulacao otimista que esconda risco de producao.
3. Registrar ambiente, dados e comandos executados.

## Ferramentas oficiais de validacao

1. Backend/API de integracao: Testcontainers.
2. Contrato de API: curl/scripts versionados.
3. Web: ferramenta e2e oficial do projeto (ex.: Playwright/Cypress).
4. Mobile/cross-device: BrowserStack (ou equivalente aprovado) + dispositivo fisico local.

## Ferramentas de apoio (API e observabilidade)

1. Insomnia ou Postman para exploracao e depuracao de requests.
2. Newman para execucao automatizada de colecoes Postman.
3. HTTPie como alternativa CLI para testes manuais rapidos.
4. k6 (ou equivalente) para smoke/performance basica quando houver risco de carga.

Regra:

1. Quando a ferramenta for aplicavel ao contexto, seu uso e obrigatorio.
2. Nao uso de ferramenta aplicavel exige excecao formal em `Docs/tasks.md`.
3. Ferramenta de apoio nao substitui evidencia reproduzivel em `curl/scripts`.

## Backend e API

1. Integracao deve usar Testcontainers por padrao.
2. Contrato de API deve ser validado com curl/scripts reproduziveis e versionados.
3. Cobrir falhas realistas: timeout, indisponibilidade e validacao.

## Interface web

1. Fluxos criticos devem ter validacao e2e.
2. Mudanca visual relevante deve ser validada com prototype e e2e.

## Mobile

1. Fluxos criticos devem ser validados em BrowserStack (ou alternativa).
2. Fluxos criticos devem ser validados em dispositivo fisico local, quando aplicavel.

## Evidencias obrigatorias

Registrar em `Docs/tasks.md`:

1. comandos executados;
2. status pass/fail por suite;
3. ambiente e versoes utilizadas;
4. ferramenta utilizada por contexto (Testcontainers, e2e, BrowserStack, curl/scripts);
5. artefatos de apoio usados (colecao Insomnia/Postman ou relatorio Newman), quando aplicavel;
6. TASK-ID, hash de commit e arquivos tocados.

## Regra de bloqueio

A task permanece aberta quando houver:

1. ausencia de evidencias obrigatorias;
2. validacao de API sem comando reproduzivel;
3. mudanca de UI sem validacao minima de fluxo critico;
4. integracao sem Testcontainers quando aplicavel e sem excecao formal;
5. fluxo mobile critico sem BrowserStack e sem dispositivo fisico, quando aplicavel.

## Integracao operacional

1. `validation-rules.md` consolida estas regras por perfil de mudanca.
2. `validation-rules.md` exige estas evidencias para fechamento.
3. `review-checklist.md` valida consistencia tecnica da validacao.
