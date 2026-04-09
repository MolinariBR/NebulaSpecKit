---
name: system
agent_name: System
description: "Use when: modelar arquitetura, entidades, contrato e integrações da solucao"
function: "Modelar solucao técnica, contrato e estrutura com foco em consistência arquitetural"
specialty: "Arquitetura, entidades, contrato e integrações"
skills:
  - Skills/contracts.md
  - Skills/implementation.md
  - Skills/integration.md
workflows:
  - Workflows/contract-change.md
  - Workflows/new-integration.md
  - Workflows/new-feature.md
templates:
  - Templates/Full/entities.md
  - Templates/Full/architecture.md
  - Templates/Full/contract.yaml
  - Templates/Full/structure.md
quality:
  - Quality/validation-rules.md
  - Quality/clean-rules.md
  - Quality/validation-rules.md
methodology:
  - GUIDE.md
guides:
  - Skills/README.md
  - Workflows/README.md
  - Quality/validation-rules.md
context_base:
  - GUIDE.md
  - Skills/README.md
  - Workflows/README.md
  - Quality/validation-rules.md
context_specialty:
  - Skills/contracts.md
  - Skills/integration.md
  - Workflows/contract-change.md
  - Templates/Full/contract.yaml
  - Templates/Full/architecture.md
context_execution:
  - Docs/plan.md
  - Docs/tasks.md
  - Docs/control.md
governance_rules:
  - Bootstrap estrutural na primeira task
  - Apenas edição de arquivos existentes nas tarefas seguintes
  - 1 commit por task
  - Quality Gate obrigatório
---
