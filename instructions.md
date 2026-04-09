# Instruções

## 1. Objetivo

Este arquivo é a raiz operacional do projeto.
Ele define como desenvolvedores e agentes devem carregar contexto, selecionar workflows, aplicar skills, executar tasks e concluir entregas com qualidade.

Use este arquivo como ponto único de alinhamento para:
- operação humana;
- operação com agentes;
- runtimes de ferramentas (Copilot, Claude Code, OpenCode, Cursor, Windsurf etc.);
- governança de execução e fechamento.

## 2. Escopo de aplicação

Estas instruções valem para:
- início de projeto;
- implementação de feature;
- bug fix e hotfix;
- refatoração;
- integração;
- release;
- revisão e fechamento de task.

Não valem para:
- código gerado automaticamente sem ownership da equipe;
- assets de terceiros sem manutenção local.

## 2.1 Resolução de caminhos

Neste arquivo, `Docs/`, `Workflows/`, `Skills/`, `Quality/`, `Templates/` e `agents/` são caminhos lógicos relativos ao `PROJECT_ROOT`.

Definição de `PROJECT_ROOT`:
- pasta que contém `Docs/`, `Workflows/`, `Skills/`, `Quality/` e `Templates/`.

Neste repositório atual, o `PROJECT_ROOT` é `NebulaSpecKit/`.

## 3. Stack canônico de políticas

Toda execução deve carregar e respeitar os documentos abaixo:

1. `instructions.md` (este arquivo)
2. `NebulaSpecKit/GUIDE.md`
3. `NebulaSpecKit/Manual/17EXECUTION-BASELINE.md`
4. `NebulaSpecKit/Workflows/01GUIDE.md`
5. `NebulaSpecKit/Skills/01GUIDE.md`
6. `NebulaSpecKit/Quality/README.md`
7. `NebulaSpecKit/Quality/execution-policy.md`
8. `NebulaSpecKit/Quality/structure-rules.md`
9. `NebulaSpecKit/Quality/clean-rules.md`
10. `NebulaSpecKit/Quality/metrics.md`
11. `NebulaSpecKit/Quality/review-checklist.md`
12. `NebulaSpecKit/Quality/realistic-tests.md`
13. `NebulaSpecKit/Quality/anti-mock.md`
14. `NebulaSpecKit/Quality/dependencies.md`
15. `NebulaSpecKit/Quality/validation-rules.md`

## 4. Ordem de precedência

Em caso de conflito, aplique esta ordem:

1. `Docs/contract.yaml` (contrato vigente)
2. Documento-fonte do domínio em `Docs/` (ex.: `Docs/architecture.md`, `Docs/design-system.md`)
3. `Docs/plan.md` e `Docs/tasks.md`
4. Workflow principal da task em `Workflows/*.md`
5. `Quality/validation-rules.md` e regras de qualidade
6. `instructions.md`
7. Políticas operacionais complementares (`Quality/execution-policy.md`, `Quality/structure-rules.md`, `Quality/clean-rules.md`, `Quality/metrics.md`, `Quality/review-checklist.md`, `Quality/realistic-tests.md`, `Quality/anti-mock.md`, `Quality/dependencies.md`, `Quality/validation-rules.md`)
8. Implementação atual

## 5. Fluxo oficial de trabalho

### 5.1 Início de projeto

1. Ler `NebulaSpecKit/Docs/get-started.md`.
2. Construir a base documental oficial em `Docs/` (templates são referência, nunca saída final).
3. Selecionar `Workflows/initial-setup.md`.
4. Aprovar `Docs/plan.md`.
5. Abrir a Task 1 com política `bootstrap_estrutural` usando `Workflows/bootstrap-structure.md`.

### 5.2 Ciclo padrão por task

1. Definir objetivo, escopo e limites da task.
2. Selecionar 1 workflow principal.
3. Selecionar skills de suporte (skill nunca substitui workflow).
4. Carregar os docs oficiais da demanda em `Docs/`.
5. Executar a implementação em passos pequenos e verificáveis.
6. Aplicar o Quality Gate.
7. Registrar evidências e rastreabilidade em `Docs/tasks.md` e `Docs/control.md`.
8. Fechar a task com 1 commit.

### 5.3 Fechamento de milestone

1. Selecionar `Workflows/release.md` quando o escopo estiver pronto.
2. Validar o gate final e as evidências operacionais.
3. Registrar o status final em `Docs/control.md`.

## 6. Acionamento de workflows (roteamento)

Escolha exatamente 1 workflow principal por task:

1. Início de execução após `Docs/plan.md` aprovado -> `Workflows/bootstrap-structure.md`
2. Início de projeto após `Docs/brief.md` aprovado -> `Workflows/initial-setup.md`
3. Nova demanda funcional -> `Workflows/new-feature.md`
4. Falha em produção, teste ou comportamento divergente -> `Workflows/bug-fix.md`
5. Incidente crítico em produção -> `Workflows/hotfix.md`
6. Nova tela definida em `Docs/pages.md` -> `Workflows/new-screen.md`
7. Ajuste visual, responsivo ou de acessibilidade -> `Workflows/ui-change.md`
8. Mudança de API, design system ou tokens -> `Workflows/contract-change.md`
9. Novo serviço externo ou comunicação entre módulos -> `Workflows/new-integration.md`
10. Débito técnico, acoplamento excessivo ou divergência estrutural -> `Workflows/module-refactoring.md`
11. Milestone concluída e aprovada -> `Workflows/release.md`

## 7. Acionamento de skills (complementar)

Selecione skills conforme o tipo de trabalho:

1. Implementação geral por task -> `Skills/implementation.md`
2. Refatoração com preservação de comportamento -> `Skills/refactoring.md`
3. Testes, regressão e validação de contrato -> `Skills/tests.md`
4. Alteração de contrato (API, design system, tokens) -> `Skills/contracts.md`
5. Interface e experiência -> `Skills/ui-ux.md`
6. Navegação e transições -> `Skills/flow.md`
7. Comunicação entre módulos/serviços -> `Skills/integration.md`
8. Publicação e operação -> `Skills/deploy.md`
9. Diagnóstico observável -> `Skills/logs.md`
10. Automação operacional -> `Skills/scripts.md`
11. Validação de API com chamadas reproduzíveis -> `Skills/curl.md`
12. Conversão de história em entrega validável -> `Skills/user-stories.md`

Regra fixa:
- a skill guia a especialidade;
- o workflow orquestra a sequência;
- o Quality Gate decide o fechamento.

## 8. Acionamento de agentes (quando em modo com agentes)

Mapeamento rápido:

1. ScopeAgent -> descoberta de escopo e objetivos.
2. ProductAgent -> user stories, fluxo, telas e UX.
3. SystemAgent -> arquitetura, contrato, entidades e integrações.
4. ExecutionAgent -> plan/tasks/control e execução por task.
5. QualityAgent -> aprovação/reprovação de fechamento.
6. ReleaseAgent -> deploy, rollout e estabilização.
7. RecoveryAgent -> incidente e hotfix.

Todo handoff entre agentes deve registrar:
- concluído;
- pendências;
- próximo agente;
- contexto mínimo para o próximo ciclo.

## 9. Prompt inicial canônico (modo com agentes)

```text
Atue como <AgentName>.
Objetivo: <objetivo da task>
Workflow: Workflows/<workflow>.md

Carregue contexto base:
- GUIDE.md
- Skills/01GUIDE.md
- Workflows/01GUIDE.md
- Quality/README.md
- Templates/Full/01GUIDE.md

Carregue contexto especializado conforme agents/<role>-agent.md.
Carregue contexto de execução em Docs/plan.md, Docs/tasks.md e Docs/control.md, quando aplicável.

Aplique governança:
- bootstrap apenas na primeira task
- edit-only após bootstrap
- 1 commit por task
- Quality Gate obrigatório

Entregue:
1) plano
2) execução
3) evidências
4) riscos e pendências
```

## 10. Governança obrigatória por task

1. Bootstrap estrutural apenas na primeira task.
2. Após bootstrap, apenas edição de arquivos existentes.
3. Exatamente 1 commit por task concluída.
4. Nenhuma task fecha sem Quality Gate aprovado.
5. Se um arquivo esperado não existir em task de edição, abrir task de ajuste estrutural.

## 11. Quality Gate mínimo para fechamento

Antes de fechar a task, valide:

1. Lint aprovado.
2. Typecheck aprovado (quando aplicável).
3. Build aprovado (quando aplicável).
4. Testes realistas executados.
5. Sem mock/stub/placeholder fora de exceção formal.
6. API validada com curl e scripts reproduzíveis (quando aplicável).
7. UI validada com e2e (quando aplicável).
8. Mobile validado em BrowserStack (ou alternativa) e em dispositivo físico local para fluxos críticos (quando aplicável).
9. Dependências e lockfile consistentes.
10. Evidências registradas na task.

Se qualquer critério falhar, a task permanece aberta.

## 12. Evidências obrigatórias de encerramento

Registrar em `Docs/tasks.md`:
- status do gate;
- resultados de lint/typecheck/build/testes;
- comandos executados (incluindo curl/scripts, quando houver);
- hash do commit;
- lista de arquivos tocados;
- riscos residuais e pendências.

Registrar em `Docs/control.md`:
- progresso da task;
- handoff (quando houver);
- bloqueios e decisões.

Atualizar `Docs/plan.md` quando houver mudança de milestone, ordem ou dependência macro.

## 13. Regra de implementação durante a execução

Aplicar `Quality/execution-policy.md` como contrato de implementação:
- começar com alvo definido e escopo claro;
- implementar em passos pequenos;
- preservar fronteiras de responsabilidade;
- evitar ampliação de escopo;
- manter legibilidade local;
- concluir somente com critérios de conclusão atendidos.

Aplicar qualidade estrutural com:
- `Quality/clean-rules.md`
- `Quality/structure-rules.md`
- `Quality/metrics.md`
- `Quality/review-checklist.md`
- `Quality/realistic-tests.md`
- `Quality/anti-mock.md`
- `Quality/dependencies.md`
- `Quality/validation-rules.md`

## 14. Integração com runtimes de ferramenta

Adaptadores por ferramenta devem referenciar este arquivo como fonte raiz.
Eles podem adicionar delta nativo da ferramenta, mas não podem contradizer:
- governança por task;
- ordem de precedência;
- seleção de workflow;
- exigência de Quality Gate.

## 15. Definição de pronto

Uma task está pronta apenas quando:

1. O workflow principal foi seguido, sem pular etapas obrigatórias.
2. As skills necessárias foram aplicadas.
3. Os docs oficiais da demanda foram atualizados.
4. O Quality Gate foi aprovado.
5. As evidências e a rastreabilidade foram registradas.
6. O commit único da task foi registrado.
