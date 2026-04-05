---
nome: Bug Fix
objetivo: Corrigir falha com reprodução, validação e registro de impacto.
fontes:
  - Docs/control.md
  - Docs/contract.yaml
  - Docs/architecture.md
  - Docs/user-stories.md
---

# Workflow: Bug Fix

## Gatilho

Falha em produção, teste ou comportamento divergente.

## Sequência recomendada

1. Logs.
2. Refatoração (diagnostico técnico).
3. Contratos (checar quebra).
4. Testes (reprodução).
5. Implementação.
6. Curl (quando houver API).
7. Quality Gate.
8. Atualização de Docs/control.md.

## Documentos principais

- Docs/control.md
- Docs/contract.yaml
- Docs/architecture.md
- Docs/user-stories.md
