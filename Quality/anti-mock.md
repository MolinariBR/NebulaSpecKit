# Anti-Mock

## Objetivo

Definir quando mock/stub/placeholder sao proibidos e como tratar excecao controlada.

## Escopo

Aplica-se a:

1. integracao;
2. contrato;
3. e2e;
4. release/hotfix.

## Regra geral

Mock, stub e placeholder sao proibidos por padrao nos escopos deste arquivo.

## Substituicao por validacao real

Quando aplicavel, substituir mock por:

1. Testcontainers para banco, fila, cache e dependencia de integracao.
2. curl/scripts versionados para contrato de API.
3. e2e real para interface web.
4. BrowserStack + dispositivo fisico para fluxos mobile criticos.

## Clientes API e anti-mock

1. Insomnia/Postman podem ser usados para exploracao, mas sem resposta simulada.
2. Validacao final de contrato exige `curl/scripts` versionados no repositorio.
3. Se Insomnia/Postman for usado, registrar request/collection e equivalente reproduzivel.

## Excecao controlada

Excecao so e valida com registro formal em `Docs/tasks.md` contendo:

1. justificativa tecnica objetiva;
2. escopo exato da excecao;
3. prazo de remocao;
4. risco assumido;
5. plano de substituicao por validacao real.

Sem registro completo, a excecao e invalida.
Excecao tambem e invalida quando existir ferramenta real aplicavel sem justificativa tecnica.

## Regra de bloqueio

A task permanece aberta quando houver:

1. uso de mock/stub/placeholder sem excecao formal completa;
2. excecao sem prazo de remocao;
3. excecao sem plano de substituicao;
4. uso de mock em integracao quando Testcontainers era aplicavel;
5. simulacao mobile critica quando BrowserStack/dispositivo fisico eram aplicaveis;
6. validacao de API baseada apenas em cliente GUI sem comando reproduzivel.

## Integracao operacional

1. `validation-rules.md` consolida esta politica no fluxo de validacao.
2. `validation-rules.md` usa esta regra para bloqueio de fechamento.
3. `review-checklist.md` deve sinalizar quando a excecao estiver incompleta.
