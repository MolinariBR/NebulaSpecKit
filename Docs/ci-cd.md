# CI/CD - NebulaSpecKit

Guia operacional do pipeline de integracao continua e entrega de releases do repositório.

## Objetivo

Automatizar Quality Gate documental, checagem de links e publicacao de releases com rastreabilidade.

## Workflows

1. `CI`
2. `Link Check (Scheduled)`
3. `Release`
4. `Quality Gate (Reusable)` (workflow interno chamado pelos demais)

## Arquivos

- `.github/workflows/ci.yml`
- `.github/workflows/links-scheduled.yml`
- `.github/workflows/release.yml`
- `.github/workflows/_quality-gate.yml`
- `.github/dependabot.yml`
- `.markdownlint-cli2.jsonc`
- `.lycheeignore`

## Fluxo de Qualidade (CI)

Gatilhos:

1. `pull_request` para `main`
2. `push` em `main`
3. `workflow_dispatch` manual

Validações executadas:

1. Lint de Markdown
2. Validação estrutural de arquivos obrigatorios
3. Validação de `JSON` e `YAML` principais
4. Checagem de links internos em modo offline

Saída:

1. Artifact com relatorio de links internos (`internal-links-report-*`)

## Fluxo de Links Externos

Workflow: `Link Check (Scheduled)`

Gatilhos:

1. Agendado diariamente (`cron`)
2. `workflow_dispatch` manual

Validações:

1. Links externos em todos os `.md`
2. Cache local do lychee para reduzir rate limit e latencia

Saída:

1. Artifact com relatorio de links externos (`external-links-report-*`)

## Fluxo de Release

Workflow: `Release`

Gatilhos:

1. Push de tag `v*` (exemplo: `v1.0.1`)
2. `workflow_dispatch` com input `version`

Ordem:

1. Executa Quality Gate
2. Gera artefatos `.tar.gz` e `.zip`
3. Publica GitHub Release com notas automaticas

## Versionamento

Padrao exigido:

1. `vMAJOR.MINOR.PATCH`
2. Sufixo opcional permitido (exemplo: `v1.2.3-rc.1`)

## Politica de Branch Protection (Recomendada)

Para `main`, habilitar:

1. Require pull request before merging
2. Require status checks before merging
3. Selecionar checks obrigatorios:
   - `Quality Gate / Validate Documentation Quality`
4. Block force push
5. Block branch deletion

Observacao: o nome do job de status check deve permanecer estavel para nao quebrar a regra de protecao.

## Dependabot

Arquivo: `.github/dependabot.yml`

Escopo:

1. Atualizacao semanal de GitHub Actions
2. PRs de dependencia com labels `dependencies` e `ci`

## Operacao Manual

Executar CI manualmente:

1. Actions -> `CI` -> `Run workflow`

Executar checagem externa de links:

1. Actions -> `Link Check (Scheduled)` -> `Run workflow`

Criar release manual:

1. Actions -> `Release` -> `Run workflow`
2. Preencher `version` (exemplo: `v1.0.1`)

## Troubleshooting

1. Falha em Markdown lint:
   - Ajustar formatação do arquivo reportado
2. Falha em YAML/JSON:
   - Validar sintaxe do arquivo reportado
3. Falha em links externos:
   - Confirmar se o dominio esta online
   - Se necessario, adicionar excecao em `.lycheeignore` com justificativa
4. Falha de release:
   - Confirmar versao no padrao `v*`
   - Confirmar permissao `contents: write`
