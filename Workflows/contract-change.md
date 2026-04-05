---
nome: Alteração de Contrato
objetivo: Propagar mudanças de contrato com avaliação de impacto e compatibilidade.
fontes:
  - Docs/contract.yaml
  - Docs/design-system.md
  - Docs/tokens.json
  - Docs/architecture.md
---

# Workflow: Alteração de Contrato

## Gatilho

Mudança em API, Docs/design-system.md ou Docs/tokens.json.

## Sequência recomendada

1. Contratos.
2. Refatoração (impacto em consumidores).
3. Implementação.
4. UI/UX (quando visual).
5. Testes.
6. Curl (quando API).
7. Quality Gate.
8. Atualização de Docs/control.md.

## Documentos principais

- Docs/contract.yaml
- Docs/design-system.md
- Docs/tokens.json
- Docs/entities.md
- Docs/architecture.md
