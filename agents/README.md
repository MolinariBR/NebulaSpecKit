# Agentes

Este diretório é a fonte canônica dos papéis de agente do framework Nébula.

## Papel deste diretório

1. Definir papéis de agente com contrato claro.
2. Evitar sobreposição de responsabilidade.
3. Garantir contexto mínimo e governança em toda execução.
4. Manter o contrato canônico separado do runtime por ferramenta.

## Escopo deste guia

1. Como selecionar agente.
2. Como carregar contexto mínimo.
3. Como executar com governança.
4. Como fazer handoff entre agentes.

Detalhes nativos por ferramenta devem ficar fora do contexto operacional carregado pelos agentes.

## Estrutura da pasta

1. Contrato e guia operacional dos agentes: `agents/README.md`
2. Arquivos individuais dos papéis: `agents/*.md`
3. Roteamento de papéis e handoff: neste próprio arquivo

## Limites para manter o minimalismo

1. Regras de contrato e papéis ficam em `agents/`.
2. Runtime por ferramenta fica fora do contexto operacional de `agents/`.
3. Não duplicar no `agents/` detalhes de setup por editor.

## Referências obrigatórias

1. Contrato canônico: `agents/README.md`
2. Arquivos de papel: `agents/*.md`
3. Método base: `Guide-Started.md`
4. Skills: `Skills/README.md`
5. Workflows: `Workflows/README.md`
6. Quality (gate mínimo): `Quality/validation-rules.md`
7. Templates (sob demanda): `Templates/Full/README.md`

## Escolha rápida de agente

1. Scope: descoberta e escopo.
2. Product: produto, fluxo e protótipo.
3. System: arquitetura, contrato e estrutura.
4. Execution: plan, tasks, control e implementação.
5. Quality: gate de qualidade e validação.
6. Release: entrega e estabilização.
7. Recovery: incidente e hotfix.

## Contrato obrigatório por agente

Todo `agents/<role>.md` deve conter frontmatter YAML válido com:

1. Identificação: `name`, `agent_name`, `description`
2. Responsabilidade: `function`, `specialty`
3. Contexto por pilar: `skills`, `workflows`, `templates`, `quality`, `methodology`, `guides`
4. Contexto de execução: `context_base`, `context_specialty`, `context_execution`
5. Regras de governança: `governance_rules`

## Procedimento padrão de chamada

1. Escolher o agente pela seção `Escolha rápida de agente`.
2. Confirmar responsabilidade e handoff esperado.
3. Carregar contexto base obrigatório:
   - `Guide-Started.md`
   - `Skills/README.md`
   - `Workflows/README.md`
   - `Quality/validation-rules.md`
4. Carregar contexto condicional:
   - `Templates/Full/README.md` (quando a task exigir definição documental ou estrutura)
5. Carregar contexto de especialidade do agente.
6. Carregar contexto de execução em `Docs/` quando houver task:
   - `Docs/plan.md`
   - `Docs/tasks.md`
   - `Docs/control.md`
7. Exigir saída com:
   - plano
   - execução
   - evidências
   - riscos e pendências

## Saída mínima por ciclo

1. Objetivo da iteração e escopo aplicado.
2. Arquivos em `Docs/` atualizados no ciclo.
3. Evidências técnicas e status do Quality Gate.
4. Pendências, riscos e próximo agente (quando houver handoff).

## Governança obrigatória

1. Bootstrap estrutural apenas na primeira task.
2. Após bootstrap, apenas edição de arquivos existentes.
3. Exatamente 1 commit por task concluída.
4. Quality Gate obrigatório para fechar task.

## Handoff entre agentes

Todo handoff deve registrar:

1. O que foi concluído.
2. O que ficou pendente.
3. Qual agente deve assumir.
4. Quais arquivos devem ser carregados no próximo ciclo.

## Checklist mínimo de validação

1. Agente correto foi escolhido.
2. Contexto base foi carregado.
3. Contexto especializado foi carregado.
4. Contexto em `Docs/` foi considerado.
5. Regras de governança foram aplicadas.
6. Handoff foi registrado quando necessário.

## Relação com Docs

Quando houver execução de task, os agentes devem trabalhar sobre artefatos oficiais em `Docs/`:

1. `Docs/plan.md`
2. `Docs/tasks.md`
3. `Docs/control.md`
