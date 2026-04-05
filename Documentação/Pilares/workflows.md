# Workflows

Guia operacional consolidado de Workflows do Nébula Framework.

## Objetivo

Padronizar a sequência de execução por tipo de mudança para garantir:

1. Rastreabilidade por task
2. Governança de execução
3. Qualidade verificável no fechamento

## Proposta do pilar

Workflows respondem **em que ordem executar** uma demanda.

Eles não substituem:

1. Skills (especialidade técnica)
2. Quality Gate (decisão de fechamento)
3. Artefatos oficiais em `Docs/` (fonte de verdade)

> [!IMPORTANT]
> Toda task deve escolher exatamente 1 workflow principal.

## Fontes analisadas

### Núcleo do framework

- `README.md`
- `GUIDE.md`
- `Docs/README.md`

### Guides e readmes do framework

- `Manual/00README.md`, `Manual/01GUIDE.md`
- `Skills/00README.md`, `Skills/01GUIDE.md`
- `Workflows/00README.md`, `Workflows/01GUIDE.md`
- `Quality/00README.md`, `Quality/01GUIDE.md`
- `Templates/Full/00README.md`, `Templates/Full/01GUIDE.md`
- `Templates/Quick/00README.md`, `Templates/Quick/01GUIDE.md`
- `agents/00README.md`, `agents/01GUIDE.md`
- `agents/behavior/00README.md`, `agents/behavior/01GUIDE.md`
- `Prototype/00README.md`, `Prototype/01GUIDE.md`
- `NebulaWeb/README.md`

### Documentação de workflows

- `Workflows/bootstrap-structure.md`
- `Workflows/initial-setup.md`
- `Workflows/new-feature.md`
- `Workflows/new-screen.md`
- `Workflows/new-integration.md`
- `Workflows/contract-change.md`
- `Workflows/ui-change.md`
- `Workflows/module-refactoring.md`
- `Workflows/bug-fix.md`
- `Workflows/hotfix.md`
- `Workflows/release.md`

### Documento web atual

- `NebulaWeb/content/docs/workflows.md`

## Regras canônicas de uso

1. Todo workflow inicia com leitura dos artefatos relevantes em `Docs/`.
2. Todo workflow mapeia impacto e dependências antes da execução.
3. Todo workflow encerra com Quality Gate aprovado.
4. Toda task registra commit, arquivos tocados e evidências em `Docs/tasks.md`.
5. Toda task atualiza estado real em `Docs/control.md`.
6. Em `bootstrap_estrutural`, criação de arquivos é permitida.
7. Em `edição`, apenas arquivos existentes podem ser alterados.

> [!WARNING]
> Pular etapa obrigatória do workflow invalida a execução da task.

## Relação entre Workflow, Skill e Quality

| Componente | Papel |
|---|---|
| Workflow | Orquestra sequência por tipo de demanda |
| Skill | Aprofunda execução técnica em cada etapa |
| Quality Gate | Decide se a task pode ser encerrada |

Sequência operacional padrão:

```text
1. Escolher workflow principal
2. Selecionar skills de suporte
3. Executar etapas do workflow
4. Validar no Quality Gate
5. Registrar evidências e commit
```

## Catálogo consolidado de workflows

| Workflow | Quando usar |
|---|---|
| `bootstrap-structure.md` | Primeira task do projeto (criação estrutural) |
| `initial-setup.md` | Início de projeto pós-brief |
| `new-feature.md` | Nova capacidade funcional |
| `new-screen.md` | Nova tela ou jornada visual |
| `new-integration.md` | Integração com serviço externo ou módulo |
| `contract-change.md` | Mudança de contrato (API, DS, tokens) |
| `ui-change.md` | Ajuste visual sem nova tela |
| `module-refactoring.md` | Refatoração estrutural de módulo |
| `bug-fix.md` | Correção de falha com reprodução |
| `hotfix.md` | Incidente crítico em produção |
| `release.md` | Publicação de milestone aprovado |

## Detalhamento por workflow

### Bootstrap Estrutural

**Gatilho:** início de execução com `Docs/plan.md` aprovado.

```text
1. Estrutura de diretórios/arquivos
2. Scripts mínimos (quando aplicável)
3. Integração mínima de build/teste
4. Validação da árvore
5. Commit
6. Quality Gate
7. Atualizar Docs/tasks.md e Docs/control.md
```

**Documentos:** `Docs/structure.md`, `Docs/plan.md`, `Docs/tasks.md`, `Docs/control.md`

> [!CAUTION]
> É o único workflow autorizado a criar caminhos novos.

### Setup Inicial

**Gatilho:** início de projeto após `Docs/brief.md` aprovado.

```text
1. Bootstrap estrutural
2. User Stories
3. Contratos
4. UI/UX
5. Fluxo
6. Prototype (quando aplicável)
7. Integração (quando aplicável)
8. Scripts
9. Testes
10. Deploy
11. Planejamento e controle
12. Quality Gate
```

**Documentos:** `Docs/brief.md`, `Docs/project.md`, `Docs/stack.md`, `Docs/plan.md`, `Docs/tasks.md`, `Docs/control.md`

### Nova Feature

**Gatilho:** nova demanda funcional em `Docs/tasks.md`.

```text
1. User Stories
2. Contratos
3. UI/UX
4. Fluxo
5. Prototype (se houver impacto visual)
6. Implementação
7. Testes
8. Curl (se houver API)
9. Quality Gate
10. Atualizar Docs/control.md
```

**Documentos:** `Docs/project.md`, `Docs/user-stories.md`, `Docs/plan.md`, `Docs/tasks.md`, `Docs/contract.yaml`, `Docs/design-system.md`, `Docs/tokens.json`

### Nova Tela

**Gatilho:** nova tela definida em `Docs/pages.md`.

```text
1. User Stories
2. Contratos visuais
3. UI/UX
4. Fluxo
5. Prototype HTML
6. Integração
7. Testes
8. Quality Gate
9. Atualizar Docs/control.md
```

**Documentos:** `Docs/pages.md`, `Docs/flow.md`, `Docs/design-system.md`, `Docs/tokens.json`, `Prototype/`, `Docs/contract.yaml`

### Nova Integração

**Gatilho:** integração externa ou entre módulos.

```text
1. Contratos
2. Integração
3. Logs
4. Scripts (quando necessário)
5. Testes
6. Curl
7. Quality Gate
8. Atualizar Docs/control.md
```

**Documentos:** `Docs/architecture.md`, `Docs/contract.yaml`, `Docs/entities.md`, `Docs/deploy.md`

### Alteração de Contrato

**Gatilho:** mudança em API, design system ou tokens.

```text
1. Contratos
2. Refatoração (consumidores)
3. Implementação
4. UI/UX (quando visual)
5. Testes
6. Curl (quando API)
7. Quality Gate
8. Atualizar Docs/control.md
```

**Documentos:** `Docs/contract.yaml`, `Docs/design-system.md`, `Docs/tokens.json`, `Docs/entities.md`, `Docs/architecture.md`

### Alteração de UI

**Gatilho:** ajuste visual, responsivo, acessibilidade, padrão de componente.

```text
1. UI/UX
2. Contratos visuais
3. Fluxo
4. Prototype
5. Implementação
6. Testes
7. Quality Gate
8. Atualizar Docs/control.md
```

**Documentos:** `Docs/pages.md`, `Docs/flow.md`, `Docs/design-system.md`, `Docs/tokens.json`, `Prototype/`

### Refatoração de Módulo

**Gatilho:** débito técnico, acoplamento excessivo, divergência estrutural.

```text
1. Logs
2. Refatoração (planejamento)
3. Contratos
4. Testes
5. Implementação
6. Integração
7. Curl
8. Quality Gate
9. Atualizar Docs/control.md
```

**Documentos:** `Docs/architecture.md`, `Docs/entities.md`, `Docs/contract.yaml`, `Docs/structure.md`

### Bug Fix

**Gatilho:** falha em produção, teste ou comportamento divergente.

```text
1. Logs
2. Diagnóstico técnico
3. Contratos (quebra)
4. Testes de reprodução
5. Implementação
6. Curl (quando API)
7. Quality Gate
8. Atualizar Docs/control.md
```

**Documentos:** `Docs/control.md`, `Docs/contract.yaml`, `Docs/architecture.md`, `Docs/user-stories.md`

### Hotfix

**Gatilho:** incidente crítico em produção.

```text
1. Logs
2. Contratos (limites)
3. Testes mínimos de reprodução
4. Implementação de menor risco
5. Deploy
6. Curl
7. Logs pós-deploy
8. Quality Gate
9. Atualizar Docs/control.md
```

**Documentos:** `Docs/control.md`, `Docs/deploy.md`, `Docs/contract.yaml`, `Docs/architecture.md`

### Release

**Gatilho:** milestone concluído e aprovado.

```text
1. Testes
2. Contratos
3. Logs
4. Scripts
5. Deploy
6. Curl
7. Quality Gate
8. Atualizar Docs/control.md
```

**Documentos:** `Docs/deploy.md`, `Docs/control.md`, `Docs/plan.md`, `Docs/tasks.md`, `Docs/contract.yaml`

## Checklist de encerramento de workflow

1. `Quality/gate.md` aprovado.
2. `Docs/control.md` atualizado.
3. `Docs/tasks.md` atualizado com hash, arquivos tocados, evidências e status do gate.
4. `Docs/plan.md` atualizado quando houver impacto macro de fase/dependência.

## Regra de precedência

1. Contrato vigente em `Docs/contract.yaml`.
2. Documento-fonte do domínio em `Docs/`.
3. Planejamento em `Docs/plan.md` e `Docs/tasks.md`.
4. Implementação atual.

## Antipadrões

1. Executar task sem workflow principal.
2. Trocar workflow no meio sem registrar mudança.
3. Pular etapa obrigatória por pressa.
4. Fechar workflow sem gate aprovado.
5. Não registrar evidência/commit em `Docs/tasks.md`.

> [!NOTE]
> Se a demanda não encaixar claramente em um fluxo, reavalie escopo em `Docs/tasks.md` antes de executar.

## Comandos úteis

```bash
cd /home/mau/molinari/Framework

# listar workflows disponíveis
ls Workflows

# revisar guias/readmes de base
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort

# revisar documentos de execução
ls Docs
```

## Encerramento

Workflow organiza a execução, skill aprofunda, quality valida, Docs comprova.

Essa combinação é o núcleo da previsibilidade operacional do Nébula.
