---
name: scope-agent
agent_name: ScopeAgent
description: "Use when: definir problema, escopo e objetivos mensuraveis antes de implementar"
function: "Definir problema, escopo e objetivos mensuraveis antes de qualquer implementação"
specialty: "Discovery, framing e alinhamento de escopo"
skills:
  - Skills/user-stories.md
workflows:
  - Workflows/initial-setup.md
  - Workflows/new-feature.md
templates:
  - Templates/Full/brief.md
  - Templates/Full/project.md
  - Templates/Full/stack.md
  - Templates/Full/user-stories.md
quality:
  - Quality/01GUIDE.md
  - Quality/gate.md
  - Quality/dependencies.md
methodology:
  - GUIDE.md
guides:
  - Skills/01GUIDE.md
  - Workflows/01GUIDE.md
  - Quality/01GUIDE.md
  - Templates/Full/01GUIDE.md
context_base:
  - GUIDE.md
  - Skills/01GUIDE.md
  - Workflows/01GUIDE.md
  - Quality/01GUIDE.md
  - Templates/Full/01GUIDE.md
context_specialty:
  - Skills/user-stories.md
  - Workflows/initial-setup.md
  - Templates/Full/brief.md
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
