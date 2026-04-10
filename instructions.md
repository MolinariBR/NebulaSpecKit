# Instruções

## 1. Objetivo
Raiz operacional para devs, agentes e runtimes. Define carga de contexto, roteamento (workflow/skills/agentes), governança e fechamento.

## 2. Escopo
Válido para: início de projeto, feature, bugfix/hotfix, refatoração, integração, release, revisão e fechamento de task.
Não válido para: código auto-gerado sem ownership e assets de terceiros sem manutenção local.

## 2.1 Caminhos
Use caminhos relativos ao `PROJECT_ROOT`.
`PROJECT_ROOT` = pasta que contém `Docs/`, `Workflows/`, `Skills/`, `Quality/`, `Templates/`, `agents/`.
Neste repositório: `PROJECT_ROOT = NebulaSpecKit/`.
`Manual/` é guia de dev humano; não integra contexto mínimo de modelo.

## 3. Stack canônico

### 3.1 Base obrigatória (sempre)
1. `instructions.md`
2. `GUIDE.md`
3. `Workflows/README.md`
4. `Skills/README.md`
5. `Quality/validation-rules.md`

### 3.2 Stack de qualidade aprofundada (`QUALITY_STACK`)
- `Quality/execution-policy.md`
- `Quality/structure-rules.md`
- `Quality/clean-rules.md`
- `Quality/metrics.md`
- `Quality/review-checklist.md`
- `Quality/realistic-tests.md`
- `Quality/anti-mock.md`
- `Quality/dependencies.md`

### 3.3 Condicional (sob demanda)
1. Documentação/estrutura: `Templates/Full/README.md`, `Docs/get-started.md`
2. Implementação/revisão/correção: `QUALITY_STACK`
3. Modo com agentes: `agents/README.md`, `agents/<role>.md`
4. UI/protótipo: `Docs/Prototype/README.md`
5. Interface operacional curta: `Docs/commands.md`

## 4. Precedência
Em conflito, use esta ordem:
1. `instructions.md` (raiz operacional)
2. `Docs/contract.yaml` (contrato vigente)
3. Documento-fonte do domínio em `Docs/`
4. `Docs/plan.md` e `Docs/tasks.md`
5. Workflow principal em `Workflows/*.md`
6. `Quality/validation-rules.md` + regras de qualidade aplicáveis
7. Implementação atual

`GUIDE.md` detalha o método e deve permanecer aderente a esta ordem de precedência.

## 5. Fluxo oficial

### 5.1 Início de projeto
1. Ler `Docs/get-started.md`
2. Ler `Docs/commands.md` (camada curta de roteamento, opcional)
3. Criar base documental oficial em `Docs/` (template = referência, nunca saída final)
4. Selecionar `Workflows/initial-setup.md`
5. Aprovar `Docs/plan.md`
6. Abrir Task 1 com `bootstrap_estrutural` via `Workflows/bootstrap-structure.md`

### 5.2 Ciclo por task
1. Definir objetivo, escopo e limites
2. Selecionar 1 workflow principal
3. Selecionar skills de suporte (skill não substitui workflow)
4. Carregar docs oficiais da demanda em `Docs/`
5. Implementar em passos pequenos e verificáveis
6. Aplicar Quality Gate
7. Registrar evidências em `Docs/tasks.md` e `Docs/control.md`
8. Fechar com 1 commit

### 5.3 Fechamento de milestone
1. Selecionar `Workflows/release.md`
2. Validar gate final e evidências
3. Registrar status final em `Docs/control.md`

## 6. Roteamento de workflows (1 principal por task)
1. `Docs/plan.md` aprovado (início de execução) -> `Workflows/bootstrap-structure.md`
2. `Docs/brief.md` aprovado (início de projeto) -> `Workflows/initial-setup.md`
3. Nova demanda funcional -> `Workflows/new-feature.md`
4. Falha em produção/teste/comportamento -> `Workflows/bug-fix.md`
5. Incidente crítico em produção -> `Workflows/hotfix.md`
6. Nova tela em `Docs/pages.md` -> `Workflows/new-screen.md`
7. Ajuste visual/responsivo/acessibilidade -> `Workflows/ui-change.md`
8. Mudança de API/design system/tokens -> `Workflows/contract-change.md`
9. Novo serviço externo/comunicação entre módulos -> `Workflows/new-integration.md`
10. Débito técnico/acoplamento/divergência estrutural -> `Workflows/module-refactoring.md`
11. Milestone concluída/aprovada -> `Workflows/release.md`

## 7. Roteamento de skills (complementar)
1. Implementação geral -> `Skills/implementation.md`
2. Refatoração preservando comportamento -> `Skills/refactoring.md`
3. Testes/regressão/contrato -> `Skills/tests.md`
4. Alteração de contrato -> `Skills/contracts.md`
5. Interface/experiência -> `Skills/ui-ux.md`
6. Navegação/transições -> `Skills/flow.md`
7. Integração entre módulos/serviços -> `Skills/integration.md`
8. Publicação/operação -> `Skills/deploy.md`
9. Diagnóstico observável -> `Skills/logs.md`
10. Automação operacional -> `Skills/scripts.md`
11. Validação de API reproduzível -> `Skills/curl.md`
12. História -> entrega validável -> `Skills/user-stories.md`

Regra fixa: skill guia especialidade; workflow orquestra sequência; Quality Gate decide fechamento.

## 8. Agentes (modo com agentes)
Mapeamento: Scope, Product, System, Execution, Quality, Release, Recovery.
Handoff obrigatório: concluído, pendências, próximo agente, contexto mínimo do próximo ciclo.

## 9. Prompt inicial canônico (modo com agentes)
```text
Atue como <AgentName>.
Objetivo: <objetivo da task>
Workflow: Workflows/<workflow>.md

Carregue contexto base:
- GUIDE.md
- Skills/README.md
- Workflows/README.md
- Quality/validation-rules.md

Carregue contexto condicional:
- Templates/Full/README.md (se task exigir definição documental/estrutura)
- QUALITY_STACK (se task envolver implementação, revisão ou correção)

Carregue contexto especializado conforme agents/<role>.md.
Carregue contexto de execução em Docs/plan.md, Docs/tasks.md e Docs/control.md, quando aplicável.

Aplique governança:
- bootstrap apenas na primeira task
- edit-only após bootstrap
- 1 commit por task
- Quality Gate obrigatório

Entregue: 1) plano 2) execução 3) evidências 4) riscos e pendências
```

## 10. Governança obrigatória por task
1. Bootstrap estrutural apenas na primeira task
2. Após bootstrap, apenas edição de arquivos existentes
3. Exatamente 1 commit por task concluída
4. Nenhuma task fecha sem Quality Gate aprovado
5. Se arquivo esperado não existir em task de edição, abrir task de ajuste estrutural

## 11. Quality Gate mínimo
Antes de fechar a task:
1. Lint aprovado
2. Typecheck aprovado (quando aplicável)
3. Build aprovado (quando aplicável)
4. Testes realistas executados
5. Sem mock/stub/placeholder fora de exceção formal
6. API validada com curl e scripts reproduzíveis (quando aplicável)
7. UI validada com e2e (quando aplicável)
8. Mobile validado em BrowserStack (ou alternativa) e em dispositivo físico local para fluxos críticos (quando aplicável)
9. Dependências e lockfile consistentes
10. Evidências registradas na task
Se qualquer critério falhar, a task permanece aberta.

## 12. Evidências obrigatórias
Registrar em `Docs/tasks.md`:
- status do gate
- resultados de lint/typecheck/build/testes
- comandos executados (incluindo curl/scripts, quando houver)
- hash do commit
- lista de arquivos tocados
- riscos residuais e pendências

Registrar em `Docs/control.md`:
- progresso da task
- handoff (quando houver)
- bloqueios e decisões

Atualizar `Docs/plan.md` quando mudar milestone, ordem ou dependência macro.

## 13. Regra de implementação
Aplicar `Quality/execution-policy.md` como contrato:
- alvo definido e escopo claro
- passos pequenos
- fronteiras de responsabilidade preservadas
- sem ampliação de escopo
- legibilidade local
- conclusão apenas com critérios atendidos

Aplicar qualidade estrutural com:
- `Quality/clean-rules.md`
- `Quality/structure-rules.md`
- `Quality/metrics.md`
- `Quality/review-checklist.md`
- `Quality/realistic-tests.md`
- `Quality/anti-mock.md`
- `Quality/dependencies.md`
- `Quality/validation-rules.md`

## 14. Integração com runtimes
Adaptadores por ferramenta devem referenciar este arquivo como raiz.
Podem adicionar delta nativo sem contradizer:
- governança por task
- ordem de precedência
- seleção de workflow
- exigência de Quality Gate

## 15. Definição de pronto
Task pronta apenas quando:
1. Workflow principal seguido sem pular etapas obrigatórias
2. Skills necessárias aplicadas
3. Docs oficiais da demanda atualizados
4. Quality Gate aprovado
5. Evidências e rastreabilidade registradas
6. Commit único da task registrado
