---
name: execution
agent_name: Execution
description: "Use when: planejar e executar tarefas com rastreabilidade, governança e entrega continua"
function: "Planejar e executar entrega por task com rastreabilidade, controle e governança"
specialty: "Plan, tasks, controle, implementação e refatoração"
skills:
  - Skills/implementation.md
  - Skills/refactoring.md
  - Skills/logs.md
workflows:
  - Workflows/bootstrap-structure.md
  - Workflows/new-feature.md
  - Workflows/bug-fix.md
  - Workflows/module-refactoring.md
templates:
  - Templates/Full/plan.md
  - Templates/Full/tasks.md
  - Templates/Full/control.md
  - Templates/Full/structure.md
quality:
  - Quality/validation-rules.md
  - Quality/clean-rules.md
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
  - Skills/implementation.md
  - Workflows/new-feature.md
  - Templates/Full/plan.md
  - Templates/Full/tasks.md
  - Templates/Full/control.md
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
