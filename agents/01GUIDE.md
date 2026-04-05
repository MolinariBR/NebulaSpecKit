# Guia de Uso dos Agentes

Este guia define o procedimento operacional dos agentes dentro do framework.

## Escopo deste Guia

1. Como selecionar agente.
2. Como carregar contexto mínimo.
3. Como executar com governança.
4. Como fazer handoff entre agentes.

Detalhes nativos por ferramenta estão no Manual.

## Referências Obrigatórias

1. Contrato canônico: `agents/00README.md`
2. Catálogo de papéis: `agents/02CATALOG.md`
3. Comportamento operacional: `agents/behavior/01GUIDE.md`
4. Baseline de criação de agentes: `Manual/15CREATE-AGENT-BASELINE.md`
5. Delta por ferramenta: `Manual/07CREATE-AGENT-GITHUB-COPILOT.md` até `Manual/14CREATE-AGENT-ZED.md`

## Procedimento Padrão de Chamada

1. Escolher o agente no catálogo.
2. Confirmar responsabilidade e handoff esperado.
3. Carregar contexto base obrigatório:
   - `GUIDE.md`
   - `Skills/01GUIDE.md`
   - `Workflows/01GUIDE.md`
   - `Quality/01GUIDE.md`
   - `Templates/Full/01GUIDE.md`
4. Carregar contexto de especialidade do agente.
5. Carregar contexto de execução em `Docs/` quando houver task:
   - `Docs/plan.md`
   - `Docs/tasks.md`
   - `Docs/control.md`
6. Exigir saída com:
   - plano
   - execução
   - evidências
   - riscos e pendências

## Saída Mínima por Ciclo

1. Objetivo da iteração e escopo aplicado.
2. Arquivos em `Docs/` atualizados no ciclo.
3. Evidências técnicas e status do Quality Gate.
4. Pendências, riscos e próximo agente (quando houver handoff).

## Governança Obrigatória

1. Bootstrap estrutural apenas na primeira task.
2. Após bootstrap, apenas edição de arquivos existentes.
3. Exatamente 1 commit por task concluída.
4. Quality Gate obrigatório para fechar task.

## Handoff entre Agentes

Todo handoff deve registrar:

1. O que foi concluído.
2. O que ficou pendente.
3. Qual agente deve assumir.
4. Quais arquivos devem ser carregados no próximo ciclo.

## Checklist Mínimo de Validação

1. Agente correto foi escolhido.
2. Contexto base foi carregado.
3. Contexto especializado foi carregado.
4. Contexto em `Docs/` foi considerado.
5. Regras de governança foram aplicadas.
6. Handoff foi registrado quando necessário.
