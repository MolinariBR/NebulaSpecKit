---
nome: Hotfix
objetivo: Corrigir incidente critico em produção com menor risco possível.
fontes:
  - Docs/control.md
  - Docs/deploy.md
  - Docs/contract.yaml
  - Docs/architecture.md
---

# Workflow: Hotfix

## Gatilho

Incidente critico em produção.

## Sequência recomendada

1. Logs.
2. Contratos (limites de segurança).
3. Testes mínimos de reprodução.
4. Implementação de menor risco.
5. Deploy.
6. Curl.
7. Logs pos-deploy.
8. Quality Gate.
9. Atualização de Docs/control.md.

## Documentos principais

- Docs/control.md
- Docs/deploy.md
- Docs/contract.yaml
- Docs/architecture.md
