---
name: quality-agent
agent_name: QualityAgent
description: "Use when: validar qualidade, testes realistas e aprovar fechamento de tasks"
function: "Garantir fidelidade de produção e aprovar ou reprovar o fechamento das tasks"
specialty: "Testes realistas, anti-mock, e2e, style e dependências"
skills:
  - Skills/tests.md
  - Skills/scripts.md
  - Skills/curl.md
  - Skills/logs.md
workflows:
  - Workflows/bug-fix.md
  - Workflows/release.md
  - Workflows/hotfix.md
templates:
  - Templates/Full/tasks.md
  - Templates/Full/control.md
  - Templates/Full/deploy.md
quality:
  - Quality/01GUIDE.md
  - Quality/gate.md
  - Quality/realistic-tests.md
  - Quality/anti-mock.md
  - Quality/code-style.md
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
  - Skills/tests.md
  - Skills/scripts.md
  - Skills/curl.md
  - Quality/gate.md
  - Quality/realistic-tests.md
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
