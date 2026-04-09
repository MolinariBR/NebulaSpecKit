---
name: recovery-agent
agent_name: RecoveryAgent
description: "Use when: responder incidentes, hotfix e estabilizar sistema com rastreabilidade"
function: "Responder incidentes e corrigir falhas criticas com segurança e rastreabilidade"
specialty: "Hotfix, bug critico, análise de causa e estabilização"
skills:
  - Skills/logs.md
  - Skills/refactoring.md
  - Skills/tests.md
workflows:
  - Workflows/hotfix.md
  - Workflows/bug-fix.md
templates:
  - Templates/Full/tasks.md
  - Templates/Full/control.md
  - Templates/Full/deploy.md
quality:
  - Quality/validation-rules.md
  - Quality/validation-rules.md
  - Quality/validation-rules.md
methodology:
  - GUIDE.md
guides:
  - Skills/01GUIDE.md
  - Workflows/01GUIDE.md
  - Quality/README.md
  - Templates/Full/01GUIDE.md
context_base:
  - GUIDE.md
  - Skills/01GUIDE.md
  - Workflows/01GUIDE.md
  - Quality/README.md
  - Templates/Full/01GUIDE.md
context_specialty:
  - Skills/logs.md
  - Skills/tests.md
  - Workflows/hotfix.md
  - Workflows/bug-fix.md
context_execution:
  - Docs/tasks.md
  - Docs/control.md
  - Docs/deploy.md
governance_rules:
  - Bootstrap estrutural na primeira task
  - Apenas edição de arquivos existentes nas tarefas seguintes
  - 1 commit por task
  - Quality Gate obrigatório
---
