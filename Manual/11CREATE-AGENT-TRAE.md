# Create Agents In TRAE

## Escopo Deste Documento

Este manual cobre apenas o delta nativo do TRAE.
O padrão comum de governança, contexto e validação esta em [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md).

## Leitura Obrigatória

1. [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md)
2. [../agents/00README.md](../agents/00README.md)
3. [../agents/02CATALOG.md](../agents/02CATALOG.md)

## Implementação Nativa No TRAE

1. O TRAE possui Custom Agents nativos criados pela interface.
2. Regras de projeto ficam em `.trae/rules`.
3. Skills ficam em `.trae/skills/<name>/SKILL.md`.
4. AGENTS.md na raiz pode ser importado nas configurações.

## Setup Rápido

1. Criar o agente em `@ > Create Agent`.
2. Definir prompt, tools e escopo.
3. Criar rules em `.trae/rules` para governança persistente.
4. Ativar importacao de AGENTS.md quando necessário.

## Exemplo Mínimo

Prompt do agente no TRAE:

```text
You are QualityAgent for Nébula Framework.
Always load GUIDE.md, Quality/01GUIDE.md, Quality/gate.md and Docs/tasks.md.
Enforce bootstrap/edit-only/1-commit-per-task/quality-gate.
Return plan, execution, evidence and pending risks.
```

## Validação Específica Do TRAE

1. Agente aparece em `@`.
2. Rules aplicam conforme modo de ativacao.
3. AGENTS.md entra em contexto quando importado.

## Referências Externas

1. https://docs.trae.ai/ide/agent
2. https://docs.trae.ai/ide/rules
3. https://docs.trae.ai/ide/skills
