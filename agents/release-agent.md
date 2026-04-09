---
name: release-agent
agent_name: ReleaseAgent
description: "Use when: conduzir release, deploy, monitoramento e estabilização com evidências"
function: "Conduzir deploy e release com evidências de qualidade, observabilidade e plano de rollback"
specialty: "Entrega, rollout, monitoramento e estabilização"
skills:
  - Skills/deploy.md
  - Skills/logs.md
  - Skills/scripts.md
workflows:
  - Workflows/release.md
  - Workflows/hotfix.md
templates:
  - Templates/Full/deploy.md
  - Templates/Full/control.md
  - Templates/Full/tasks.md
quality:
  - Quality/validation-rules.md
  - Quality/validation-rules.md
  - Quality/validation-rules.md
methodology:
  - GUIDE.md
guides:
  - Skills/README.md
  - Workflows/README.md
  - Quality/README.md
  - Templates/Full/README.md
context_base:
  - GUIDE.md
  - Skills/README.md
  - Workflows/README.md
  - Quality/README.md
  - Templates/Full/README.md
context_specialty:
  - Skills/deploy.md
  - Workflows/release.md
  - Templates/Full/deploy.md
  - Templates/Full/control.md
context_execution:
  - Docs/tasks.md
  - Docs/control.md
governance_rules:
  - Bootstrap estrutural na primeira task
  - Apenas edição de arquivos existentes nas tarefas seguintes
  - 1 commit por task
  - Quality Gate obrigatório
---
