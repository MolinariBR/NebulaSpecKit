# Commands

## Objetivo

Definir uma camada operacional curta para dev e IA, sem substituir
`Workflows/`, `Skills/`, `Quality/` e governança por task do Nébula.

## Escopo

1. Esta camada é um roteador de execução.
2. Cada comando aponta para um workflow principal.
3. Skills são complemento do comando, nunca substituição do workflow.
4. Quality Gate continua obrigatório para fechamento.

## Comandos Canônicos (Fluxo)

| Comando | Quando usar | Workflow principal | Skills de suporte (exemplo) |
| --- | --- | --- | --- |
| `nebula.start` | Início de projeto | `Workflows/initial-setup.md` | `user-stories`, `contracts`, `ui-ux` |
| `nebula.bootstrap` | Task 1 estrutural | `Workflows/bootstrap-structure.md` | `implementation`, `scripts` |
| `nebula.feature` | Nova demanda funcional | `Workflows/new-feature.md` | `implementation`, `tests`, `curl` |
| `nebula.bugfix` | Correção de bug | `Workflows/bug-fix.md` | `logs`, `tests`, `refactoring` |
| `nebula.hotfix` | Incidente crítico | `Workflows/hotfix.md` | `logs`, `deploy`, `curl` |
| `nebula.screen` | Nova tela | `Workflows/new-screen.md` | `ui-ux`, `flow`, `tests` |
| `nebula.ui` | Ajuste de UI | `Workflows/ui-change.md` | `ui-ux`, `flow`, `tests` |
| `nebula.contract` | Mudança de contrato | `Workflows/contract-change.md` | `contracts`, `tests`, `curl` |
| `nebula.integration` | Nova integração externa | `Workflows/new-integration.md` | `integration`, `logs`, `scripts` |
| `nebula.refactor` | Refatoração de módulo | `Workflows/module-refactoring.md` | `refactoring`, `tests`, `integration` |
| `nebula.release` | Fechamento de milestone | `Workflows/release.md` | `deploy`, `logs`, `scripts` |

## Comandos Canônicos (Qualidade e Consistência)

Esses comandos são para projetos usuários que adotam Nébula.
Não fazem parte do pipeline de manutenção do repositório NebulaSpecKit.

1. `nebula.check.context`
   - Executa: `tools/check-context.sh --mode ci`
   - Origem do script: `Templates/Full/automation/` ou `Templates/Quick/automation/`
2. `nebula.check.consistency`
   - Executa: `tools/analyze-consistency.sh`
   - Origem do script: `Templates/Full/automation/` ou `Templates/Quick/automation/`
3. `nebula.gate`
   - Executa o checklist de fechamento em `Quality/validation-rules.md`

## Regras Inegociáveis

1. Bootstrap estrutural apenas na primeira task.
2. Após bootstrap, modo edição de arquivos existentes.
3. Um comando ativa um workflow principal por task.
4. Fechamento exige Quality Gate + evidências em `Docs/tasks.md`.
5. `Docs/plan.md`, `Docs/tasks.md` e `Docs/control.md` devem ser atualizados quando aplicável.
