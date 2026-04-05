# Skills

Guia operacional consolidado de Skills do Nébula Framework.

## Objetivo

Este documento define como usar skills de forma padronizada para execução técnica especializada, sem quebrar governança, rastreabilidade e qualidade.

## Proposta do pilar

Skills existem para responder **como executar tecnicamente** uma demanda em um domínio específico.

Elas não substituem:

1. Workflow (sequência de execução)
2. Quality Gate (critério de fechamento)
3. Artefatos oficiais em `Docs/` (fonte de verdade)

> [!IMPORTANT]
> Skill é especialização. Workflow continua obrigatório. Quality Gate continua obrigatório.

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

### Skills específicas

- `Skills/implementation.md`
- `Skills/refactoring.md`
- `Skills/tests.md`
- `Skills/contracts.md`
- `Skills/ui-ux.md`
- `Skills/flow.md`
- `Skills/integration.md`
- `Skills/deploy.md`
- `Skills/logs.md`
- `Skills/scripts.md`
- `Skills/curl.md`
- `Skills/user-stories.md`

### Documento web atual

- `NebulaWeb/content/docs/skills.md`

## Regras canônicas de uso

1. Toda skill consulta fontes oficiais em `Docs/` antes da execução.
2. Toda skill mapeia impacto antes de implementar.
3. Skill não substitui workflow nem ordem da task.
4. Toda entrega com skill fecha com Quality Gate aprovado.
5. Evidências em `Docs/tasks.md` e `Docs/control.md`.
6. Regra estrutural permanece: bootstrap na primeira task, edição nas próximas.
7. Exatamente 1 commit por task concluída.

> [!WARNING]
> Aplicar skill sem atualização de evidências torna a task não auditável.

## Relação entre Workflow, Skill e Quality

| Componente | Papel |
|---|---|
| Workflow | Define o fluxo da mudança por tipo de demanda |
| Skill | Define aprofundamento técnico por domínio |
| Quality Gate | Define se pode fechar a task |

Sequência operacional recomendada:

```text
1. Escolher workflow principal
2. Selecionar skill(s) adequada(s)
3. Executar com base em Docs/
4. Validar no Quality Gate
5. Registrar evidências e commit
```

## Catálogo consolidado de skills

| Skill | Quando usar | Fontes principais |
|---|---|---|
| `implementation.md` | Implementar entrega planejada | `Docs/plan.md`, `Docs/tasks.md`, `Docs/project.md` |
| `refactoring.md` | Melhorar estrutura sem mudar comportamento | `Docs/architecture.md`, `Docs/structure.md`, `Docs/contract.yaml` |
| `tests.md` | Validar comportamento, contrato e regressão | `Docs/tasks.md`, `Docs/user-stories.md`, `Docs/contract.yaml`, `Quality/gate.md` |
| `contracts.md` | Criar/revisar contrato de API, design system e tokens | `Docs/contract.yaml`, `Docs/design-system.md`, `Docs/tokens.json` |
| `ui-ux.md` | Implementar/ajustar interface e experiência | `Docs/pages.md`, `Docs/flow.md`, `Docs/design-system.md`, `Docs/tokens.json` |
| `flow.md` | Ajustar navegação e transições | `Docs/flow.md`, `Docs/pages.md` |
| `integration.md` | Integrar módulos/serviços externos | `Docs/contract.yaml`, `Docs/architecture.md`, `Docs/entities.md` |
| `deploy.md` | Publicar com segurança operacional | `Docs/deploy.md`, `Docs/architecture.md`, `Docs/control.md` |
| `logs.md` | Diagnosticar problemas por observabilidade | `Docs/deploy.md`, `Docs/architecture.md` |
| `scripts.md` | Automatizar tarefas operacionais | `Docs/structure.md`, `Docs/deploy.md`, `Quality/gate.md` |
| `curl.md` | Validar endpoints de forma reproduzível | `Docs/contract.yaml`, `Quality/gate.md` |
| `user-stories.md` | Converter histórias em entrega validável | `Docs/user-stories.md`, `Docs/project.md`, `Docs/tasks.md` |

## Fontes de verdade por domínio

| Domínio | Fonte principal | Fontes complementares |
|---|---|---|
| Escopo | `Docs/project.md` | `Docs/plan.md`, `Docs/tasks.md` |
| Requisitos | `Docs/user-stories.md` | `Docs/pages.md`, `Docs/flow.md` |
| UI e experiência | `Docs/design-system.md`, `Docs/tokens.json` | `Docs/pages.md`, `Prototype/` |
| Dados | `Docs/entities.md` | `Docs/contract.yaml`, `Docs/architecture.md` |
| API | `Docs/contract.yaml` | `Docs/entities.md`, `Docs/architecture.md` |
| Estrutura técnica | `Docs/structure.md` | `Docs/architecture.md`, `Docs/stack.md` |
| Operação | `Docs/deploy.md` | `Docs/architecture.md`, `Docs/control.md` |
| Execução | `Docs/plan.md`, `Docs/tasks.md` | `Docs/control.md` |
| Qualidade | `Quality/gate.md` | `Quality/realistic-tests.md`, `Quality/dependencies.md` |

## Fluxo padrão de aplicação de uma skill

```text
1. Analisar demanda e workflow selecionado
2. Revisar fontes oficiais do domínio
3. Mapear impacto técnico e de qualidade
4. Planejar execução
5. Implementar/Executar
6. Testar
7. Validar (Quality Gate)
8. Registrar evidências em Docs/tasks.md e Docs/control.md
```

## Critério de pronto (Definition of Done da skill)

Uma skill foi corretamente aplicada quando:

1. Houve revisão de fontes.
2. Houve mapeamento de impacto.
3. A execução técnica foi concluída.
4. Testes/validações aplicáveis foram executados.
5. Quality Gate da task está aprovado.
6. Evidências foram registradas.

## Padrão mínimo para arquivo de skill

```yaml
---
nome: "Nome da skill"
objetivo: "Objetivo principal em uma frase"
fontes:
  - "Docs/DocumentoPrincipal.md"
  - "Docs/DocumentoComplementar.md"
---
```

## Antipadrões

1. Selecionar skill sem workflow principal.
2. Usar skill para pular documentação em `Docs/`.
3. Encerrar task sem Quality Gate.
4. Não registrar evidências em `Docs/tasks.md`.
5. Usar mock/stub sem exceção formal quando a skill envolve testes realistas.

> [!CAUTION]
> Se a skill não gerar evidência rastreável, ela não deve ser considerada aplicada.

## Comandos úteis

```bash
cd /home/mau/molinari/Framework

# catálogo de skills
ls Skills

# revisar guias/readmes usados como base
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort

# revisar artefatos de execução
ls Docs
```

## Encerramento

Este documento transforma o pilar Skills em operação prática consistente com o método Nébula.

Resumo: workflow organiza, skill especializa, quality valida, Docs rastreia.
