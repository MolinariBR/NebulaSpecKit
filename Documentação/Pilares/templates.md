# Templates

Guia operacional consolidado de Templates do Nébula Framework.

## Objetivo

Este documento define como usar `Templates/` para acelerar documentação com consistência, sem violar governança, rastreabilidade e qualidade de execução.

## Proposta do pilar

Templates respondem **como estruturar cada artefato documental** antes da execução técnica.

Eles não substituem:

1. `Docs/` como fonte oficial do projeto
2. Workflow de execução por task
3. Quality Gate de fechamento
4. Regras canônicas do `GUIDE.md`

> [!IMPORTANT]
> Template é modelo. Entrega oficial sempre fica em `Docs/`.

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

### Documentação de templates

- `Templates/Full/*.md`, `Templates/Full/tokens.json`, `Templates/Full/contract.yaml`
- `Templates/Quick/*.md`

### Documento web atual

- `NebulaWeb/content/docs/templates.md`

## Regra fundamental

```text
Templates/  -> modelo de preenchimento
Docs/       -> artefato oficial (fonte de verdade)
Prototype/  -> protótipos HTML de validação de interface
```

> [!WARNING]
> Não entregar arquivos diretamente de `Templates/` como documentação final do projeto.

## Full vs Quick

### Quando usar Full

1. Escopo com risco de ambiguidade médio/alto.
2. Integração entre módulos relevante.
3. Necessidade de governança forte.
4. Projeto onde Docs é base de execução para Dev e AI.

### Quando usar Quick

1. Escopo pequeno e claro.
2. Risco de ambiguidade baixo.
3. Velocidade de documentação como prioridade.

### Regra de migração

Se surgir ambiguidade no Quick, migrar para Full **na mesma task**.

> [!NOTE]
> Em caso de dúvida entre os dois modos, priorize Full.

## Catálogo consolidado

### Templates Full

1. `brief.md`
2. `project.md`
3. `stack.md`
4. `user-stories.md`
5. `pages.md`
6. `flow.md`
7. `design-system.md`
8. `tokens.json`
9. `entities.md`
10. `architecture.md`
11. `contract.yaml`
12. `structure.md`
13. `deploy.md`
14. `plan.md`
15. `tasks.md`
16. `control.md`

### Templates Quick

1. `brief.md`
2. `project.md`
3. `stack.md`
4. `user-stories.md`
5. `pages.md`
6. `flow.md`
7. `design-system.md`
8. `entities.md`
9. `architecture.md`
10. `structure.md`
11. `deploy.md`
12. `plan.md`
13. `tasks.md`
14. `control.md`

## Mapa canônico Template -> Docs

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

## Ordem recomendada de criação

```text
1. brief
2. project
3. stack
4. user-stories
5. pages
6. flow
7. prototype (quando houver UI)
8. design-system
9. tokens
10. entities
11. architecture
12. contract
13. structure
14. deploy
15. plan
16. tasks
17. control
```

## Papel prático de cada artefato

### Descoberta e definição

- `brief.md`: captura contexto, problema, objetivo, escopo e riscos.
- `project.md`: consolida definição do produto, limites e sucesso.
- `stack.md`: formaliza escolhas de tecnologia e justificativas.

### Produto e experiência

- `user-stories.md`: comportamentos esperados por perfil.
- `pages.md`: inventário de telas e responsabilidades.
- `flow.md`: jornadas e transições entre páginas.
- `design-system.md`: padrão visual e componentes.
- `tokens.json`: tokens de design estruturados.
- `Prototype/`: validação visual navegável antes da implementação.

### Sistema e operação

- `entities.md`: modelo de domínio e relacionamentos.
- `architecture.md`: estrutura de sistema e fronteiras.
- `contract.yaml`: contrato formal da API.
- `structure.md`: árvore de diretórios/arquivos.
- `deploy.md`: ambientes, pipeline e rollback.

### Execução e rastreabilidade

- `plan.md`: estratégia e fases macro.
- `tasks.md`: execução granular com critérios por task.
- `control.md`: estado real, bloqueios e histórico operacional.

## Regras canônicas de preenchimento

1. Não preencher sem base documental prévia.
2. Não duplicar conteúdo sem necessidade.
3. Não improvisar informação técnica sem fonte.
4. Marcar indefinições explicitamente.
5. Atualizar o artefato quando a fonte de verdade mudar.
6. Manter coerência entre `Docs/pages.md`, `Docs/flow.md` e `Prototype/`.
7. Fechar task apenas com Quality Gate aprovado.
8. Registrar evidências e commit em `Docs/tasks.md`.

## Governança por task

```text
- Task 1: bootstrap_estrutural (cria estrutura completa)
- Tasks seguintes: edição (somente arquivos existentes)
- 1 task = 1 commit
- Quality Gate obrigatório
```

> [!CAUTION]
> Criar novos arquivos em task de edição viola a política do framework.

## Critério de pronto no uso de templates

Uma task de documentação baseada em template só é considerada pronta quando:

1. Artefato oficial correspondente em `Docs/` foi atualizado.
2. Mudança está rastreada em `Docs/tasks.md` e `Docs/control.md`.
3. Quality Gate da task está aprovado.

## Relação com outros pilares

- Workflows: definem a ordem de execução da demanda.
- Skills: orientam a especialidade de implementação.
- Quality: define validação obrigatória da task.
- Agents: executam com contrato e contexto, usando `Docs/` como base.

Resumo operacional:

```text
Template estrutura -> Docs oficializa -> Workflow orquestra -> Skill aprofunda -> Quality valida
```

## Antipadrões

1. Usar `Templates/` como saída final do projeto.
2. Pular `brief/project` e começar por implementação.
3. Preencher `tasks/control` sem refletir estado real.
4. Usar Quick mesmo com ambiguidade alta.
5. Fechar task sem evidências de qualidade.
6. Desalinhamento entre design docs e protótipo.

## Regra de precedência

1. Contrato vigente (`Docs/contract.yaml`).
2. Documento-fonte do domínio em `Docs/`.
3. `Docs/plan.md` e `Docs/tasks.md`.
4. Implementação atual.

## Comandos úteis

```bash
cd /home/mau/molinari/Framework

# catálogo de templates
find Templates -maxdepth 2 -type f | sort

# revisar guias/readmes base
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort

# revisar artefatos oficiais
ls Docs
```

## Encerramento

Templates no Nébula são aceleradores de consistência, não atalhos de governança. O valor do pilar está em reduzir ambiguidade sem perder rastreabilidade de produção.
