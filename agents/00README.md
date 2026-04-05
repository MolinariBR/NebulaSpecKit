# Agentes

Este diretório é a fonte canônica dos papéis de agente do framework Nébula.

## Papel Deste Diretório

1. Definir papéis de agente com contrato claro.
2. Evitar sobreposição de responsabilidade.
3. Garantir contexto mínimo e governança em toda execução.
4. Manter o contrato canônico separado do runtime por ferramenta.

## Estrutura da Pasta

1. Contrato canônico dos agentes: `agents/00README.md`
2. Guia operacional dos agentes: `agents/01GUIDE.md`
3. Catálogo de papéis e handoff: `agents/02CATALOG.md`
4. Comportamento operacional: `agents/behavior/00README.md`
5. Guia de comportamento: `agents/behavior/01GUIDE.md`
6. Arquivos individuais dos papéis: `agents/*-agent.md`

## Limites para Manter o Minimalismo

1. Regras de contrato e papéis ficam em `agents/`.
2. Runtime por ferramenta fica no `Manual/`.
3. Não duplicar no `agents/` detalhes de setup por editor.

## Contrato Obrigatório por Agente

Todo `agents/<role>-agent.md` deve conter frontmatter YAML válido com:

1. Identificação: `name`, `agent_name`, `description`
2. Responsabilidade: `function`, `specialty`
3. Contexto por pilar: `skills`, `workflows`, `templates`, `quality`, `methodology`, `guides`
4. Contexto de execução: `context_base`, `context_specialty`, `context_execution`
5. Regras de governança: `governance_rules`

## Regras Mínimas de Execução

1. Bootstrap estrutural apenas na primeira task.
2. Após bootstrap, apenas edição de arquivos existentes.
3. Exatamente 1 commit por task concluída.
4. Quality Gate obrigatório para fechar task.

## Onde Está o Runtime Detalhado

Para manter minimalismo e evitar duplicidade, o passo a passo operacional por ferramenta fica no Manual:

1. Baseline comum: `Manual/15CREATE-AGENT-BASELINE.md`
2. Delta por ferramenta: `Manual/07CREATE-AGENT-GITHUB-COPILOT.md` até `Manual/14CREATE-AGENT-ZED.md`

## Relação com Docs

Quando houver execução de task, os agentes devem trabalhar sobre artefatos oficiais em `Docs/`:

1. `Docs/plan.md`
2. `Docs/tasks.md`
3. `Docs/control.md`
