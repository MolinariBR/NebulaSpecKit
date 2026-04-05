# Plataformas de Agentes (IDE e CLI)

Este guia consolida como operar os agentes canônicos do Nébula em ambientes diferentes (IDE e CLI) sem perder governança, rastreabilidade e previsibilidade.

## Objetivo

Padronizar a configuração e a execução dos agentes por plataforma, mantendo um único contrato operacional para todo o framework.

## Escopo

1. Definir o que é canônico e o que é adaptador de runtime.
2. Mapear caminhos físicos por ferramenta.
3. Descrever fluxo de setup e execução por task.
4. Garantir validação mínima antes de fechar qualquer task.

## Fontes analisadas

### Núcleo do framework

- `README.md`
- `GUIDE.md`
- `Docs/README.md`

### Guias e READMEs dos pilares

- `Manual/00README.md`, `Manual/01GUIDE.md`
- `Skills/00README.md`, `Skills/01GUIDE.md`
- `Workflows/00README.md`, `Workflows/01GUIDE.md`
- `Quality/00README.md`, `Quality/01GUIDE.md`
- `Templates/Full/00README.md`, `Templates/Full/01GUIDE.md`
- `Templates/Quick/00README.md`, `Templates/Quick/01GUIDE.md`
- `agents/00README.md`, `agents/01GUIDE.md`
- `agents/behavior/00README.md`, `agents/behavior/01GUIDE.md`
- `Prototype/00README.md`, `Prototype/01GUIDE.md`

### Base canônica de criação de agentes

- `Manual/15CREATE-AGENT-BASELINE.md`
- `Manual/07CREATE-AGENT-GITHUB-COPILOT.md`
- `Manual/08CREATE-AGENT-CURSOR.md`
- `Manual/09CREATE-AGENT-ANTIGRAVITY.md`
- `Manual/10CREATE-AGENT-WINDSURF.md`
- `Manual/11CREATE-AGENT-TRAE.md`
- `Manual/12CREATE-AGENT-CLAUDE-CODE.md`
- `Manual/13CREATE-AGENT-OPEN-CODE.md`
- `Manual/14CREATE-AGENT-ZED.md`

### Documentação web relacionada

- `NebulaWeb/content/docs/agent-platforms-overview.md`
- `NebulaWeb/content/docs/agents.md`
- `NebulaWeb/content/docs/chat-commands.md`
- `NebulaWeb/content/docs/commands-baseline.md`
- `NebulaWeb/content/docs/commands-agents.md`
- `NebulaWeb/content/docs/commands-direct-chat.md`
- `NebulaWeb/content/docs/commands-skills-workflows.md`
- `NebulaWeb/content/docs/ide-github-copilot.md`
- `NebulaWeb/content/docs/ide-cursor.md`
- `NebulaWeb/content/docs/ide-antigravity.md`
- `NebulaWeb/content/docs/ide-windsurf.md`
- `NebulaWeb/content/docs/ide-trae.md`
- `NebulaWeb/content/docs/ide-zed.md`
- `NebulaWeb/content/docs/cli-claude-code.md`
- `NebulaWeb/content/docs/cli-open-code.md`

## Regra de ouro

1. `agents/` é a fonte de verdade dos papéis.
2. IDE/CLI são adaptadores de runtime.
3. Em conflito, prevalece o contrato canônico versionado em `agents/`.

> [!IMPORTANT]
> Nunca transformar configuração nativa da ferramenta em nova regra do framework.

## Invariantes operacionais

1. `Docs/` é o único destino de artefato oficial.
2. `Templates/` é modelo de preenchimento, nunca saída final.
3. `Prototype/` é exclusivo para protótipos HTML.
4. Primeira task: `bootstrap_estrutural`.
5. Após bootstrap: apenas edição de arquivos existentes.
6. Exatamente 1 commit por task concluída.
7. Quality Gate obrigatório para fechamento.

## Contexto obrigatório em qualquer plataforma

### Base

```text
- GUIDE.md
- Skills/01GUIDE.md
- Workflows/01GUIDE.md
- Quality/01GUIDE.md
- Templates/Full/01GUIDE.md
```

### Especialidade

```text
- agents/<role>-agent.md
```

### Execução (quando houver task)

```text
- Docs/plan.md
- Docs/tasks.md
- Docs/control.md
```

## Matriz de plataformas

| Tipo | Plataforma | Runtime nativo principal | Caminhos físicos recomendados |
|---|---|---|---|
| IDE | GitHub Copilot | Custom Agents | `.github/agents/*.agent.md` |
| IDE | Cursor | Rules + `AGENTS.md` | `.cursor/rules/*`, `AGENTS.md` |
| IDE | Antigravity | Rules + Skills + Workflows | `.agents/rules/*`, `.agents/skills/*` |
| IDE | Windsurf | Rules + Skills + Workflows + `AGENTS.md` | `.windsurf/rules/*`, `.windsurf/skills/*`, `.windsurf/workflows/*`, `AGENTS.md` |
| IDE | TRAE | Custom Agents + Rules + Skills | `.trae/rules/*`, `.trae/skills/*` |
| IDE | Zed | Agent Panel + Rules | `.rules` |
| CLI | Claude Code | Subagents | `.claude/agents/*.md` ou `~/.claude/agents/*.md`, `CLAUDE.md` |
| CLI | OpenCode | Agents + config + commands | `.opencode/agents/*.md`, `.opencode/skills/*`, `.opencode/commands/*`, `opencode.json` |

## Delta por plataforma

### GitHub Copilot

1. Criar agentes em `.github/agents`.
2. Usar `*.agent.md` com frontmatter YAML.
3. Validar seleção do agente no chat do Copilot.

### Cursor

1. Centralizar comportamento em `.cursor/rules`.
2. Usar `AGENTS.md` como camada complementar.
3. Garantir que Rules e `AGENTS.md` não entrem em conflito.

### Antigravity

1. Tratar Rules, Skills e Workflows como composição de runtime.
2. Organizar regras em `.agents/rules`.
3. Organizar skills em `.agents/skills/<nome>/SKILL.md`.

### Windsurf

1. Regras em `.windsurf/rules`.
2. Skills em `.windsurf/skills`.
3. Workflows em `.windsurf/workflows` para slash commands.

### TRAE

1. Criar agentes nativos via interface `@`.
2. Reforçar governança em `.trae/rules`.
3. Usar `.trae/skills` para tarefas recorrentes.

### Zed

1. Usar Agent Panel como runtime principal.
2. Consolidar guardrails em `.rules`.
3. Opcionalmente integrar agentes externos via ACP.

### Claude Code

1. Criar subagentes em `.claude/agents` (projeto) ou `~/.claude/agents` (global).
2. Operar via `/agents`.
3. Se usar `AGENTS.md`, importar pelo `CLAUDE.md`.

### OpenCode

1. Definir agentes em `.opencode/agents` ou `opencode.json`.
2. Versionar skills em `.opencode/skills`.
3. Padronizar comandos em `.opencode/commands`.

## Fluxo canônico de implantação

1. Escolher modo de execução: com agentes ou sem agentes.
2. Selecionar workflow principal da demanda.
3. Definir papel de agente por etapa (quando aplicável).
4. Configurar o adaptador nativo da plataforma.
5. Validar contexto mínimo antes da execução.
6. Executar task com evidências.
7. Aplicar Quality Gate.
8. Atualizar `Docs/tasks.md` e `Docs/control.md`.

## Prompt base portável (IDE e CLI)

```text
Atue como <AgentName>.
Objetivo: <objetivo da task>
Workflow: Workflows/<workflow>.md

Carregue contexto base:
- GUIDE.md
- Skills/01GUIDE.md
- Workflows/01GUIDE.md
- Quality/01GUIDE.md
- Templates/Full/01GUIDE.md

Carregue contexto especializado:
- agents/<role>-agent.md

Carregue contexto de execução:
- Docs/plan.md
- Docs/tasks.md
- Docs/control.md

Regras:
- bootstrap apenas na primeira task
- modo edição após bootstrap
- 1 commit por task
- Quality Gate obrigatório

Saída:
1) plano
2) execução
3) evidências
4) riscos e pendências
```

## Checklist de validação

1. Plataforma correta para o contexto do time.
2. Agente correto para a etapa.
3. Workflow principal explícito.
4. Contexto base carregado.
5. Contexto de execução carregado.
6. Regras de governança aplicadas.
7. Evidências registradas em `Docs/tasks.md`.
8. Status real atualizado em `Docs/control.md`.
9. Quality Gate aprovado antes do fechamento.

## Antipadrões críticos

1. Duplicar regras canônicas em vários runtimes e perder sincronização.
2. Executar task sem workflow principal declarado.
3. Tratar `Templates/` como entrega final.
4. Fechar task sem gate aprovado.
5. Fazer handoff sem registrar pendências e próximo responsável.

## Comandos úteis

```bash
cd /home/mau/molinari/Framework

# inventário de READMEs e GUIDEs
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort

# base canônica de agentes
ls agents

# manuais de criação por plataforma
ls Manual | rg 'CREATE-AGENT'

# documentação web de IDE/CLI
ls NebulaWeb/content/docs | rg '^(agent-platforms-overview|ide-|cli-|commands-)'
```

## Encerramento

A padronização entre plataformas não depende de copiar prompts isolados. Ela depende de manter contrato canônico em `agents/`, execução real em `Docs/` e governança obrigatória em cada task.
