# Validation Rules

## Objetivo

Definir regras de validacao tecnica para garantir fidelidade de producao antes do fechamento de task.

Este arquivo consolida as regras de `realistic-tests.md`, `anti-mock.md` e `dependencies.md`.

## Escopo

Aplica-se a:

1. validacao de backend/API;
2. validacao de interface web;
3. validacao mobile;
4. validacao de integracao;
5. validacao de atualizacao de dependencias.

## Regra de ownership

1. Regras de validacao vivem aqui.
2. Regras especificas de teste vivem em `realistic-tests.md`.
3. Regra anti-mock vive em `anti-mock.md`.
4. Regras de dependencias vivem em `dependencies.md`.
5. Checklist de fechamento vive em `validation-rules.md`.
6. Thresholds numericos vivem em `metrics.md`.
7. Fluxo de implementacao vive em `execution-policy.md`.
8. Checklist de revisao vive em `review-checklist.md`.

## Principios de validacao

1. Validar comportamento real, nao simulacao otimista.
2. Evidencia reproduzivel e obrigatoria.
3. Sem evidencia, task permanece aberta.
4. Validacao deve ser proporcional ao risco da mudanca.

## Ferramentas obrigatorias por contexto

1. Integracao backend/API: Testcontainers, quando aplicavel.
2. Contrato de API: curl/scripts versionados e reproduziveis.
3. Web: e2e real com ferramenta oficial do projeto.
4. Mobile/cross-device: BrowserStack (ou equivalente aprovado) + dispositivo fisico local.
5. Insomnia/Postman/Newman/HTTPie: ferramentas de apoio para exploracao e automacao complementar de API.

Regra:

1. Ferramenta aplicavel sem uso exige excecao formal em `Docs/tasks.md`.
2. Ferramenta de apoio nao substitui comando reproduzivel versionado.

## Regras de testes realistas

### Regras gerais

1. Priorizar componentes reais e infraestrutura realista.
2. Evitar simulacoes que escondam risco de producao.
3. Registrar ambiente, dados e comandos executados.

### Backend e API

1. Integracao deve usar Testcontainers por padrao (excecao exige registro formal).
2. Contrato de API deve ser validado com curl/scripts reproduziveis e versionados.
3. Cobrir falhas realistas (timeout, indisponibilidade, validacao).

### Interface web

1. Fluxos criticos devem ter validacao e2e.
2. Mudanca visual relevante deve ter validacao com prototype e e2e.

### Mobile

1. Fluxos criticos devem ser validados em BrowserStack (ou alternativa).
2. Fluxos criticos devem ser validados em dispositivo fisico local (quando aplicavel).

## Politica anti-mock

### Regra geral

Mock/stub/placeholder sao proibidos por padrao em:

1. integracao;
2. contrato;
3. e2e;
4. release/hotfix.

### Excecao controlada

Excecao so e aceita com registro formal na task contendo:

1. justificativa tecnica objetiva;
2. escopo exato da excecao;
3. prazo de remocao;
4. risco assumido;
5. plano de substituicao por validacao real.

Sem registro completo, excecao e invalida.

## Regras de dependencias e compatibilidade

1. Lockfile deve estar versionado e consistente.
2. Evitar ranges amplos para dependencia critica.
3. Validar compatibilidade entre runtime/framework/bibliotecas.
4. Atualizacao de dependencia exige quality gate completo e evidencias de build/testes.
5. Nao introduzir biblioteca sem justificativa tecnica.
6. Nao manter dependencia sem uso real.

## Evidencias obrigatorias

Registrar na task:

1. resultado de lint/typecheck/build (quando aplicavel);
2. resultado de testes (pass/fail por suite) e ambiente utilizado;
3. comandos curl/scripts executados (quando houver API);
4. evidencias e2e de fluxos criticos (quando houver UI);
5. evidencias mobile (quando aplicavel);
6. impacto de dependencia e lockfile;
7. artefatos de cliente API usados (colecao Insomnia/Postman e relatorio Newman), quando aplicavel;
8. TASK-ID, hash do commit e arquivos tocados.

## Perfis de validacao por tipo de mudanca

### Feature com API + UI

1. lint/typecheck/build;
2. testes de integracao;
3. validacao de contrato com curl/scripts;
4. e2e de fluxos criticos;
5. checagem de dependencia/lockfile.

### Bug fix

1. reproducao da falha;
2. teste de regressao da causa;
3. validacao de impacto de contrato (se houver);
4. evidencias de nao-regressao nos fluxos afetados.

### Refatoracao

1. evidencia de preservacao de comportamento;
2. validacao de contrato inalterado (ou mudanca explicitada);
3. risco residual documentado.

### Hotfix

1. validacao minima de seguranca da correcao;
2. evidencia de estabilizacao;
3. rastreabilidade de risco residual e plano de follow-up.

### Atualizacao de dependencia

1. instalacao limpa sem conflito;
2. quality gate completo com build e testes pos-atualizacao;
3. registro de impacto da versao alterada.

## Regra de bloqueio

Task deve permanecer aberta quando houver qualquer um dos casos:

1. ausencia de evidencia obrigatoria;
2. uso de mock/stub sem excecao formal completa;
3. validacao de API sem comando reproduzivel;
4. mudanca de UI sem validacao minima de fluxo critico;
5. lockfile inconsistente;
6. quality gate de dependencia incompleto;
7. integracao sem Testcontainers quando aplicavel e sem excecao formal;
8. fluxo mobile critico sem BrowserStack/dispositivo fisico quando aplicavel;
9. validacao de API baseada apenas em cliente GUI sem curl/scripts reproduziveis;
10. risco critico sem mitigacao ou plano de acao.

## Integracao operacional

1. `validation-rules.md` consome estas regras para decisao final de fechamento.
2. `review-checklist.md` verifica consistencia tecnica da validacao.
3. `metrics.md` cobre sinais estruturais complementares.
4. `execution-policy.md` governa como implementar antes de validar.
