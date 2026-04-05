---
nome: "Testes"
objetivo: "Validar comportamento, contrato e regressão."
fontes:
  - "Docs/tasks.md"
  - "Docs/user-stories.md"
  - "Docs/contract.yaml"
  - "Quality/realistic-tests.md"
  - "Quality/gate.md"
---

# Skill: Testes

## Objetivo

Validar comportamento, contrato e regressão.

## Fontes principais

- Docs/tasks.md
- Docs/user-stories.md
- Docs/contract.yaml

## Passos

1. Mapear cenários críticos e critérios de aceite.
2. Priorizar testes realistas com infraestrutura de produção ou equivalente.
3. Usar Testcontainers por padrão para integração de backend/API.
4. Validar interface com e2e em fluxos críticos.
5. Para mobile, validar em BrowserStack (ou alternativa) e em dispositivo físico local quando aplicável.
6. Evitar mock/stub/placeholder, salvo exceção formal registrada na task.
7. Executar suite.
8. Registrar evidências no fluxo de execução e no Quality Gate.
