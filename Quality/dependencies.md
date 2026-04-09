# Dependencies

## Objetivo

Definir regras de compatibilidade, lockfile e atualizacao de dependencias.

## Regras obrigatorias

1. Lockfile deve estar versionado e consistente.
2. Evitar ranges amplos para dependencia critica.
3. Validar compatibilidade entre runtime, framework e bibliotecas.
4. Atualizacao de dependencia exige quality gate completo.
5. Dependencias de validacao (Testcontainers, BrowserStack SDK e ferramenta e2e) devem ter versao controlada.
6. Ferramentas de API usadas na validacao (Insomnia/Postman/Newman/HTTPie) devem ter versao e artefato rastreavel quando fizerem parte do fluxo.

## Validacoes minimas

1. Instalacao limpa sem conflito.
2. Build e testes aprovados apos atualizacao.
3. Registro da versao alterada e impacto em `Docs/tasks.md`.
4. Smoke de ferramentas de validacao apos update (quando aplicavel).

## Restricoes

1. Nao introduzir biblioteca sem justificativa tecnica.
2. Nao manter dependencia sem uso real.
3. Nao atualizar dependencia critica sem evidencia de compatibilidade.
4. Nao atualizar dependencia de teste realista sem revalidar pipeline de qualidade.

## Regra de bloqueio

A task permanece aberta quando houver:

1. lockfile inconsistente;
2. atualizacao sem build/testes;
3. atualizacao critica sem evidencia de compatibilidade;
4. falha de smoke em Testcontainers/BrowserStack/e2e sem mitigacao.

## Integracao operacional

1. `validation-rules.md` consolida estas regras no fluxo de validacao.
2. `validation-rules.md` aplica bloqueio de fechamento por inconsistencias de dependencia.
3. `metrics.md` complementa com sinais estruturais de risco.
