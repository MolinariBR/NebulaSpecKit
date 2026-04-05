# Get Started

Guia oficial de início do Nébula Framework para execução com rastreabilidade, governança e qualidade de produção.

## Objetivo deste documento

Este Get Started traduz, em um fluxo prático único, as regras distribuídas nos READMEs e GUIDEs do framework para que você comece um projeto sem ambiguidade.

> [!NOTE]
> Este documento é operacional: use como checklist de execução real, não só leitura conceitual.

## Fontes analisadas

### Núcleo do framework

- `README.md`
- `GUIDE.md`
- `Docs/README.md`

### Manual operacional

- `Manual/00README.md`
- `Manual/01GUIDE.md`

### Pilares

- `Skills/00README.md`
- `Skills/01GUIDE.md`
- `Workflows/00README.md`
- `Workflows/01GUIDE.md`
- `Quality/00README.md`
- `Quality/01GUIDE.md`
- `Templates/Full/00README.md`
- `Templates/Full/01GUIDE.md`
- `Templates/Quick/00README.md`
- `Templates/Quick/01GUIDE.md`
- `Prototype/00README.md`
- `Prototype/01GUIDE.md`

### Agentes

- `agents/00README.md`
- `agents/01GUIDE.md`
- `agents/behavior/00README.md`
- `agents/behavior/01GUIDE.md`

### Web (complementar)

- `NebulaWeb/README.md`

## Modelo mental do Nébula

```text
Analisar -> Revisar -> Mapear -> Planejar -> Comparar -> Implementar -> Testar -> Validar
```

Sem documentação viva em `Docs/`, não há execução confiável.

## Regras de ouro (não negociáveis)

1. `Templates/` é modelo. Saída oficial sempre em `Docs/`.
2. Primeira task é sempre `bootstrap_estrutural`.
3. Após bootstrap, tasks operam só em modo edição.
4. Cada task concluída gera exatamente 1 commit.
5. Toda task registra evidência e hash em `Docs/tasks.md`.
6. Estado real da execução deve estar em `Docs/control.md`.
7. Nenhuma task é concluída sem Quality Gate aprovado.
8. Protótipos de interface ficam em `Prototype/`.
9. Workflows definem a sequência obrigatória da mudança.
10. Com agentes, o contrato canônico de papéis está em `agents/`.

> [!IMPORTANT]
> Se uma regra canônica conflitar com prática local do time, prevalece a regra canônica do framework.

## Estrutura mínima do repositório

```text
.
├── README.md
├── GUIDE.md
├── Docs/
├── Templates/
│   ├── Full/
│   └── Quick/
├── Skills/
├── Workflows/
├── Quality/
├── agents/
├── Manual/
└── Prototype/
```

## Caminho recomendado para começar

### Passo 1. Ler base canônica

1. `README.md`
2. `GUIDE.md`
3. `Manual/00README.md`
4. `Manual/01GUIDE.md`

### Passo 2. Definir modo de execução

- Com agentes:
1. `Manual/17EXECUTION-BASELINE.md`
2. `Manual/02AGENTS.md`
3. `agents/00README.md`
4. `agents/01GUIDE.md`

- Sem agentes:
1. `Manual/17EXECUTION-BASELINE.md`
2. `Manual/03NO-AGENTS.md`

### Passo 3. Escolher nível de template

- Menos ambiguidade: `Templates/Full/01GUIDE.md`
- Velocidade com governança mínima: `Templates/Quick/01GUIDE.md`

Regra: se aparecer ambiguidade no Quick, migrar para Full na mesma task.

### Passo 4. Criar base documental em `Docs/`

Ordem recomendada:

1. `Docs/brief.md`
2. `Docs/project.md` + `Docs/stack.md`
3. `Docs/user-stories.md`
4. `Docs/pages.md` + `Docs/flow.md` + `Docs/design-system.md` + `Docs/tokens.json`
5. `Docs/entities.md` + `Docs/architecture.md` + `Docs/contract.yaml` + `Docs/structure.md` + `Docs/deploy.md`
6. `Docs/plan.md` + `Docs/tasks.md` + `Docs/control.md`

## Task 001 obrigatória: bootstrap estrutural

```text
TASK-001
Política: bootstrap_estrutural
Objetivo: criar toda a árvore prevista de diretórios e arquivos
```

Depois da TASK-001, toda nova task é `edição`.

> [!CAUTION]
> Criar diretórios/arquivos em task de edição quebra rastreabilidade e exige task de ajuste estrutural.

## Mapa canônico Templates -> Docs

| Template                          | Saída oficial           |
|-----------------------------------|-------------------------|
| `Templates/Full/brief.md`         | `Docs/brief.md`         |
| `Templates/Full/project.md`       | `Docs/project.md`       |
| `Templates/Full/stack.md`         | `Docs/stack.md`         |
| `Templates/Full/user-stories.md`  | `Docs/user-stories.md`  |
| `Templates/Full/pages.md`         | `Docs/pages.md`         |
| `Templates/Full/flow.md`          | `Docs/flow.md`          |
| `Templates/Full/design-system.md` | `Docs/design-system.md` |
| `Templates/Full/tokens.json`      | `Docs/tokens.json`      |
| `Templates/Full/entities.md`      | `Docs/entities.md`      |
| `Templates/Full/architecture.md`  | `Docs/architecture.md`  |
| `Templates/Full/contract.yaml`    | `Docs/contract.yaml`    |
| `Templates/Full/structure.md`     | `Docs/structure.md`     |
| `Templates/Full/deploy.md`        | `Docs/deploy.md`        |
| `Templates/Full/plan.md`          | `Docs/plan.md`          |
| `Templates/Full/tasks.md`         | `Docs/tasks.md`         |
| `Templates/Full/control.md`       | `Docs/control.md`       |

## Sequência padrão de uma task

1. Definir objetivo e escopo.
2. Selecionar 1 workflow principal em `Workflows/`.
3. Carregar contexto relevante de `Docs/`.
4. Executar mudança técnica.
5. Validar com `Quality/gate.md`.
6. Registrar evidências e resultado do gate.
7. Registrar hash e arquivos tocados.
8. Fechar com 1 commit.

## Fases documentais e execução

| Fase documental | Escopo                                                                  |
|-----------------|-------------------------------------------------------------------------|
| Fase 0          | Descoberta (`brief`)                                                    |
| Fase 1          | Definição (`project`, `stack`)                                          |
| Fase 2          | Requisitos (`user-stories`)                                             |
| Fase 3          | Produto (`pages`, `flow`, `design-system`, `tokens`)                    |
| Fase 4          | Sistema (`entities`, `architecture`, `contract`, `structure`, `deploy`) |
| Fase 5          | Planejamento (`plan`, `tasks`, `control`)                               |

| Fase de execução                                  | Escopo                                  |
|---------------------------------------------------|-----------------------------------------|
| FASE-01                                           | Consolidação documental inicial         |
| FASE-02                                           | Modelagem técnica e preparo de execução |
| FASE-03                                           | Implementação/refatoração por task      |
| FASE-04                                           | Estabilização final e fechamento        |

## Escolha de workflow por cenário

| Cenário                                                           | Workflow |
|-------------------------------------------------------------------|------------------------------------|
| Estrutura inicial do projeto                                      | `Workflows/bootstrap-structure.md` |
| Configuração inicial                                              | `Workflows/initial-setup.md`       |
| Nova funcionalidade                                               | `Workflows/new-feature.md`         |
| Nova tela                                                         | `Workflows/new-screen.md`          |
| Integração externa                                                | `Workflows/new-integration.md`     |
| Correção de bug                                                   | `Workflows/bug-fix.md`             |
| Incidente em produção                                             | `Workflows/hotfix.md`              |
| Mudança de contrato                                               | `Workflows/contract-change.md`     |
| Mudança visual sem nova tela                                      | `Workflows/ui-change.md`           | 
| Refatoração de módulo                                             | `Workflows/module-refactoring.md`  |
| Publicação                                                        | `Workflows/release.md`             |
 
## Quality Gate (obrigatório)

Condição de fechamento de task:

1. Critérios técnicos aplicáveis aprovados.
2. Evidência registrada em `Docs/tasks.md`.
3. Estado atualizado em `Docs/control.md`.
4. Commit único da task documentado.

Sem isso, a task permanece aberta.

> [!WARNING]
> Task sem evidência + gate aprovado não deve ser considerada concluída, mesmo que o código pareça pronto.

## Regra de precedência (em conflito de fonte)

1. Contrato vigente.
2. Documento-fonte do domínio em `Docs/`.
3. Planejamento e rastreio em `Docs/plan.md` e `Docs/tasks.md`.
4. Implementação atual.

## Dependências recomendadas entre artefatos

1. `Docs/contract.yaml` depende de `Docs/entities.md` e `Docs/architecture.md`.
2. `Docs/tasks.md` depende de `Docs/plan.md`.
3. `Docs/tokens.json` depende de `Docs/design-system.md`.
4. `Docs/design-system.md` deve refletir evidência validada em `Prototype/`, quando houver interface.

## Comandos úteis (operação local)

```bash
# entrar no repositório
cd /home/mau/molinari/Framework

# validar estrutura geral
ls -la

# listar READMEs/GUIDEs do framework
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort

# abrir a documentação web (opcional)
cd NebulaWeb
npm install
npm run dev
```

> [!TIP]
> Antes de iniciar uma task, abra lado a lado `Docs/plan.md`, `Docs/tasks.md` e `Docs/control.md`.

## Erros comuns que quebram governança

1. Usar `Templates/` como entrega final.
2. Criar arquivo novo em task de edição.
3. Fechar task sem evidência objetiva.
4. Fechar task sem Quality Gate.
5. Misturar múltiplas tasks em um único commit.
6. Não atualizar `Docs/control.md` em handoff/risco/bloqueio.

## Definition of Done de uma task no Nébula

Uma task só está concluída quando:

1. O workflow foi seguido sem pular etapa obrigatória.
2. O resultado foi refletido nos artefatos oficiais em `Docs/`.
3. O Quality Gate foi aprovado.
4. Evidências e hash de commit foram registrados.
5. O estado real ficou explícito em `Docs/control.md`.

## Próximo passo recomendado

1. Executar a TASK-001 (bootstrap estrutural).
2. Preencher o mínimo documental em `Docs/`.
3. Iniciar TASK-002 já em modo edição com workflow definido.

## Roteiro prático das primeiras 24h

### Janela 0h-2h

1. Ler base canônica (`README.md`, `GUIDE.md`, `Manual/00README.md`, `Manual/01GUIDE.md`).
2. Definir modo de execução (com ou sem agentes).
3. Escolher Full ou Quick para documentação inicial.

### Janela 2h-6h

1. Executar TASK-001 (`bootstrap_estrutural`).
2. Criar documentação mínima em `Docs/` até fase de planejamento (`plan`, `tasks`, `control`).
3. Escolher workflow da primeira entrega real.

### Janela 6h-24h

1. Executar TASK-002 em modo edição.
2. Registrar evidências e atualizar `Docs/tasks.md` + `Docs/control.md`.
3. Aplicar Quality Gate e concluir com 1 commit.
