# Automation (User Projects)

Automacoes opcionais para projetos que usam o Nébula Spec Kit.

## Objetivo

Fornecer checks locais read-only para validar contexto e consistencia documental
no projeto do usuario, sem acoplar ao pipeline de manutencao do proprio
repositório NebulaSpecKit.

## Arquivos

1. `check-context.sh`: valida pre-condicoes de contexto por fase.
2. `analyze-consistency.sh`: analisa consistencia entre documentos canônicos.

## Como usar no projeto do usuario

1. Copiar os scripts para o projeto alvo (ex.: `tools/`).
2. Tornar executavel:
   - `chmod +x tools/check-context.sh tools/analyze-consistency.sh`
3. Executar:
   - `tools/check-context.sh --mode ci`
   - `tools/analyze-consistency.sh`

## Escopo

1. Esses scripts sao para o fluxo do usuario em projetos que adotam Nébula.
2. Esses scripts nao fazem parte do CI/release de manutencao do NebulaSpecKit.
