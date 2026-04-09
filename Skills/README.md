# Skills

Índice oficial das skills do framework.

## Papel deste pilar

Orientar execução especializada por domínio técnico e funcional.

## Escopo deste guia

1. Este guia define regras específicas para uso de skills.
2. Regras globais do framework ficam em [../GUIDE.md](../GUIDE.md).
3. Baseline operacional de execução fica em [../Manual/17EXECUTION-BASELINE.md](../Manual/17EXECUTION-BASELINE.md).

## Leitura recomendada

1. [../Manual/17EXECUTION-BASELINE.md](../Manual/17EXECUTION-BASELINE.md)
2. [../Manual/19COMPONENTS-SKILLS.md](../Manual/19COMPONENTS-SKILLS.md)
3. Skill específica da demanda

## Estrutura da pasta

1. `README.md`: regras de uso, fontes por domínio e critério de pronto.
2. `*.md`: uma skill por domínio.

## Catálogo

- `implementation.md`
- `refactoring.md`
- `tests.md`
- `contracts.md`
- `ui-ux.md`
- `flow.md`
- `integration.md`
- `deploy.md`
- `logs.md`
- `scripts.md`
- `curl.md`
- `user-stories.md`

## Princípio comum

Analisar -> Revisar -> Mapear -> Planejar -> Comparar -> Implementar/Executar -> Testar -> Validar

## Regras específicas

1. Skill é guia de especialidade; não substitui workflow.
2. Toda skill deve consultar fontes oficiais em `Docs/` do domínio.
3. Toda skill deve mapear impacto antes da execução.
4. Toda entrega técnica deve encerrar com Quality Gate aprovado.
5. Toda evidência deve ser registrada em [../Docs/tasks.md](../Docs/tasks.md) e [../Docs/control.md](../Docs/control.md), quando aplicável.

## Padrão de frontmatter

Todo arquivo de skill (`*.md`) deve começar com frontmatter YAML mínimo:

```yaml
---
nome: "Nome da skill"
objetivo: "Objetivo principal em uma frase"
fontes:
  - "DocumentoPrincipal.md"
  - "DocumentoComplementar.md"
---
```

## Fontes de verdade por domínio

| Domínio | Fonte principal | Fontes complementares |
| --- | --- | --- |
| Escopo | Docs/project.md | Docs/plan.md, Docs/tasks.md |
| Requisitos | Docs/user-stories.md | Docs/pages.md, Docs/flow.md |
| UI e experiência | Docs/design-system.md, Docs/tokens.json | Docs/pages.md, Docs/Prototype/ |
| Dados | Docs/entities.md | Docs/contract.yaml, Docs/architecture.md |
| API | Docs/contract.yaml | Docs/entities.md, Docs/architecture.md |
| Estrutura técnica | Docs/structure.md | Docs/architecture.md, Docs/stack.md |
| Operação | Docs/deploy.md | Docs/architecture.md, Docs/control.md |
| Execução | Docs/plan.md, Docs/tasks.md | Docs/control.md |
| Qualidade | Quality/validation-rules.md | Quality/realistic-tests.md, Quality/anti-mock.md, Quality/dependencies.md, Quality/metrics.md |

## Critério de pronto de uma skill

Uma skill só encerra quando:

1. Houve revisão de fontes.
2. Houve mapeamento de impacto.
3. Houve execução.
4. Houve teste.
5. Houve validação final.

## Fechamento mínimo

1. Skill aplicada sem substituir workflow.
2. Task encerrada com Quality Gate aprovado em [../Quality/validation-rules.md](../Quality/validation-rules.md).
3. Evidências registradas em [../Docs/tasks.md](../Docs/tasks.md).
